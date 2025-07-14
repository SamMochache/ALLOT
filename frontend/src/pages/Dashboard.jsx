function Dashboard() {
  const handleLogout = () => {
    localStorage.removeItem('access_token');
    localStorage.removeItem('refresh_token');
    window.location.href = '/';
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

      <div>
        <p className="mb-4">Welcome to the system dashboard. Here you'll see:</p>
        <ul className="list-disc ml-6">
          <li>Compliance status</li>
          <li>Vulnerabilities overview</li>
          <li>Threat intelligence insights</li>
          <li>Audit logs</li>
        </ul>
      </div>
    </div>
  );
}

export default Dashboard;
