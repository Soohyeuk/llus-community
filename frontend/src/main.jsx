import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";  // Import the root component
import { BrowserRouter } from "react-router-dom";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
    <BrowserRouter>  {/* Enables routing in App */}
        <App />  {/* Renders the App component */}
    </BrowserRouter>
);
