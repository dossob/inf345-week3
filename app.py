from flask import Flask, jsonify

app = Flask(__name__)

notes = [
    {"id": 1, "text": "Learn Flask"},
    {"id": 2, "text": "Complete INF 345 Week 3"}
]


@app.route("/")
def home():
    return jsonify({
        "message": "Notes API is running"
    })


@app.route("/healthz")
def health():
    return jsonify({
        "status": "ok"
    })


@app.route("/notes")
def get_notes():
    return jsonify(notes)


if __name__ == "__main__":
    import os

    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)