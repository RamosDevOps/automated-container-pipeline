from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify(status="healthy", message="DevOps Pipeline is Active!")

if __name__ == '__main__':
    # Running on 0.0.0.0 is critical for Docker container networking
    app.run(host='0.0.0.0', port=5000)