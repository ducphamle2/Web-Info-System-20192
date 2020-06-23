# 1. Import the PayPal SDK client that was created in `Set up Server-Side SDK`.
from paypalClient import PayPalClient
from paypalcheckoutsdk.orders import OrdersCreateRequest


class CreateOrder(PayPalClient):

    # 2. Set up your server to receive a call from the client
    """ This is the sample function to create an order. It uses the
      JSON body returned by buildRequestBody() to create an order."""

    def create_order(self, request_json, debug=False):
        request = OrdersCreateRequest()
        request.prefer('return=representation')
        # 3. Call PayPal to set up a transaction
        request.request_body(self.build_request_body(request_json))
        response = self.client.execute(request)
        if debug:
            print('Status Code: ', response.status_code)
            print('Status: ', response.result.status)
            print('Order ID: ', response.result.id)
            print('Intent: ', response.result.intent)
            for link in response.result.links:
                print('\t{}: {}\tCall Type: {}'.format(
                    link.rel, link.href, link.method))
            print('Total Amount: {} {}'.format(response.result.purchase_units[0].amount.currency_code,
                                               response.result.purchase_units[0].amount.value))

        return response

        """Setting up the JSON request body for creating the order. Set the intent in the
    request body to "CAPTURE" for capture intent flow."""
    @staticmethod
    def build_request_body(request_json):
        """Method to create body with CAPTURE intent"""
        item_name = request_json['item_name']
        full_name = request_json['full_name']
        address = request_json['address']
        quantity = request_json['quantity']
        item_total = 0.01 * int(quantity)
        tax_total = item_total
        total_price = item_total + tax_total + 0.02
        print("item name: ", item_name)
        return \
            {
                "intent": "CAPTURE",
                "application_context": {
                    "brand_name": "DUC PHAM LE LIQUOR STORE",
                    "landing_page": "BILLING",
                    "shipping_preference": "SET_PROVIDED_ADDRESS",
                    "user_action": "CONTINUE"
                },
                "purchase_units": [
                    {
                        "reference_id": "PUHF",
                        "description": "Sporting Goods",

                        "custom_id": "CUST-HighFashions",
                        "soft_descriptor": "HighFashions",
                        "amount": {
                            "currency_code": "USD",
                            "value": str(total_price),
                            "breakdown": {
                                "item_total": {
                                    "currency_code": "USD",
                                    "value": str(item_total)
                                },
                                "shipping": {
                                    "currency_code": "USD",
                                    "value": "0.01"
                                },
                                "handling": {
                                    "currency_code": "USD",
                                    "value": "0.01"
                                },
                                "tax_total": {
                                    "currency_code": "USD",
                                    "value": str(tax_total)
                                }
                            }
                        },
                        "items": [
                            {
                                "name": str(item_name),
                                "description": "Very yummy and cheap",
                                "sku": "sku01",
                                "unit_amount": {
                                    "currency_code": "USD",
                                    "value": "0.01"
                                },
                                "tax": {
                                    "currency_code": "USD",
                                    "value": "0.01"
                                },
                                "quantity": str(quantity),
                                "category": "PHYSICAL_GOODS"
                            }
                        ],
                        "shipping": {
                            "method": "United States Postal Service",
                            "address": {
                                "name": {
                                    "full_name": full_name,
                                    "surname": "Bean"
                                },
                                "address_line_1": address,
                                "address_line_2": "Floor 6",
                                "admin_area_2": "Hanoi",
                                "admin_area_1": "Hanoi",
                                "postal_code": "94107",
                                "country_code": "VN"
                            }
                        }
                    }
                ]
            }
