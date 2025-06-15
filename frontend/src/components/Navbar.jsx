// import { Link, useNavigate } from "react-router-dom";
// import useAuthStore from "../store/auth";

// export default function Navbar() {
//   const logout = useAuthStore((s) => s.logout);
//   const navigate = useNavigate();

//   const handleLogout = () => {
//     logout();
//     navigate("/");
//   };

//   return (
//     <nav className="flex items-center justify-between px-6 py-3 bg-gray-100 shadow">
//       <h1 className="font-bold text-xl">DocuMind</h1>
//       <div className="space-x-4">
//         <Link to="/upload" className="hover:underline">Upload</Link>
//         <Link to="/chat" className="hover:underline">Chat</Link>
//         <button onClick={handleLogout} className="text-red-600">Logout</button>
//       </div>
//     </nav>
//   );
// }


import { Link, useNavigate } from "react-router-dom";

export default function Navbar({ token, onLogout }) {
  const navigate = useNavigate();

  const handleLogoutClick = () => {
    onLogout();
    navigate("/");
  };

  return (
    // <nav className="flex justify-between items-center p-4 bg-gray-100 shadow">
    //   <div className="text-lg font-bold">
    //     <Link to="/">MyApp</Link>
    //   </div>
    //   <div className="space-x-4">
    //     {token ? (
    //       <>
    //         <Link to="/upload">Upload</Link>
    //         <Link to="/chat">Chat</Link>
    //         <button onClick={handleLogoutClick} className="text-red-500">Logout</button>
    //       </>
    //     ) : (
    //       <>
    //         <Link to="/">Login</Link>
    //         <Link to="/register">Register</Link>
    //       </>
    //     )}
    //   </div>
    // </nav>


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
