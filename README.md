# FastAPI Simple Text File Generator

এটি একটি ছোট FastAPI অ্যাপ। যেকোনো টেক্সট পাঠালে সেটি UTF-8 `.txt` ফাইল হিসেবে ডাউনলোড হয়। প্রতিটি ফাইলের নামের ধরন হলো `export_######.txt`, যেখানে `######` ছয় সংখ্যার একটি আইডি।

## চালানোর নিয়ম

```bash
cd /home/ubuntu/fastapi-text-generator
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
```

এরপর ব্রাউজারে `http://127.0.0.1:8000` খুলে ফর্মে লেখা দিয়ে **Export TXT** চাপুন।

## API ব্যবহার

`POST /export` endpoint-এ JSON পাঠাতে হবে:

```bash
curl -X POST http://127.0.0.1:8000/export \
  -H 'Content-Type: application/json' \
  --data-raw '{"text":"হ্যালো পৃথিবী\nএটি একটি টেস্ট লেখা।"}' \
  -o export.txt -D headers.txt
```

সার্ভার `Content-Disposition` header-এ আসল ডাউনলোড নাম, যেমন `export_042781.txt`, পাঠাবে। API-টি খালি লেখাও গ্রহণ করে এবং লেখার বাংলা, ইংরেজি, Unicode ও line break অপরিবর্তিত রাখে।

## Endpoint সংক্ষেপ

| Method | Path | কাজ |
|---|---|---|
| GET | `/` | সহজ browser form দেখায় |
| POST | `/export` | JSON text নিয়ে `.txt` download দেয় |
| POST | `/export-form` | browser form-এর text নিয়ে `.txt` download দেয় |
