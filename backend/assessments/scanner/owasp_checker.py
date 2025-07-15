import requests
from .base_checker import BaseComplianceChecker

class OWASPComplianceChecker(BaseComplianceChecker):
    name = "OWASP ASVS Compliance Checker"
    description = "Performs live compliance checks against OWASP ASVS"

    def __init__(self, target):
        super().__init__(target)

    def run_checks(self):
        results = []
        
        # Check 1: HTTPS Enforcement
        https_check = self.check_https_enforced()
        results.append(https_check)

        # Check 2: Security Headers
        headers_check = self.check_security_headers()
        results.append(headers_check)

        return results

    def check_https_enforced(self):
        if not self.target.startswith('https'):
            return {
                "check": "HTTPS Enforcement",
                "description": "Ensure the application enforces HTTPS connections.",
                "status": "FAIL",
                "severity": "High",
                "remediation": "Redirect HTTP traffic to HTTPS. Use HSTS headers.",
                "evidence": f"Target URL does not start with HTTPS: {self.target}"
            }
        return {
            "check": "HTTPS Enforcement",
            "description": "Ensure the application enforces HTTPS connections.",
            "status": "PASS",
            "severity": "High",
            "remediation": "Redirect HTTP traffic to HTTPS. Use HSTS headers.",
            "evidence": f"Target URL: {self.target}"
        }

    def check_security_headers(self):
        try:
            response = requests.get(self.target, timeout=5)
            security_headers = [
                'Strict-Transport-Security',
                'Content-Security-Policy',
                'X-Content-Type-Options',
                'X-Frame-Options',
                'Referrer-Policy'
            ]

            missing = [h for h in security_headers if h not in response.headers]

            if missing:
                return {
                    "check": "Security HTTP Headers",
                    "description": "Ensure recommended HTTP security headers are set.",
                    "status": "FAIL",
                    "severity": "Medium",
                    "remediation": "Implement headers: " + ", ".join(security_headers),
                    "evidence": f"Missing headers: {', '.join(missing)}"
                }
            else:
                return {
                    "check": "Security HTTP Headers",
                    "description": "Ensure recommended HTTP security headers are set.",
                    "status": "PASS",
                    "severity": "Medium",
                    "remediation": "Implement headers: " + ", ".join(security_headers),
                    "evidence": "All recommended headers are present."
                }

        except Exception as e:
            return {
                "check": "Security HTTP Headers",
                "description": "Ensure recommended HTTP security headers are set.",
                "status": "FAIL",
                "severity": "Medium",
                "remediation": "Ensure the target is reachable and headers are configured.",
                "evidence": f"Request failed: {str(e)}"
            }
