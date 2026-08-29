from io import BytesIO
import secrets

from fastapi import FastAPI
from fastapi.responses import HTMLResponse, StreamingResponse
from pydantic import BaseModel

app = FastAPI(title="Simple Text File Generator")


class TextRequest(BaseModel):
    text: str


def make_filename() -> str:
    """Return a filename containing a zero-padded six-digit numeric ID."""
    file_id = secrets.randbelow(1_000_000)
    return f"export_{file_id:06d}.txt"


@app.get("/", response_class=HTMLResponse)
def home() -> str:
    return """<!doctype html>
<html lang="bn">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Text File Generator</title>
  <style>
    body { max-width: 720px; margin: 48px auto; padding: 0 20px; font-family: sans-serif; line-height: 1.5; }
    textarea { width: 100%; min-height: 260px; padding: 12px; box-sizing: border-box; font-size: 16px; }
    button { margin-top: 14px; padding: 10px 18px; font-size: 16px; cursor: pointer; }
  </style>
</head>
<body>
  <h1>Text File Generator</h1>
  <p>লেখা দিন, তারপর Export চাপুন। ফাইলটি <code>export_######.txt</code> নামে ডাউনলোড হবে।</p>
  <form action="/export-form" method="post">
    <textarea name="text" placeholder="এখানে আপনার লেখা দিন..."></textarea>
    <br>
    <button type="submit">Export TXT</button>
  </form>
</body>
</html>"""


@app.get("/gen")
def generate_text(text: str = "") -> StreamingResponse:
    """Accept text through ?text=... and return it as a UTF-8 download."""
    content = text.encode("utf-8")
    return StreamingResponse(
        BytesIO(content),
        media_type="text/plain; charset=utf-8",
        headers={"Content-Disposition": f'attachment; filename="{make_filename()}"'},
    )


@app.get("/gen")
def generate_text(text: str = "") -> StreamingResponse:
    """Accept text through ?text=... and return it as a UTF-8 download."""
    content = text.encode("utf-8")
    return StreamingResponse(
        BytesIO(content),
        media_type="text/plain; charset=utf-8",
        headers={"Content-Disposition": f'attachment; filename="{make_filename()}"'},
    )


@app.post("/export")
def export_text(payload: TextRequest) -> StreamingResponse:
    """Accept JSON text and return it as a UTF-8 downloadable TXT file."""
    content = payload.text.encode("utf-8")
    return StreamingResponse(
        BytesIO(content),
        media_type="text/plain; charset=utf-8",
        headers={"Content-Disposition": f'attachment; filename="{make_filename()}"'},
    )


@app.post("/export-form")
async def export_form(text: str = "") -> StreamingResponse:
    """Accept the browser form and return the same UTF-8 TXT download."""
    content = text.encode("utf-8")
    return StreamingResponse(
        BytesIO(content),
        media_type="text/plain; charset=utf-8",
        headers={"Content-Disposition": f'attachment; filename="{make_filename()}"'},
    )
