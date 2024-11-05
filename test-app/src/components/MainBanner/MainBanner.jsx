import React from 'react';

import './index.css';

const MainBanner = () => (
  <section className="main-banner" data-testid="main-banner">
    <img src="placeholder.jpg" alt="left banner" className="banner-image" />
    <div className="banner-text" data-testid="banner-text">
      Event Details
    </div>
    <img src="placeholder.jpg" alt="right banner" className="banner-image" />
  </section>
);

export default MainBanner;
