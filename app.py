from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify({"message": "Hello from Thanawat"})

@app.route('/api/me', methods=['GET'])
def me():
    return jsonify({"message": "My name is Thanawat Srisaeng"})

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({"message": "up"})

@app.route('/api/goodbye', methods=['GET'])
def goodbye():
    return jsonify({"message": "Goodbye from Flask API!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
