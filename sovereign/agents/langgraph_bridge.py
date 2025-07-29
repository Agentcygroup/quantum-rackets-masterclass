import requests

def send_commit_event():
    payload = {"event": "commit"}
    print("📡 Triggering LangGraph...")
    requests.post("http://localhost:8080/hook", json=payload)

if __name__ == "__main__":
    send_commit_event()
