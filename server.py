import http.server
import socketserver
import os
import re
import sys
import webbrowser

PORT = 8123
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class RangeFileWrapper:
    def __init__(self, f, length):
        self.f = f
        self.remaining = length

    def read(self, size=-1):
        if self.remaining <= 0:
            return b""
        to_read = self.remaining if size < 0 else min(size, self.remaining)
        data = self.f.read(to_read)
        self.remaining -= len(data)
        return data

    def close(self):
        self.f.close()

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def end_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Accept-Ranges", "bytes")
        super().end_headers()

    def send_head(self):
        if "Range" not in self.headers:
            return super().send_head()

        path = self.translate_path(self.path)
        if not os.path.isfile(path):
            return super().send_head()

        range_header = self.headers["Range"]
        match = re.match(r"bytes=(\d+)-(\d*)", range_header)
        if not match:
            return super().send_head()

        total_size = os.path.getsize(path)
        start = int(match.group(1))
        end = int(match.group(2)) if match.group(2) else total_size - 1
        end = min(end, total_size - 1)
        length = end - start + 1

        self.send_response(206)
        self.send_header("Content-Type", self.guess_type(path))
        self.send_header("Content-Range", f"bytes {start}-{end}/{total_size}")
        self.send_header("Content-Length", str(length))
        self.end_headers()

        f = open(path, "rb")
        f.seek(start)
        return RangeFileWrapper(f, length)

def main():
    os.chdir(DIRECTORY)
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
        print(f"Servidor iniciado en http://localhost:{PORT}")
        print(f"Sirviendo directorio: {DIRECTORY}")
        webbrowser.open(f"http://localhost:{PORT}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServidor detenido.")

if __name__ == "__main__":
    main()
