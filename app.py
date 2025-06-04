from flask import Flask, request, jsonify
from rag_pipeline import query_rag

app = Flask(__name__)

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    question = data.get("query")
    if not question:
        return jsonify({"error": "Query not provided"}), 400
    response = query_rag(question)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
