from flask import (Flask, request, session, g, redirect,
                   url_for, abort, render_template, flash, Response)
from flask_cors import CORS
from order.createOrder import CreateOrder
from order.getOrder import GetOrder
from order.captureOrder import CaptureOrder
from flask import jsonify, make_response

app = Flask(__name__)

# USE CORS SO THE BROWSER CAN CALL TO THE SERVER
CORS(app)


@app.route("/create_order", methods=["POST"])
def createOrder():
    try:
        print("AAAAAAAAAAAAAAA")
        request_json = request.get_json()
        print("request json: ", request_json)
        result = CreateOrder().create_order(request_json, debug=True)
        res = {
            "statusCode": result.status_code,
            "status": result.result.status,
            "orderID": result.result.id,
            "intent": result.result.intent,
            "totalAmount": result.result.purchase_units[0].amount.value + " " + result.result.purchase_units[0].amount.currency_code
        }
        print("response: ", res)
        return jsonify(res)
    except Exception as e:
        print("\nStopping...")
        print("error: ", e)
        return jsonify({"error": "some error"})


@app.route("/get_order/<order_id>", methods=["GET"])
def getOrder(order_id):
    try:
        print("order id: ", order_id)
        result = GetOrder().get_order(order_id)
        res = {
            "statusCode": result.status_code,
            "status": result.result.status,
            "orderID": result.result.id,
            "intent": result.result.intent,
            "totalAmount": result.result.purchase_units[0].amount.value + " " + result.result.purchase_units[0].amount.currency_code
        }
        print("response: ", res)
        return jsonify(res)
    except KeyboardInterrupt:
        print("\nStopping...")
        return jsonify({"error": "some error"})
    except Exception as e:
        print("\nStopping...")
        print("error: ", e)
        return jsonify({"error": "some error"})


@app.route("/capture_order/<order_id>", methods=["GET"])
def captureOrder(order_id):
    try:
        print("order id: ", order_id)
        result = CaptureOrder().capture_order(order_id)
        res = {
            "statusCode": result.status_code,
            "status": result.result.status,
            "orderID": result.result.id,
            "buyer_name": result.result.payer.name.given_name,
            "buyer_email": result.result.payer.email_address
        }
        print("response: ", res)
        return jsonify(res)
    except KeyboardInterrupt:
        print("\nStopping...")
        return jsonify({"error": "some error"})
    except Exception as e:
        print("\nStopping...")
        return jsonify({"error": "some error"})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8088)
