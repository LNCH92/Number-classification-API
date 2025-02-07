from flask import Flask, request, jsonify
import math
import requests
from functools import lru_cache

app = Flask(__name__)

@lru_cache(maxsize=128)
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

@lru_cache(maxsize=128)
def is_perfect(n):
    if n < 2:
        return False
    sum_divisors = 1
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            sum_divisors += i
            if i != n // i:
                sum_divisors += n // i
    return sum_divisors == n

@lru_cache(maxsize=128)
def is_armstrong(n):
    num_str = str(n)
    num_len = len(num_str)
    return n == sum(int(digit) ** num_len for digit in num_str)

@lru_cache(maxsize=128)
def get_fun_fact(number):
    response = requests.get(f'http://numbersapi.com/{number}')
    if response.status_code == 200:
        return response.text
    return "No fun fact available."

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    number_str = request.args.get('number')
    try:
        number = float(number_str)
    except ValueError:
        return jsonify({"number": number_str, "error": True}), 400

    properties = []
    if is_armstrong(int(abs(number))):  # Use absolute value for Armstrong check
        properties.append("armstrong")
    if number % 2 != 0:
        properties.append("odd")
    else:
        properties.append("even")

    fun_fact = get_fun_fact(int(number))

    response = {
        "number": number,
        "is_prime": is_prime(int(number)),
        "is_perfect": is_perfect(int(number)),
        "properties": properties,
        "class_sum": sum(int(digit) for digit in str(int(abs(number)))),  # Use absolute value for class sum
        "fun_fact": fun_fact
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)