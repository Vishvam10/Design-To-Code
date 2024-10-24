import React from 'react';

function App() {
  return (
    <div>
      <h1>Design & Build Your Own Landing Pages</h1>
      <p className="subheading">Transform your marketing with our powerful landing page builder.</p>

      <div className="left-column">
        <h2>Special Features:</h2>
        <ul>
          <li className="feature-card">
            <i className="icon icon-1" />
            <h3>Title Goes Here</h3>
            <p>This is the body text for feature 1.</p>
          </li>
          <li className="feature-card">
            <i className="icon icon-2" />
            <h3>Title Goes Here</h3>
            <p>This is the body text for feature 2.</p>
          </li>
          <li className="feature-card">
            <i className="icon icon-3" />
            <h3>Title Goes Here</h3>
            <p>This is the body text for feature 3.</p>
          </li>
          <li className="feature-card">
            <i className="icon icon-4" />
            <h3>Title Goes Here</h3>
            <p>This is the body text for feature 4.</p>
          </li>
        </ul>
      </div>

      <div className="right-column">
        <img src="smartphone-image.jpg" alt="Smartphone Image" />
      </div>
    </div>
  );
}

export default App;