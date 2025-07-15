from abc import ABC, abstractmethod

class BaseComplianceChecker(ABC):
    name = "Base Compliance Checker"
    description = "Base template for compliance checkers"

    def __init__(self, target):
        """
        Initialize with a target e.g., domain, IP, or system.
        """
        self.target = target

    @abstractmethod
    def run_checks(self):
        """
        Runs all compliance checks.
        Returns:
            List of dictionaries with:
            - check
            - description
            - status: PASS/FAIL
            - severity: Low/Medium/High/Critical
            - remediation
            - evidence
        """
        pass
