import { useState } from "react";
import api from "../services/api";
import { useNavigate } from "react-router-dom";

export default function Login({ onLogin }) {
  const [form, setForm] = useState({ username: "", password: "" });
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await api.post("http://127.0.0.1:8000/api/auth/login", new URLSearchParams(form));
      const { access_token } = res.data;

      onLogin(access_token);  
      navigate("/upload");
    } catch (err) {
      console.error("Login failed", err);
      alert("Invalid username or password.");
    }
  };

  return (

  <form onSubmit={handleSubmit} className="max-w-sm mx-auto mt-12 p-6 bg-white rounded-2xl shadow space-y-6">
  <h2 className="text-2xl font-bold text-center text-gray-800">Login</h2>
  
  <input
    type="text"
    name="username"
    placeholder="Username"
    required
    className="w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
    onChange={(e) => setForm({ ...form, username: e.target.value })}
  />
  
  <input
    type="password"
    name="password"
    placeholder="Password"
    required
    className="w-full p-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
    onChange={(e) => setForm({ ...form, password: e.target.value })}
  />
  
  <button type="submit" className="w-full bg-blue-600 text-white p-3 rounded-lg hover:bg-blue-700 transition">
    Sign In
  </button>
</form>

   );
}



