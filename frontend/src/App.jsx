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
