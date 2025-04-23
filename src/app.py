from flask import Flask, request, jsonify
from calculator import add, subtract, multiply, divide

app = Flask(__name__)

@app.route("/")
def home():
    return "Calculator API is running!"

@app.route("/form")
def form():
    return '''
        <h2>Calculator Form</h2>
        <form action="/calculate" method="post">
            <label>A: <input name="a" type="number" step="any"></label><br><br>
            <label>B: <input name="b" type="number" step="any"></label><br><br>
            <label>Operation:
                <select name="operation">
                    <option value="add">Add</option>
                    <option value="subtract">Subtract</option>
                    <option value="multiply">Multiply</option>
                    <option value="divide">Divide</option>
                </select>
            </label><br><br>
            <input type="submit" value="Calculate">
        </form>
    '''

@app.route("/calculate", methods=["POST"])
def calculate():
    if request.content_type == 'application/json':
        data = request.get_json()
        a = float(data.get("a"))
        b = float(data.get("b"))
        operation = data.get("operation")
    else:
        a = float(request.form.get("a"))
        b = float(request.form.get("b"))
        operation = request.form.get("operation")

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

        if request.content_type == 'application/json':
            return jsonify({"result": result})
        else:
            return f"<h3>Result: {result}</h3>"

    except Exception as e:
        if request.content_type == 'application/json':
            return jsonify({"error": str(e)}), 500
        else:
            return f"<h3>Error: {str(e)}</h3>", 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
