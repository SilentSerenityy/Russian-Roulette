from flask import Flask
from threading import Thread
app = Flask('')
@app.route('/')
def main():
    return 'Russian Roulette is a go'

def run():
    app.run(host='0.0.0.0', port=3000)

def b():
    server = Thread(target=run)
    server.start()
