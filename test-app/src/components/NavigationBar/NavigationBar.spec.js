import React from 'react';
import { render } from '@testing-library/react';
import NavigationBar from './NavigationBar';

describe('NavigationBar Component', () => {
  test('renders navigation bar with correct structure', () => {
    const { getByTestId, getAllByTestId } = render(<NavigationBar />);
    
    const navigationBar = getByTestId('navigation-bar');
    expect(navigationBar).toBeInTheDocument();
    expect(navigationBar).toHaveStyle('display: flex');
    expect(navigationBar).toHaveStyle('justify-content: space-around');
    expect(navigationBar).toHaveStyle('background-color: white');
    expect(navigationBar).toHaveStyle('padding: 10px 0');

    const menuItems = getAllByTestId('menu-item');
    expect(menuItems).toHaveLength(4);
    menuItems.forEach((item) => {
      expect(item).toHaveStyle('cursor: pointer');
    });
  });

  test('checks if menu items have correct text', () => {
    const { getAllByTestId } = render(<NavigationBar />);
    const menuItems = getAllByTestId('menu-item');

    const menuTexts = ['All', 'Medical Care', 'Best Sellers', '...'];
    menuItems.forEach((item, index) => {
      expect(item).toHaveTextContent(menuTexts[index]);
    });
  });
});