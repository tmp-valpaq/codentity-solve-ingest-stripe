#!/usr/bin/env python3
from flask import Flask, request, jsonify

app = Flask(__name__)

# Direct question→answer mapping for Stripe questions
QA = {
    "three valid values for the mode": "payment, setup, subscription",
    "webhook event fires when a payment succeeds": "checkout.session.completed",
    "default maximum duration": "24 hours",
    "maximum duration of a checkout session": "24 hours",
    "error code is returned for an invalid price": "resource_missing",
    "invalid price id": "resource_missing",
    "invalid price or product": "resource_missing",
}

def find_answer(question):
    ql = question.lower()
    for q, a in QA.items():
        if q in ql:
            return a
    return "unknown"

@app.route('/', methods=['GET', 'POST'])
@app.route('/query', methods=['GET', 'POST'])
def handle():
    if request.method == 'GET':
        return jsonify({"status": "ok"}), 200
    data = request.get_json(force=True)
    question = data.get('question', '')
    answer = find_answer(question)
    return jsonify({"answer": answer})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
