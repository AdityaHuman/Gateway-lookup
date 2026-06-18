# Gateway Lookup

CLI tool to detect payment gateways, Cloudflare, and CAPTCHA on any domain.

## Features

- Detects **20+ payment gateways** (Stripe, PayPal, Razorpay, Braintree, Square, Adyen, Paytm, Shopify, Klarna, Apple Pay, Google Pay, and more)
- Detects **Cloudflare** protection
- Detects **CAPTCHA / reCAPTCHA** challenges
- Outputs results in a rich formatted table
- Saves results as JSON files

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
python main.py lookup example.com
```

Save results to JSON:

```bash
python main.py lookup example.com --save
```

## License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

## Project Structure

```
gateway_lookup/
├── main.py       # CLI entry point (Typer)
├── scanner.py    # HTTP scanner + orchestration
├── detectors.py  # Signature-based detection logic
├── utils.py      # Display and save utilities
├── results/      # Saved JSON output
└── requirements.txt
```
