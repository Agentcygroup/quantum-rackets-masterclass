#!/usr/bin/env python3
import os
import time

def get_heartbeat_file():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    hb_file = os.path.join(base_dir, "heartbeat.log")
    os.makedirs(os.path.dirname(hb_file), exist_ok=True)
    if not os.path.exists(hb_file):
        with open(hb_file, "w") as f:
            f.write("💓 Heartbeat init\n")
    return hb_file

def heartbeat_loop():
    hb_file = get_heartbeat_file()
    while True:
        with open(hb_file, "a") as f:
            f.write("💓 Heartbeat: " + str(time.time()) + "\n")
        time.sleep(5)

if __name__ == "__main__":
    heartbeat_loop()
