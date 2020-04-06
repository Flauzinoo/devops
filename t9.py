import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)

@app.route('/')
def primos():
    p = 2
    n = 3

    primos = '1, 2, '
    while p < 100:
        x = 1
        for k in range(2, n):
            if n % k == 0:
                x = 0
                break
        if (x):
            primos = primos + str(n) + ','
            p += 1
        n += 1
    return primos



if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

