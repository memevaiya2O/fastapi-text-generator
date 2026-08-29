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

## সরাসরি GET endpoint

দ্রুত ব্যবহার করার জন্য text query parameter হিসেবে পাঠান:

```text
GET /gen?text=আপনার লেখা
```

সম্পূর্ণ URL-এ text URL-encode করে পাঠানো ভালো:

```text
http://127.0.0.1:8000/gen?text=%E0%A6%B9%E0%A7%8D%E0%A6%AF%E0%A6%BE%E0%A6%B2%E0%A7%8B%20%E0%A6%AA%E0%A7%83%E0%A6%A5%E0%A6%BF%E0%A6%AC%E0%A7%80
```

ব্রাউজারে URL খুললেই `export_######.txt` ফাইল download হবে। cURL দিয়ে:

```bash
curl -G "http://127.0.0.1:8000/gen" \
  --data-urlencode "text=হ্যালো পৃথিবী" \
  -OJ
```

## Endpoint সংক্ষেপ

| Method | Path | কাজ |
|---|---|---|
| GET | `/` | সহজ browser form দেখায় |
| GET | `/gen?text=...` | query parameter-এর text নিয়ে `.txt` download দেয় |
| POST | `/export` | JSON text নিয়ে `.txt` download দেয় |
| POST | `/export-form` | browser form-এর text নিয়ে `.txt` download দেয় |
