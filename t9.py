import os
from flask import Flask, jsonify, request
from math import sqrt

app = Flask(__name__)

@app.route('/')
def p():
    c = 0
    n = 2
    lista = []

    while c <= 100:
        normal = False
        for k in range(2, n):
            if n % k == 0:
                normal = True
                break
        if not normal:
            c += 1
            lista.append(n)
        n += 1
    return lista


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

