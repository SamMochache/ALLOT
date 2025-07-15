import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import LoginPage from './pages/LoginPage';
import Dashboard from './pages/Dashboard';
import HomePage from './pages/HomePage';
import ProtectedRoute from './components/ProtectedRoute';
import RegisterPage from './pages/RegisterPage';
import AssessmentResultsPage from './pages/AssessmentResultsPage';


function App() {
  return (
    <Router>
      <Routes>
        <Route path='/' element={<HomePage />} />
        <Route path='/login' element={<LoginPage />} />
        <Route path='/register' element={<RegisterPage />} />
        <Route
          path='/dashboard'
          element={
            <ProtectedRoute>
              <Dashboard />
            </ProtectedRoute>
          }
        />
        <Route
  path="/assessment-results/:assessmentId"
  element={
    <ProtectedRoute>
      <AssessmentResultsPage />
    </ProtectedRoute>
  }
/>
      </Routes>
      
    </Router>
  );
}
export default App;
