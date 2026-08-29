from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Mera Calculator</h1>
    <form method="POST" action="/calculate">
        <input type="number" name="num1" placeholder="Pehla number"><br><br>
        <input type="number" name="num2" placeholder="Doosra number"><br><br>
        <select name="operator">
            <option value="+">+ (Jama)</option>
            <option value="-">- (Minus)</option>
            <option value="*">* (Zarb)</option>
            <option value="/">(Taqseem)</option>
        </select><br><br>
        <button type="submit">Calculate!</button>
    </form>
    """

@app.route("/calculate", methods=["POST"])
def calculate():
    num1 = float(request.form["num1"])
    num2 = float(request.form["num2"])
    operator = request.form["operator"]

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            result = "Zero se divide nahi ho sakta!"
        else:
            result = num1 / num2

    return f"""
    <h1>Mera Calculator</h1>
    <p>{num1} {operator} {num2} = <b>{result}</b></p>
    <a href="/">Wapas jao</a>
    """

if __name__ == "__main__":
    app.run(debug=True)