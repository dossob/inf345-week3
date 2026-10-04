from flask import Flask, jsonify, request
import os

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


@app.route("/notes", methods=["GET", "POST"])
def get_notes():
    if request.method == "POST":
        data = request.get_json()

        note = {
            "id": len(notes) + 1,
            "text": data["text"]
        }

        notes.append(note)

        return jsonify(note), 201

    return jsonify(notes)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
