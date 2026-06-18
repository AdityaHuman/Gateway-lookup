import time
import httpx
from detectors import detect_gateways, detect_cloudflare, detect_captcha

def normalize_url(domain: str) -> str:
    if domain.startswith(("http://", "https://")):
        return domain
    return f"https://{domain}"

def scan_website(domain: str):
    start = time.perf_counter()
    try:
        with httpx.Client(timeout=15, follow_redirects=True) as client:
            response = client.get(normalize_url(domain))
            html = response.text
        return {
            "success": True,
            "domain": domain,
            "url": str(response.url),
            "status_code": response.status_code,
            "gateways": detect_gateways(html),
            "cloudflare": detect_cloudflare(html),
            "captcha": detect_captcha(html),
            "time_taken": round(time.perf_counter() - start, 2),
        }
    except Exception as e:
        return {"success": False, "error": str(e)}
