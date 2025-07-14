import { useState } from 'react';
import api from '../services/api';
import { useNavigate } from 'react-router-dom';

function RegisterPage() {
  const [formData, setFormData] = useState({ username: '', email: '', password: '' });
  const navigate = useNavigate();

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleRegister = async (e) => {
    e.preventDefault();
    try {
      await api.post('users/register/', formData);  // We'll configure this API
      alert('Registration successful! Please log in.');
      navigate('/login');
    } catch (err) {
      alert('Registration failed. Try again.');
    }
  };

  return (
    <div className="min-h-screen bg-cover bg-center flex items-center justify-center"
         style={{ backgroundImage: "url('/mount.jpg')" }}>
      <form onSubmit={handleRegister} className="glass p-8 w-96 text-white">
        <h2 className="text-3xl font-bold mb-6 text-center">Register</h2>
        
        <input
          type="text"
          name="username"
          placeholder="Username"
          className="bg-white/10 border border-white/20 text-white placeholder-gray-300 p-2 w-full mb-4 rounded"
          onChange={handleChange}
          required
        />
        <input
          type="email"
          name="email"
          placeholder="Email"
          className="bg-white/10 border border-white/20 text-white placeholder-gray-300 p-2 w-full mb-4 rounded"
          onChange={handleChange}
          required
        />
        <input
          type="password"
          name="password"
          placeholder="Password"
          className="bg-white/10 border border-white/20 text-white placeholder-gray-300 p-2 w-full mb-4 rounded"
          onChange={handleChange}
          required
        />

        <button type="submit" className="bg-blue-500 text-white w-full py-2 rounded hover:bg-blue-600">
          Register
        </button>

        <p className="text-center text-gray-300 mt-4">
          Already have an account? <a href="/login" className="underline text-white">Login</a>
        </p>
      </form>
    </div>
  );
}

export default RegisterPage;
