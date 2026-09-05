"""Package the catalogue's explicit public files; exclude working files and metadata."""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED, ZipInfo
import json
import shutil
import tempfile

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / 'output'
SITE = OUTPUT / 'site'
ids = json.loads((ROOT / 'content/catalogue.json').read_text())
files = {'index.html': (SITE / 'index.html').read_bytes()}
legacy = []
for work_id in ids:
    assert work_id.startswith(('wtc-i-', 'wtc-ii-')) and '/' not in work_id
    work_dir = ROOT / 'content/fugues' / work_id
    metadata = json.loads((work_dir / 'metadata.json').read_text())
    prefix = f'fugues/{work_id}/'
    html = (SITE / prefix / 'index.html').read_bytes()
    files[prefix + 'index.html'] = html
    work_files = {'index.html': html.replace(b' data-collection-href="../../index.html"', b'')}
    for source in metadata['publicFiles']:
        assert '..' not in Path(source).parts and not Path(source).is_absolute()
        target = 'SOURCE-NOTICES.txt' if source == 'sources/NOTICE.txt' else source
        data = (work_dir / source).read_bytes()
        assert (SITE / prefix / target).read_bytes() == data, f'Rebuild stale document: {source}'
        files[prefix + target] = data
        work_files[target] = data
    if metadata.get('legacyArchive'):
        name = metadata['legacyArchive']
        assert Path(name).name == name and name.endswith('.zip')
        legacy.append((name, work_files))


def archive(name, contents):
    with ZipFile(OUTPUT / name, 'w', compression=ZIP_DEFLATED, compresslevel=9) as z:
        for path, data in contents.items():
            info = ZipInfo(path, date_time=(2020, 1, 1, 0, 0, 0))
            info.compress_type = ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            z.writestr(info, data)
    with ZipFile(OUTPUT / name) as z:
        assert set(z.namelist()) == set(contents)
        assert z.testzip() is None
        assert all(z.read(path) == data for path, data in contents.items())


# Replace this generated directory, so removed works/assets cannot linger in a release.
with tempfile.TemporaryDirectory(prefix='release-build-', dir=OUTPUT) as staging:
    staged = Path(staging) / 'release'
    for name, data in files.items():
        target = staged / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
    release = OUTPUT / 'release'
    if release.exists():
        shutil.rmtree(release)
    shutil.move(str(staged), release)
archive('wtc-fugues-public.zip', files)
for name, contents in legacy:
    archive(name, contents)
print(f'Packaged collection: {len(ids)} fugue(s), {len(files)} public files. Individual legacy archives retained.')
