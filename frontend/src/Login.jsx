import React, { useState } from "react";
import axios from "axios";

const Login = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post("http://localhost:8000/api/token/", {
        username,
        password,
      });

      if (response.status === 200) {
        console.log("Login successful!");
        console.log(" Token:", response.data.token); // Logs the JWT token
        localStorage.setItem("authToken", response.data.token); // Store token
      } else {
        console.log("Login failed: Unexpected response.");
      }
    } catch (error) {
      console.error(" Login failed:", error.response ? error.response.data : error.message);
    }
  };

  return (
    <form onSubmit={handleLogin}>
      <label htmlFor="username">Username:</label>
      <input type="text" id="username" value={username} onChange={(e) => setUsername(e.target.value)} required />

      <label htmlFor="password">Password:</label>
      <input type="password" id="password" value={password} onChange={(e) => setPassword(e.target.value)} required />

      <button type="submit">Login</button>
    </form>
  );
};

export default Login;
