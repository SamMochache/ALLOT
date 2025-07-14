function HomePage() {
  return (
    <section
      className="min-h-screen bg-cover bg-center flex items-center justify-center relative"
      style={{ backgroundImage: "url('/laake.jpg')" }}
    >
      <div className="absolute inset-0 bg-black bg-opacity-0" />

      <div className="glass p-8 max-w-xl text-center text-white z-10">
        <h1 className="text-4xl font-bold mb-3">
          Cybersecurity Compliance & Risk Management
        </h1>
        <p className="mb-5 text-gray-200">
          Secure infrastructure, manage risks, and stay compliant — all in one platform.
        </p>
        <a
          href="/login"
          className="bg-gradient-to-r from-purple-500 to-blue-500 hover:from-blue-600 hover:to-purple-600 px-5 py-2 rounded-full font-medium shadow-md transition-transform hover:scale-105"
        >
          Get Started
        </a>
      </div>
    </section>
  );
}

export default HomePage;
