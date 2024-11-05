import React from 'react';

import './index.css';

const NavigationBar = () => (
  <nav className="navigation-bar" data-testid="navigation-bar">
    <div className="menu-item" data-testid="menu-item">
      All
    </div>
    <div className="menu-item" data-testid="menu-item">
      Medical Care
    </div>
    <div className="menu-item" data-testid="menu-item">
      Best Sellers
    </div>
    <div className="menu-item" data-testid="menu-item">
      ...
    </div>
  </nav>
);

export default NavigationBar;
