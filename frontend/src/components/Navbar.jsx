import { Link, useNavigate } from "react-router-dom";

export default function Navbar({ token, onLogout }) {
  const navigate = useNavigate();

  const handleLogoutClick = () => {
    onLogout();
    navigate("/");
  };

  return (
    <nav className="bg-white shadow-md px-6 py-4 flex justify-between items-center">
      <div className="text-2xl font-bold text-indigo-600">
        <Link to="/">DocuMind</Link>
      </div>
      <div className="space-x-4 flex items-center text-gray-700">
        {token ? (
          <>
            <Link
              to="/upload"
              className="hover:text-indigo-600 transition font-medium"
            >
              Upload
            </Link>
            <Link to="/chat" className="hover:text-indigo-600 transition font-medium"> Chat</Link>
            <button
              onClick={handleLogoutClick}
              className="text-red-600 hover:text-red-700 transition font-medium"
            >
              Logout
            </button>
          </>
        ) : (
          <>
            <Link
              to="/"
              className="hover:text-indigo-600 transition font-medium"
            >
              Login
            </Link>
            <Link
              to="/register"
              className="hover:text-indigo-600 transition font-medium"
            >
              Register
            </Link>
          </>
        )}
      </div>
    </nav>
  );
}
