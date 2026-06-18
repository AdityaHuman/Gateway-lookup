from typing import List

PAYMENT_GATEWAYS = {
    "Stripe": ["stripe"],
    "PayPal": ["paypal"],
    "Braintree": ["braintree"],
    "Razorpay": ["razorpay"],
    "Square": ["square"],
    "Adyen": ["adyen"],
    "Authorize.Net": ["authorize.net"],
    "Checkout.com": ["checkout.com"],
    "Paytm": ["paytm"],
    "Shopify": ["shopify"],
    "WooCommerce": ["woocommerce"],
    "PayU": ["payu"],
    "Klarna": ["klarna"],
    "Apple Pay": ["apple-pay", "apple.com"],
    "Google Pay": ["google pay", "pay.google.com"],
}

def detect_gateways(html: str) -> List[str]:
    html = html.lower()
    found = []
    for gateway, signatures in PAYMENT_GATEWAYS.items():
        if any(sig in html for sig in signatures):
            found.append(gateway)
    return found or ["Unknown"]

def detect_cloudflare(html: str) -> bool:
    return any(sig in html.lower() for sig in [
        "cloudflare",
        "challenges.cloudflare.com",
        "cdnjs.cloudflare.com",
    ])

def detect_captcha(html: str) -> bool:
    return any(sig in html.lower() for sig in [
        "recaptcha",
        "captcha",
        "i'm not a robot",
        "recaptcha/api.js",
    ])
