class CISComplianceChecker:
    def __init__(self, target_system):
        self.target_system = target_system
        self.checks = [
            {
                "check": "Disable Root SSH Login",
                "description": "Verify that SSH root login is disabled.",
                "severity": "High",
                "remediation": "Edit /etc/ssh/sshd_config to set PermitRootLogin to no.",
            },
            {
                "check": "Ensure UFW is Enabled",
                "description": "Check that Uncomplicated Firewall (UFW) is active.",
                "severity": "Medium",
                "remediation": "Enable UFW using: sudo ufw enable.",
            },
            {
                "check": "Password Complexity Policy",
                "description": "Ensure password policies enforce complexity.",
                "severity": "High",
                "remediation": "Configure /etc/login.defs or use PAM modules.",
            }
        ]

    def run_checks(self):
        results = []
        for check in self.checks:
            # Simulate checking logic (In production, SSH to server and validate)
            status = "PASS" if "example.com" not in self.target_system else "FAIL"
            evidence = f"Checked on {self.target_system}"

            results.append({
                "check": check["check"],
                "description": check["description"],
                "status": status,
                "severity": check["severity"],
                "remediation": check["remediation"],
                "evidence": evidence
            })
        return results
