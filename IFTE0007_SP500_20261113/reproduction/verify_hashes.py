from pathlib import Path
import hashlib,json
root=Path(__file__).resolve().parents[1]
m=json.loads((root/'MANIFEST_SHA256.json').read_text())
actual={str(p.relative_to(root)) for p in root.rglob('*') if p.is_file() and p.name not in {'MANIFEST_SHA256.json', '.DS_Store', 'Thumbs.db'} and not any(part in {'.git', '__pycache__'} for part in p.relative_to(root).parts)}
assert actual==set(m['files']), 'Missing or unexpected file'
for name,digest in m['files'].items():
 assert hashlib.sha256((root/name).read_bytes()).hexdigest()==digest,name
print('PASS: all',len(actual),'payload files match SHA-256; no unexpected files.')
