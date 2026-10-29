
from flask import Flask, jsonify, request

app = Flask(__name__)
balance = 1000.00


@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Simple Banking Application</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                max-width: 500px;
                margin: 40px auto;
                padding: 20px;
                background: #f1f5f9;
            }
            .card {
                background: white;
                padding: 25px;
                border-radius: 12px;
            }
            input, button {
                padding: 10px;
                margin: 8px 0;
                width: 100%;
                box-sizing: border-box;
            }
            button {
                background: #155eef;
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Simple Banking Application</h1>
            <h3 id="balance">Loading balance...</h3>

            <button onclick="checkBalance()">1. Check Balance</button>

            <h3>2. Deposit Money</h3>
            <input id="depositAmount" type="number"
                   min="0.01" step="0.01" placeholder="Deposit amount">
            <button onclick="transact('/deposit', 'depositAmount')">
                Deposit
            </button>

            <h3>3. Withdraw Money</h3>
            <input id="withdrawAmount" type="number"
                   min="0.01" step="0.01" placeholder="Withdrawal amount">
            <button onclick="transact('/withdraw', 'withdrawAmount')">
                Withdraw
            </button>

            <p id="message"></p>
        </div>

        <script>
        async function checkBalance() {
            const response = await fetch('/balance');
            const data = await response.json();
            document.getElementById('balance').textContent =
                'Balance: Rs. ' + data.balance.toFixed(2);
        }

        async function transact(url, inputId) {
            const amount = Number(document.getElementById(inputId).value);

            const response = await fetch(url, {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({amount: amount})
            });

            const data = await response.json();
            document.getElementById('message').textContent = data.message;

            if (response.ok) {
                document.getElementById(inputId).value = '';
            }

            await checkBalance();
        }

        checkBalance();
        </script>
    </body>
    </html>
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
    data = request.get_json(silent=True) or {}
    amount = data.get("amount")

    if isinstance(amount, bool) or not isinstance(amount, (int, float)):
        return jsonify(message="Invalid deposit amount"), 400

    if not 0 < amount < 1_000_000_000:
        return jsonify(message="Enter a valid positive amount"), 400

    balance = round(balance + amount, 2)
    return jsonify(message="Deposit successful", balance=balance), 200


@app.route("/withdraw", methods=["POST"])
def withdraw():
    global balance
    data = request.get_json(silent=True) or {}
    amount = data.get("amount")

    if isinstance(amount, bool) or not isinstance(amount, (int, float)):
        return jsonify(message="Invalid withdrawal amount"), 400

    if not 0 < amount < 1_000_000_000:
        return jsonify(message="Enter a valid positive amount"), 400

    if amount > balance:
        return jsonify(message="Insufficient balance"), 400

    balance = round(balance - amount, 2)
    return jsonify(message="Withdrawal successful", balance=balance), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
