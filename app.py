from flask import Flask
import os

app = Flask(__name__)

@app.route('/status', methods=['GET'])
def status():
    return "OK", 200

@app.route('/exit', methods=['GET'])
def exit_app():
    os._exit(0)
    return "Exited", 200

@app.route('/cpu', methods=['GET'])
def cpu():
    # Simulate CPU intensive task
    x = 0
    while True:
        x += 1
    return "Using CPU", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
