import { useState, useEffect } from 'react'
import './App.css'
import axios from 'axios'; 

function App() {
  useEffect(() => {
    const fetchItems = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/profile/1');
        console.log(response.data);
      } catch (error) {
        console.log("shiet")
      }
    };

    fetchItems();
  }, []);

  return (
    <>
    </>
  )
}

export default App
