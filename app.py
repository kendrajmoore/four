from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/add', methods=['GET'])
def add():
    num1, num2 = request.args.get('num1'), request.args.get('num2')
    sum = int(num1) + int(num2)
    return {
        "sum": sum
    }
    
@app.route('/sub', methods=['POST'])
def sub():
    num1, num2 = request.form.get('num1'), request.form.get('num2')
    diff = int(num1) - int(num2)
    return {
        "diff": diff
    }
    
@app.route('/mult', methods=['POST'])
def mult():
    numbers = request.get_json()
    num1, num2 = numbers['num1'], numbers['num2']
    total = int(num1) * int(num2)
    return {
        "total": total
    }


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)