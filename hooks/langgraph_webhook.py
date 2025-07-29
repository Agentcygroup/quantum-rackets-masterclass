from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class LangGraphHookHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length)
        print("📡 LangGraph Trigger Received:", json.loads(post_data))
        self.send_response(200)
        self.end_headers()

if __name__ == "__main__":
    print("🛰️ LangGraph webhook server running on port 8088...")
    HTTPServer(('localhost', 8088), LangGraphHookHandler).serve_forever()
