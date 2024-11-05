import React from 'react';

import './index.css';

const Header = () => (
  <header className="header" data-testid="header">
    <div className="logo" data-testid="logo">Logo</div>
    <div className="delivery-info" data-testid="delivery-info">Delivery to 12345</div>
    <input type="text" className="search-bar" placeholder="Search..." data-testid="search-bar" />
    <div className="right-section" data-testid="right-section">
      <div className="language" data-testid="language">EN</div>
      <div className="account" data-testid="account">Account</div>
      <div className="orders" data-testid="orders">Orders</div>
      <div className="cart" data-testid="cart">Cart</div>
    </div>
  </header>
);

export default Header;