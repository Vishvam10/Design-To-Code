import React from 'react';
import { render, screen } from '@testing-library/react';
import '@testing-library/jest-dom';
import MainBanner from './MainBanner';

describe('MainBanner Component', () => {
  beforeEach(() => {
    render(<MainBanner />);
  });

  test('should render main banner section with correct styles', () => {
    const mainBanner = screen.getByTestId('main-banner');
    expect(mainBanner).toHaveStyle(`
      display: flex;
      justify-content: space-between;
      align-items: center;
      background-color: blue;
      color: white;
      padding: 20px;
    `);
  });

  test('should render left and right banner images with correct alt text and styles', () => {
    const bannerImages = screen.getAllByAltText(/banner/i);
    expect(bannerImages.length).toBe(2);
    bannerImages.forEach((image) => {
      expect(image).toHaveStyle(`
        width: 100px;
        height: 100px;
      `);
    });
  });

  test('should render centered text with correct style', () => {
    const bannerText = screen.getByTestId('banner-text');
    expect(bannerText).toHaveTextContent('Event Details');
    expect(bannerText).toHaveStyle(`
      flex: 1;
      text-align: center;
      font-size: 24px;
    `);
  });
});