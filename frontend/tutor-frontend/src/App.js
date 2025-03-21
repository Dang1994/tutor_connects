import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import TutorRegistration from './components/TutorRegistration'; // Import TutorRegistration component
import About from './components/About';
import Feedback from './components/Feedback';
import Chatbot from './components/Chatbot'; // Import the Chatbot component
import './App.css';
import logo from './logo.png'; // Import the logo image

function App() {
  const [showRegister, setShowRegister] = useState(false);
  const [menuOpen, setMenuOpen] = useState(false); // State to handle the hamburger menu

  const toggleRegisterForm = () => {
    setShowRegister(!showRegister);
  };

  const toggleMenu = () => {
    setMenuOpen(!menuOpen); // Toggle the hamburger menu
  };

  return (
    <Router>
      <div className="App">
        <header className="App-header">
          <div className="App-logo">
            <img src={logo} alt="Tutor Finder" /> {/* Use the imported logo */}
            <h1>Tutor Finder</h1>
          </div>
          
          <div className="hamburger-menu" onClick={toggleMenu}>
            {/* Three dots or hamburger icon */}
            <span className="hamburger-icon">☰</span>
          </div>
          
          {menuOpen && (
            <nav className="App-nav">
              <ul>
                <li>
                  <Link to="/" onClick={toggleMenu}>Home</Link>
                </li>
                <li>
                  <Link to="/about" onClick={toggleMenu}>About</Link>
                </li>
                <li>
                  <a href="https://yourcompanywebsite.com" target="_blank" rel="noopener noreferrer" onClick={toggleMenu}>
                    More Products
                  </a>
                </li>
                <li>
                  <button className="register-button" onClick={() => { toggleRegisterForm(); toggleMenu(); }}>
                    {showRegister ? 'Close Registration' : 'Register as Tutor'}
                  </button>
                </li>
                <li>
                  <Link to="/feedback" onClick={toggleMenu}>Feedback</Link>
                </li>
                <li>
                  <a href="mailto:contact@yourwebsite.com" onClick={toggleMenu}>Contact</a>
                </li>
              </ul>
            </nav>
          )}
        </header>

        <main className="App-content">
          <Routes>
            <Route
              path="/"
              element={
                !showRegister ? (
                  <section className="App-section">
                    <h2>Welcome to Tutor Finder</h2>
                    <p>Click here and find your tutor with Salu</p>
                  </section>
                ) : (
                  <section className="App-section">
                    <TutorRegistration />
                  </section>
                )
              }
            />
            <Route path="/about" element={<About />} />
            <Route path="/feedback" element={<Feedback />} />
          </Routes>
        </main>

        <Chatbot /> {/* Add the Chatbot component here for interaction */}

        <footer className="App-footer">
          <p>© 2024 SG Tutor. All Rights Reserved.</p>
        </footer>
      </div>
    </Router>
  );
}

export default App;
