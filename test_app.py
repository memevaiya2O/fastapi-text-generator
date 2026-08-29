from pathlib import Path
import json
import re
from urllib.request import Request, urlopen

text = "হ্যালো পৃথিবী\nSimple test"
request = Request(
    "http://127.0.0.1:8000/export",
    data=json.dumps({"text": text}, ensure_ascii=False).encode("utf-8"),
    headers={"Content-Type": "application/json"},
    method="POST",
)
with urlopen(request, timeout=10) as response:
    body = response.read()
    status_code = response.status
    header = response.headers["content-disposition"]
assert status_code == 200
assert body.decode("utf-8") == text
assert re.fullmatch(r'attachment; filename="export_\d{6}\.txt"', header)
Path("verified_export.txt").write_bytes(body)
print("PASS", header)
