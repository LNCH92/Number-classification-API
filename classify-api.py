from flask import Flask, request, jsonify
import math
import requests

app = Flask(__name__)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    return n == sum(i for i in range(1, n) if n % i == 0)

def is_armstrong(n):
    num_str = str(n)
    num_len = len(num_str)
    return n == sum(int(digit) ** num_len for digit in num_str)

def get_fun_fact(number):
    response = requests.get(f'http://numbersapi.com/{number}')
    if response.status_code == 200:
        return response.text
    return "No fun fact available."

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    number = request.args.get('number')
    if not number.isdigit():
        return jsonify({"number": number, "error": True}), 400

    number = int(number)
    properties = []
    if is_armstrong(number):
        properties.append("armstrong")
    if number % 2 != 0:
        properties.append("odd")
    else:
        properties.append("even")

    fun_fact = get_fun_fact(number)

    response = {
        "number": number,
        "is_prime": is_prime(number),
        "is_perfect": is_perfect(number),
        "properties": properties,
        "class_sum": sum(int(digit) for digit in str(number)),
        "fun_fact": fun_fact
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)