from celery import shared_task
from .scanner.owasp_checker import OWASPComplianceChecker
from .scanner.cis_checker import CISComplianceChecker
from .scanner.risk_scoring import calculate_risk_score
from .models import Assessment, AssessmentResult

@shared_task
def run_compliance_scan(assessment_id, url, standard='OWASP'):
    if standard.upper() == 'OWASP':
        checker = OWASPComplianceChecker(url)
    elif standard.upper() == 'CIS':
        checker = CISComplianceChecker(url)
    else:
        raise ValueError(f"Unsupported compliance standard: {standard}")

    results = checker.run_checks()
    risk_score = calculate_risk_score(results)

    try:
        assessment = Assessment.objects.get(id=assessment_id)
        AssessmentResult.objects.create(
            assessment=assessment,
            standard=standard,
            result_data=results,
            risk_score=risk_score
        )
        print(f"AssessmentResult saved for Assessment ID {assessment_id} with {standard} standard")
    except Assessment.DoesNotExist:
        print(f"Assessment with ID {assessment_id} does not exist. Cannot save results.")

    return {
        "assessment_id": assessment_id,
        "target": url,
        "standard": standard,
        "results": results,
        "risk_score": risk_score
    }
