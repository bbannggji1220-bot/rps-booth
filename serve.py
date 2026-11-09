# 게임 파일을 localhost:8765로 열어 주는 작은 서버.
# 브라우저가 예전 게임 파일을 기억(캐시)하지 않도록 매번 새로 받게 합니다.
import http.server
import socketserver

PORT = 8765


class NoCacheHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()


try:
    httpd = socketserver.TCPServer(("127.0.0.1", PORT), NoCacheHandler)
except OSError:
    print("이미 게임 서버가 켜져 있어요. 먼저 열려 있는 '게임 실행' 창을 닫고 다시 실행해 주세요.")
    input("엔터를 누르면 닫힙니다...")
    raise SystemExit(1)

with httpd:
    print(f"http://localhost:{PORT}/index.html 에서 게임이 실행 중입니다.")
    httpd.serve_forever()
