import React from 'react';
import MainBanner from './components/MainBanner/MainBanner';
import Header from './components/Header/Header';
import NavigationBar from './components/NavigationBar/NavigationBar';
import ContentSection from './components/ContentSection/ContentSection';

import './index.css';

const App = () => (
  <div className="app">
    <Header />
    <NavigationBar />
    <MainBanner />
    <ContentSection />
  </div>
);

export default App;