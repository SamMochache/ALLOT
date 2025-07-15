def calculate_risk_score(results):
    """
    Calculates a risk score based on the severity of failed checks.

    Args:
        results (list): List of dicts each representing a compliance check result.

    Returns:
        int: Total risk score.
    """
    severity_points = {
        "Critical": 5,
        "High": 4,
        "Medium": 3,
        "Low": 1
    }

    total_score = 0

    for result in results:
        if result['status'] == 'FAIL':
            severity = result.get('severity', 'Low')
            total_score += severity_points.get(severity, 1)

    return total_score
