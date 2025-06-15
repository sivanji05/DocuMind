// import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
// import { useState } from "react";
// import Login from "./pages/Login";
// import Register from "./pages/Register";
// import Upload from "./pages/Upload";
// import Chat from "./pages/Chat";
// import ProtectedRoute from "./components/ProtectedRoute";
// import Navbar from "./components/Navbar";

// function App() {

//     const [token, setToken] = useState(localStorage.getItem('token'))
//   const [use,setuser_id] = useState(localStorage.getItem('id'))

 

//   const handleLogin=(token, user_id)=>{
//     localStorage.setItem('token',token)
//     localStorage.setItem('user_id',user_id)

//     setToken(token)
//     setuser_id(user_id)
//   }
//   return (
//     <Router>
//       <Navbar />
//       <Routes>
//         <Route path="/" element={<Login />} />
//         <Route path="/register" element={<Register />} />
//         <Route path="/upload" element={<ProtectedRoute><Upload /></ProtectedRoute>} />
//         <Route path="/chat" element={<ProtectedRoute><Chat /></ProtectedRoute>} />
//       </Routes>
//     </Router>
//   );
// }

// export default App;



import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { useState } from "react";
import Login from "./pages/Login";
import Register from "./pages/Register";
import Upload from "./pages/Upload";
import Chat from "./pages/Chat";
import ProtectedRoute from "./components/ProtectedRoute";
import Navbar from "./components/Navbar";
import './index.css';


function App() {
  const [token, setToken] = useState(localStorage.getItem('token'));

  const handleLogin = (token) => {
    localStorage.setItem('token', token);
    setToken(token);
  };



  return (
    <Router>
      <Navbar token={token} onLogout={() => {
        localStorage.removeItem('token');
        setToken(null);
      }} />
      <Routes>
        <Route path="/" element={<Login onLogin={handleLogin} />} />
        <Route path="/register" element={<Register />} />
        <Route path="/upload" element={<ProtectedRoute token={token}><Upload /></ProtectedRoute>} />
        <Route path="/chat" element={<ProtectedRoute token={token}><Chat /></ProtectedRoute>} />
      </Routes>
     
    </Router>
    
  );
  
}

export default App;
