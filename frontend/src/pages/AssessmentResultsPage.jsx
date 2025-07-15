import { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import api from '../services/api';

function AssessmentResultsPage() {
  const { assessmentId } = useParams();
  const [results, setResults] = useState([]);
  const [nextPage, setNextPage] = useState(null);
  const [prevPage, setPrevPage] = useState(null);

  useEffect(() => {
    fetchResults();
  }, []);

  const fetchResults = async (url = `/assessments/assessment-results/?assessment=${assessmentId}`) => {
    try {
      const response = await api.get(url);
      setResults(response.data.results);
      setNextPage(response.data.next);
      setPrevPage(response.data.previous);
    } catch (err) {
      console.error('Failed to fetch results', err);
    }
  };

  // Utility to clean API URLs for frontend fetch
  const formatApiUrl = (fullUrl) => {
    return fullUrl?.replace(/^https?:\/\/[^/]+\/api/, '');
  };

  return (
    <div className="min-h-screen bg-gradient-to-r from-gray-800 via-gray-900 to-black text-white p-8">
      <h1 className="text-3xl font-bold mb-6 text-center">Assessment Results</h1>
      <p className="text-center text-gray-300 mb-12">
        Viewing results for Assessment ID: <span className="font-bold">{assessmentId}</span>
      </p>

      {results.length === 0 ? (
        <p className="text-center text-gray-400">No results yet. Please run a scan first.</p>
      ) : (
        results.map((result) => (
          <div key={result.id} className="glass p-6 mb-8 rounded-lg shadow-lg">
            <div className="flex justify-between items-center mb-4">
              <div>
                <p><strong>Risk Score:</strong> <span className="text-yellow-400">{result.risk_score}</span></p>
                <p><strong>Completed:</strong> {new Date(result.completed_at).toLocaleString()}</p>
              </div>
            </div>

            <h3 className="text-xl font-semibold border-b border-gray-600 pb-2 mb-3">Compliance Checks</h3>
            <ul className="space-y-4">
              {result.result_data.map((check, index) => (
                <li key={index} className="bg-gray-700 p-4 rounded shadow text-gray-200">
                  <p className="text-lg font-bold">{check.check}</p>
                  <p>Status: 
                    <span className={`ml-2 font-semibold ${check.status === 'PASS' ? 'text-green-400' : 'text-red-400'}`}>
                      {check.status}
                    </span>
                  </p>
                  <p>Severity: <span className="text-pink-400">{check.severity}</span></p>
                  <p className="text-sm mt-2"><em>Remediation:</em> {check.remediation}</p>
                </li>
              ))}
            </ul>
          </div>
        ))
      )}

      {results.length > 0 && (
        <div className="flex justify-center gap-4 mt-8">
          {prevPage && (
            <button
              onClick={() => fetchResults(formatApiUrl(prevPage))}
              className="bg-gray-700 text-white px-4 py-2 rounded hover:bg-gray-600"
            >
              Previous
            </button>
          )}
          {nextPage && (
            <button
              onClick={() => fetchResults(formatApiUrl(nextPage))}
              className="bg-gray-700 text-white px-4 py-2 rounded hover:bg-gray-600"
            >
              Next
            </button>
          )}
        </div>
      )}
    </div>
  );
}

export default AssessmentResultsPage;
