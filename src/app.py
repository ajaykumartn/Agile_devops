from flask import Flask, request, jsonify
from calculator import add, subtract, multiply, divide

app = Flask(__name__)

@app.route("/")
def home():
    return "Calculator API is running!"

@app.route("/calculate", methods=["POST"])
def calculate():
    data = request.json
    a = data.get("a")
    b = data.get("b")
    operation = data.get("operation")

    try:
        if operation == "add":
            result = add(a, b)
        elif operation == "subtract":
            result = subtract(a, b)
        elif operation == "multiply":
            result = multiply(a, b)
        elif operation == "divide":
            result = divide(a, b)
        else:
            return jsonify({"error": "Invalid operation"}), 400

        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
