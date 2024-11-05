import React from 'react';
import { render, screen, describe } from '@testing-library/react';
import App from './App';
import Header from './components/Header/Header';
import NavigationBar from './components/NavigationBar/NavigationBar';
import MainBanner from './components/MainBanner/MainBanner';
import ContentSection from './components/ContentSection/ContentSection';

describe('App Component', () => {
  test('renders the App component', () => {
    render(<App />);
    expect(screen.getByTestId('app')).toBeInTheDocument();
  });

  test('renders the Header component', () => {
    render(<Header />);
    expect(screen.getByTestId('header')).toBeInTheDocument();
    expect(screen.getByTestId('logo')).toBeInTheDocument();
    expect(screen.getByTestId('delivery-info')).toBeInTheDocument();
    expect(screen.getByTestId('search-bar')).toBeInTheDocument();
    expect(screen.getByTestId('language-selection')).toBeInTheDocument();
    expect(screen.getByTestId('account-details')).toBeInTheDocument();
    expect(screen.getByTestId('orders')).toBeInTheDocument();
    expect(screen.getByTestId('cart')).toBeInTheDocument();
  });

  test('checks Header layout structure', () => {
    render(<Header />);
    const header = screen.getByTestId('header');
    expect(header).toHaveStyle('display: flex');
    expect(header).toHaveStyle('justify-content: space-between');
  });

  test('renders the NavigationBar component', () => {
    render(<NavigationBar />);
    expect(screen.getByTestId('navigation-bar')).toBeInTheDocument();
  });

  test('checks NavigationBar layout structure', () => {
    render(<NavigationBar />);
    const navBar = screen.getByTestId('navigation-bar');
    expect(navBar).toHaveStyle('display: flex');
  });

  test('renders the MainBanner component', () => {
    render(<MainBanner />);
    expect(screen.getByTestId('main-banner')).toBeInTheDocument();
    expect(screen.getByTestId('banner-text')).toBeInTheDocument();
  });

  test('checks MainBanner layout and styles', () => {
    render(<MainBanner />);
    const banner = screen.getByTestId('main-banner');
    expect(banner).toHaveStyle('display: flex');
    expect(banner).toHaveStyle('justify-content: center');
    expect(banner).toHaveStyle('background-color: blue');
    const bannerText = screen.getByTestId('banner-text');
    expect(bannerText).toHaveStyle('color: white');
  });

  test('renders the ContentSection component', () => {
    render(<ContentSection />);
    expect(screen.getByTestId('content-section')).toBeInTheDocument();
  });

  test('checks ContentSection layout structure', () => {
    render(<ContentSection />);
    const contentSection = screen.getByTestId('content-section');
    expect(contentSection).toHaveStyle('display: grid');
    expect(contentSection).toHaveStyle('grid-template-columns: repeat(4, 1fr)');
  });

  test('checks typography and colors', () => {
    render(<App />);
    expect(screen.getByTestId('app')).toHaveStyle(
      'font-family: "Amazon Ember", Arial, sans-serif'
    );
    expect(screen.getByTestId('app')).toHaveStyle('color: black');
  });

  test('checks accessibility features', () => {
    render(<App />);
    const images = screen.getAllByRole('img');
    images.forEach((img) => {
      expect(img).toHaveAttribute('alt');
    });
  });
});
