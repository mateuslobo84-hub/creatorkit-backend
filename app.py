ANTHROPIC_KEY = os.environ.get("ANTHROPIC_API_KEY", "")
ANTHROPIC_URL = "https://api.anthropic.com/v1/messages"


@app.route("/", methods=["GET"])
def health():
    return jsonify({"status": "CreatorKit API online"}), 200


@app.route("/api/chat", methods=["POST"])
def chat():
    if not ANTHROPIC_KEY:
        return jsonify({"error": "ANTHROPIC_API_KEY não configurada no servidor."}), 500

    body = request.get_json()
    if not body:
        return jsonify({"error": "Body inválido."}), 400

    # garante model e max_tokens corretos
    body["model"] = "claude-sonnet-4-6"
    if "max_tokens" not in body:
        body["max_tokens"] = 3000

    resp = requests.post(
        ANTHROPIC_URL,
        headers={
            "Content-Type": "application/json",
            "x-api-key": ANTHROPIC_KEY,
            "anthropic-version": "2023-06-01",
        },
        json=body,
        timeout=90,
    )

    return jsonify(resp.json()), resp.status_code


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
