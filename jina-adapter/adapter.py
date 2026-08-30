import json
import urllib.request
from http.server import BaseHTTPRequestHandler, HTTPServer
from concurrent.futures import ThreadPoolExecutor

READER = "http://jina-reader:8081"

def fetch(url):
    try:
        req = urllib.request.Request(READER + "/" + url, headers={"User-Agent": "owui-jina-adapter/1.0"})
        with urllib.request.urlopen(req, timeout=90) as r:
            text = r.read().decode("utf-8", "ignore")
        return {"page_content": text, "metadata": {"source": url}}
    except Exception as e:
        return {"page_content": "", "metadata": {"source": url, "error": str(e)}}

class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers.get("Content-Length", 0))
        body = json.loads(self.rfile.read(length) or b"{}")
        urls = body.get("urls", [])
        with ThreadPoolExecutor(max_workers=5) as ex:
            out = list(ex.map(fetch, urls))
        payload = json.dumps(out).encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def log_message(self, fmt, *args):
        pass

if __name__ == "__main__":
    HTTPServer(("0.0.0.0", 8091), Handler).serve_forever()
