# Too Poor to buy Replit Premium.

from flask import Flask
from threading import Thread

app = Flask(' ')

@app.route('/')
def main():
    return "Bot running"

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    server = Thread(target=run)
    server.start()

if __name__ == '__main__':
    keep_alive()
    print("\nOpen mercury.py for the bot. this is only for obtaining flask IP")