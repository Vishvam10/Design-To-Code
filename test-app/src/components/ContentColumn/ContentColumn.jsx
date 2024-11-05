import React from 'react';

import './index.css';

const ContentColumn = ({ title, linkText }) => (
  <div className="content-column" data-testid="content-column">
    <h2>{title}</h2>
    <div className="grid-container">
      <div className="grid-item" data-testid="grid-item"> <img src="placeholder.jpg" alt="" className="content-image" /> Description</div>
      <div className="grid-item" data-testid="grid-item"> <img src="placeholder.jpg" alt="" className="content-image" /> Description</div>
      <div className="grid-item" data-testid="grid-item"> <img src="placeholder.jpg" alt="" className="content-image" /> Description</div>
      <div className="grid-item" data-testid="grid-item"> <img src="placeholder.jpg" alt="" className="content-image" /> Description</div>
    </div>
    <a href="#" className="link" data-testid="link">{linkText}</a>
  </div>
);

export default ContentColumn;