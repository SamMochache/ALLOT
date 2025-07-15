import logging
from celery import shared_task
from .scanner.owasp_checker import OWASPComplianceChecker
from .scanner.cis_checker import CISComplianceChecker
from .scanner.risk_scoring import calculate_risk_score
from .models import Assessment, AssessmentResult

# Setup logger for this module
logger = logging.getLogger(__name__)

@shared_task
def run_compliance_scan(assessment_id, url, standard='OWASP'):
    logger.info(f"Starting compliance scan for Assessment ID {assessment_id} with standard {standard}")

    try:
        if standard.upper() == 'OWASP':
            checker = OWASPComplianceChecker(url)
        elif standard.upper() == 'CIS':
            checker = CISComplianceChecker(url)
        else:
            raise ValueError(f"Unsupported compliance standard: {standard}")

        results = checker.run_checks()
        risk_score = calculate_risk_score(results)
        logger.info(f"Risk score calculated for Assessment ID {assessment_id}: {risk_score}")

        assessment = Assessment.objects.get(id=assessment_id)
        AssessmentResult.objects.create(
            assessment=assessment,
            standard=standard,
            result_data=results,
            risk_score=risk_score
        )
        logger.info(f"AssessmentResult saved for Assessment ID {assessment_id} with {standard} standard")

        return {
            "assessment_id": assessment_id,
            "target": url,
            "standard": standard,
            "results": results,
            "risk_score": risk_score
        }

    except Assessment.DoesNotExist:
        error_msg = f"Assessment with ID {assessment_id} does not exist. Cannot save results."
        logger.error(error_msg)
        return {'error': error_msg}

    except Exception as e:
        logger.error(f"Compliance scan failed for Assessment ID {assessment_id}: {str(e)}", exc_info=True)
        return {'error': str(e)}
