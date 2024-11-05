import React from 'react';
import { render, screen } from '@testing-library/react';
import ContentColumn from './ContentColumn';

describe('ContentColumn Component', () => {
  const title = 'Sample Title';
  const linkText = 'Sample Link';

  beforeEach(() => {
    render(<ContentColumn title={title} linkText={linkText} />);
  });

  test('renders the content column with correct title', () => {
    const titleElement = screen.getByText(title);
    expect(titleElement).toBeInTheDocument();
    expect(titleElement).toHaveStyle({
      fontSize: '24px',
      fontWeight: 'bold',
      textAlign: 'left',
    });
  });

  test('renders a 2x2 grid of images with descriptions', () => {
    const gridContainer = screen
      .getByTestId('content-column')
      .querySelector('.grid-container');
    expect(gridContainer).toHaveStyle({
      display: 'grid',
      gridTemplateColumns: '1fr 1fr',
      gap: '10px',
    });

    const gridItems = screen.getAllByTestId('grid-item');
    expect(gridItems).toHaveLength(4);
    gridItems.forEach((item) => {
      expect(item).toHaveStyle({ textAlign: 'center' });
      const img = item.querySelector('img');
      expect(img).toHaveAttribute('src', 'placeholder.jpg');
      expect(img).toHaveStyle({
        width: '100px',
        height: '100px',
        borderRadius: '8px',
      });
    });
  });

  test('renders a link with correct text', () => {
    const linkElement = screen.getByTestId('link');
    expect(linkElement).toBeInTheDocument();
    expect(linkElement).toHaveTextContent(linkText);
    expect(linkElement).toHaveStyle({
      color: 'blue',
      textDecoration: 'underline',
    });
  });

  test('content column has correct padding and background color', () => {
    const contentColumn = screen.getByTestId('content-column');
    expect(contentColumn).toHaveStyle({
      padding: '10px',
      backgroundColor: 'white',
    });
  });
});
