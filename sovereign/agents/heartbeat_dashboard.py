import os
import time

HEARTBEAT_FILE = os.path.join(os.path.dirname(__file__), "heartbeat.log")

# Ensure the file exists
os.makedirs(os.path.dirname(HEARTBEAT_FILE), exist_ok=True)
if not os.path.exists(HEARTBEAT_FILE):
    with open(HEARTBEAT_FILE, "w") as f:
        f.write("💓 Heartbeat init\n")

def heartbeat_loop():
    while True:
        with open(HEARTBEAT_FILE, "a") as f:
            f.write("💓 Heartbeat: " + str(time.time()) + "\n")
        time.sleep(5)

if __name__ == "__main__":
    heartbeat_loop()
