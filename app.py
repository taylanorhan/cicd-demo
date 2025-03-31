from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({"message": "Merhaba Dünya!"})

@app.route('/api/status')
def status():
    return jsonify({"status": "çalışıyor", "version": "1.0.0"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)