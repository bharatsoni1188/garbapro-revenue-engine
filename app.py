import razorpay
import hmac
import hashlib

client = razorpay.Client(auth=("YOUR_RAZORPAY_KEY_ID", "YOUR_RAZORPAY_KEY_SECRET"))

def verify_payment_signature(order_id, payment_id, signature):
    try:
        # Construct verification parameters dictionary
        params_dict = {
            'razorpay_order_id': order_id,
            'razorpay_payment_id': payment_id,
            'razorpay_signature': signature
        }
        # Built-in utility to verify cryptographic signature validity
        client.utility.verify_payment_signature(params_dict)
        return True
    except razorpay.errors.SignatureVerificationError:
        return False
