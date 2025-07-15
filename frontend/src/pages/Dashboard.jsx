import { useEffect, useState } from 'react';
import api from '../services/api';
import { useNavigate } from 'react-router-dom';

function Dashboard() {
  const [assessments, setAssessments] = useState([]);
  const navigate = useNavigate();

  useEffect(() => {
    fetchAssessments();
  }, []);

  const fetchAssessments = async () => {
    try {
      const response = await api.get('/assessments/');
      setAssessments(response.data.results);
    } catch (err) {
      console.error('Error fetching assessments:', err);
    }
  };

  const handleLogout = () => {
    localStorage.removeItem('access_token');
    localStorage.removeItem('refresh_token');
    window.location.href = '/';
  };

  const triggerScan = async (assessmentId, standard = 'OWASP') => {
    try {
      await api.post(`/assessments/trigger-scan/${assessmentId}/`, { standard });
      alert(`${standard} scan triggered successfully!`);
    } catch (err) {
      alert(`Failed to trigger ${standard} scan`);
    }
  };

  const viewResults = (assessmentId) => {
    navigate(`/assessment-results/${assessmentId}`);
  };

  const getRiskLabel = (score) => {
    if (score >= 0 && score <= 3) return { label: 'Low', color: 'bg-green-500' };
    if (score > 3 && score <= 6) return { label: 'Medium', color: 'bg-yellow-500' };
    return { label: 'High', color: 'bg-red-500' };
  };

  return (
    <div className="p-8 bg-gray-100 min-h-screen">
      <header className="flex justify-between items-center mb-8">
        <h1 className="text-3xl font-bold">Dashboard</h1>
        <button
          onClick={handleLogout}
          className="bg-red-500 text-white px-4 py-2 rounded hover:bg-red-600"
        >
          Logout
        </button>
      </header>

      <section className="mb-8">
        <h2 className="text-xl font-semibold mb-4">Welcome to your Security Dashboard</h2>
        <p>Here you can view:</p>
        <ul className="list-disc ml-6 mt-2">
          <li>Compliance status</li>
          <li>Vulnerabilities overview</li>
          <li>Threat intelligence insights</li>
          <li>Audit logs</li>
        </ul>
      </section>

      <section>
        <h2 className="text-xl font-semibold mb-4">Your Assessments</h2>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {assessments.map((assessment) => {
            const rawScore = Number(assessment.latest_risk_score);
            const score = isNaN(rawScore) ? null : rawScore;
            const risk = score !== null ? getRiskLabel(score) : null;

            return (
              <div key={assessment.id} className="glass p-4 rounded shadow backdrop-blur bg-white/10 text-black">
                <h3 className="font-bold text-lg">{assessment.target_system}</h3>
                <p>Compliance: {assessment.compliance_standard}</p>
                <p>Created: {new Date(assessment.created_at).toLocaleDateString()}</p>

                {risk && (
                  <p className="mt-2">
                    <strong>Risk Score:</strong>
                    <span className={`ml-2 px-2 py-1 rounded text-sm text-white ${risk.color}`}>
                      {score} ({risk.label})
                    </span>
                  </p>
                )}
                {assessment.latest_standard && (
  <p>
    <strong>Last Scan Standard:</strong> {assessment.latest_standard}
  </p>
)}


                <div className="mt-3 flex gap-2 flex-wrap">
                  <button
                    onClick={() => triggerScan(assessment.id, 'OWASP')}
                    className="bg-blue-500 text-white px-3 py-1 rounded hover:bg-blue-600"
                  >
                    Trigger OWASP Scan
                  </button>
                  <button
                    onClick={() => triggerScan(assessment.id, 'CIS')}
                    className="bg-purple-500 text-white px-3 py-1 rounded hover:bg-purple-600"
                  >
                    Trigger CIS Scan
                  </button>
                  <button
                    onClick={() => viewResults(assessment.id)}
                    className="bg-green-500 hover:bg-green-600 text-white px-3 py-1 rounded"
                  >
                    View Results
                  </button>
                </div>
              </div>
            );
          })}
        </div>
      </section>
    </div>
  );
}

export default Dashboard;
