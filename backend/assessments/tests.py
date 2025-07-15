from django.test import TestCase
from users.models import User
from assessments.models import Assessment, AssessmentResult
from assessments.tasks import run_compliance_scan
from assessments.scanner.owasp_checker import OWASPComplianceChecker
from assessments.scanner.cis_checker import CISComplianceChecker
from assessments.scanner.risk_scoring import calculate_risk_score

class OWASPComplianceCheckerTest(TestCase):
    def test_https_enforcement_check(self):
        checker = OWASPComplianceChecker('https://example.com')
        results = checker.run_checks()

        self.assertIsInstance(results, list)
        self.assertGreater(len(results), 0)

        for check in results:
            self.assertIn('check', check)
            self.assertIn('status', check)
            self.assertIn('severity', check)
            self.assertIn('remediation', check)

class CISComplianceCheckerTest(TestCase):
    def test_cis_checks(self):
        checker = CISComplianceChecker('https://example.com')
        results = checker.run_checks()

        self.assertIsInstance(results, list)
        self.assertGreater(len(results), 0)

        for check in results:
            self.assertIn('check', check)
            self.assertIn('status', check)
            self.assertIn('severity', check)
            self.assertIn('remediation', check)

class RiskScoringTest(TestCase):
    def test_risk_score_calculation(self):
        sample_results = [
            {'status': 'PASS', 'severity': 'High'},
            {'status': 'FAIL', 'severity': 'Medium'},
            {'status': 'FAIL', 'severity': 'Low'},
        ]
        score = calculate_risk_score(sample_results)
        self.assertEqual(score, 4)  # Medium=2, Low=1

class AssessmentFlowTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.assessment = Assessment.objects.create(
            user=self.user,
            target_system='https://example.com',
            compliance_standard='OWASP'
        )

    def test_create_assessment(self):
        self.assertEqual(Assessment.objects.count(), 1)
        self.assertEqual(self.assessment.target_system, 'https://example.com')

    def test_run_owasp_compliance_scan_task(self):
        result = run_compliance_scan(self.assessment.id, self.assessment.target_system, 'OWASP')

        self.assertIn('risk_score', result)
        self.assertEqual(result['standard'], 'OWASP')
        self.assertTrue(AssessmentResult.objects.filter(assessment=self.assessment).exists())

    def test_run_cis_compliance_scan_task(self):
        result = run_compliance_scan(self.assessment.id, self.assessment.target_system, 'CIS')

        self.assertIn('risk_score', result)
        self.assertEqual(result['standard'], 'CIS')
        self.assertTrue(AssessmentResult.objects.filter(assessment=self.assessment).exists())



from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from users.models import User
from assessments.models import Assessment

class AssessmentAPITests(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='apitestuser', password='testpass')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        self.assessment = Assessment.objects.create(
            user=self.user,
            target_system='https://example.com',
            compliance_standard='OWASP'
        )

    def test_assessment_list_api(self):
        response = self.client.get('/api/assessments/')
        self.assertEqual(response.status_code, 200)
        self.assertGreaterEqual(len(response.data), 1)

    def test_trigger_scan_api(self):
        response = self.client.post(f'/api/assessments/trigger-scan/{self.assessment.id}/')
        self.assertEqual(response.status_code, 202)
        self.assertIn('message', response.data)

    def test_assessment_results_api(self):
        response = self.client.get(f'/api/assessments/assessment-results/?assessment={self.assessment.id}')
        self.assertEqual(response.status_code, 200)
