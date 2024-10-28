import React from 'react';
import { render } from '@testing-library/react';
// import '@testing-library/jest-dom/extend-expect';

describe('Amazon Webpage Layout and Components', () => {
  
  test('Header layout is correct', () => {
    const { getByTestId } = render(<Header />);
    const header = getByTestId('header');
    
    expect(header).toHaveStyle('display: flex');
    expect(getByTestId('logo')).toBeInTheDocument();
    expect(getByTestId('delivery-info')).toBeInTheDocument();
    expect(getByTestId('search-bar')).toBeInTheDocument();
    expect(getByTestId('language-selection')).toBeInTheDocument();
    expect(getByTestId('account-details')).toBeInTheDocument();
    expect(getByTestId('orders')).toBeInTheDocument();
    expect(getByTestId('cart')).toBeInTheDocument();
  });

  test('Navigation bar layout is correct', () => {
    const { getByTestId } = render(<NavigationBar />);
    const navBar = getByTestId('nav-bar');
    
    expect(navBar).toHaveStyle('display: flex');
    expect(getByTestId('menu-item-all')).toBeInTheDocument();
    expect(getByTestId('menu-item-medical')).toBeInTheDocument();
    expect(getByTestId('menu-item-best-sellers')).toBeInTheDocument();
  });

  test('Main Banner layout is correct', () => {
    const { getByTestId } = render(<MainBanner />);
    const banner = getByTestId('main-banner');
    
    expect(banner).toHaveStyle('display: flex');
    expect(getByTestId('banner-text')).toHaveStyle('text-align: center');
    expect(getByTestId('banner-image-left')).toBeInTheDocument();
    expect(getByTestId('banner-image-right')).toBeInTheDocument();
  });

  test('Content Section layout is correct', () => {
    const { getByTestId } = render(<ContentSection />);
    const contentSection = getByTestId('content-section');

    expect(contentSection).toHaveStyle('display: grid');
    expect(contentSection).toHaveStyle('grid-template-columns: repeat(4, 1fr)');
  });

  const columnTests = [
    { column: 'column-1', linkText: 'Join Prime' },
    { column: 'column-2', linkText: 'Shop all' },
    { column: 'column-3', linkText: 'Join Prime' },
    { column: 'column-4', linkText: 'Shop new little looks' }
  ];

  columnTests.forEach(({ column, linkText }) => {
    test(`${column} layout and components are correct`, () => {
      const { getByTestId } = render(<ContentSection />);
      const columnElement = getByTestId(column);

      expect(columnElement).toHaveStyle('display: grid');
      expect(columnElement).toHaveStyle('grid-template-columns: repeat(2, 1fr)');
      expect(columnElement).toHaveStyle('grid-template-rows: repeat(2, 1fr)');

      for (let i = 1; i <= 4; i++) {
        expect(getByTestId(`${column}-image-${i}`)).toBeInTheDocument();
        expect(getByTestId(`${column}-text-${i}`)).toBeInTheDocument();
      }

      expect(getByTestId(`${column}-link`)).toHaveTextContent(linkText);
    });
  });

  test('Typography and colors are correct', () => {
    const { getByTestId } = render(<MainPage />);
    const headers = getByTestId('headers');
    const subText = getByTestId('sub-text');
    const links = getByTestId('links');

    expect(headers).toHaveStyle('font-size: large');
    expect(headers).toHaveStyle('font-weight: bold');
    expect(subText).toHaveStyle('font-size: medium');
    expect(subText).toHaveStyle('font-weight: regular');
    expect(links).toHaveStyle('font-size: medium');
    expect(links).toHaveStyle('text-decoration: underline');
    expect(links).toHaveStyle('color: blue');
  });

  test('Images and media styling is correct', () => {
    const { getByTestId } = render(<ImageComponent />);
    const image = getByTestId('image');

    expect(image).toHaveStyle('aspect-ratio: 1 / 1');
    expect(image).toHaveStyle('border-radius: 8px'); // Assuming rounded corners
  });

  test('Interactive elements are styled correctly', () => {
    const { getByTestId } = render(<InteractiveComponent />);
    const button = getByTestId('button');
    const link = getByTestId('link');

    expect(button).toHaveStyle('transition: background-color 0.3s');
    expect(link).toHaveStyle('text-decoration: none');
    expect(link).toHaveStyle('color: blue');
  });

  test('Accessibility features are present', () => {
    const { getByAltText, getByTestId } = render(<AccessibleComponent />);
    const image = getByAltText('Descriptive alt text');
    const button = getByTestId('focus-button');

    expect(image).toBeInTheDocument();
    expect(button).toHaveStyle('outline: 2px solid blue'); 
  });

});