
from flask import Flask, jsonify, request

app = Flask(__name__)
balance = 1000.00


@app.route("/")
def home():
    return """
    <h1>Simple Banking Application</h1>
    <button onclick="location.href='/balance'">Check Balance</button>
    <form action="/deposit" method="post">
        <input name="amount" type="number" step="0.01"
               min="0.01" required placeholder="Deposit amount">
        <button type="submit">Deposit</button>
    </form>
    <form action="/withdraw" method="post">
        <input name="amount" type="number" step="0.01"
               min="0.01" required placeholder="Withdrawal amount">
        <button type="submit">Withdraw</button>
    </form>
    """


@app.route("/health")
def health():
    return jsonify(status="healthy"), 200


@app.route("/balance")
def check_balance():
    return jsonify(balance=round(balance, 2)), 200


@app.route("/deposit", methods=["POST"])
def deposit():
    global balance

    amount = request.form.get("amount")
    if amount is None:
        data = request.get_json(silent=True) or {}
        amount = data.get("amount")

    try:
        if isinstance(amount, bool):
            raise ValueError
        amount = float(amount)
    except (ValueError, TypeError):
        return jsonify(message="Invalid deposit amount"), 400

    if amount <= 0:
        return jsonify(message="Amount must be positive"), 400

    balance = round(balance + amount, 2)
    return jsonify(message="Deposit successful", balance=balance), 200


@app.route("/withdraw", methods=["POST"])
def withdraw():
    global balance

    data = request.get_json(silent=True)
    amount = request.form.get("amount") if data is None else data.get("amount")

    try:
        if isinstance(amount, bool):
            raise ValueError
        amount = float(amount)
    except (ValueError, TypeError):
        return jsonify(message="Invalid withdrawal amount"), 400

    if amount <= 0:
        return jsonify(message="Amount must be positive"), 400

    if amount > balance:
        return jsonify(message="Insufficient balance"), 400

    balance = round(balance - amount, 2)
    return jsonify(message="Withdrawal successful", balance=balance), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
