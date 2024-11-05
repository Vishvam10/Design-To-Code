import React from 'react';
import { render, screen } from '@testing-library/react';
import Header from './Header';

describe('Header Component', () => {
  beforeEach(() => {
    render(<Header />);
  });

  it('should render the header with correct layout', () => {
    const header = screen.getByTestId('header');
    expect(header).toHaveStyle('display: flex');
    expect(header).toHaveStyle('justify-content: space-between');
    expect(header).toHaveStyle('align-items: center');
    expect(header).toHaveStyle('padding: 10px');
    expect(header).toHaveStyle('background-color: white');
  });

  it('should render the logo on the left', () => {
    const logo = screen.getByTestId('logo');
    expect(logo).toBeInTheDocument();
    expect(logo).toHaveStyle('flex: 1');
  });

  it('should render the delivery information next to the logo', () => {
    const deliveryInfo = screen.getByTestId('delivery-info');
    expect(deliveryInfo).toBeInTheDocument();
    expect(deliveryInfo).toHaveStyle('flex: 1');
  });

  it('should render the search bar centered', () => {
    const searchBar = screen.getByTestId('search-bar');
    expect(searchBar).toBeInTheDocument();
    expect(searchBar).toHaveStyle('flex: 2');
    expect(searchBar).toHaveStyle('padding: 5px');
  });

  it('should render the right section with language, account, orders, and cart on the right', () => {
    const rightSection = screen.getByTestId('right-section');
    expect(rightSection).toBeInTheDocument();
    expect(rightSection).toHaveStyle('flex: 2');
    expect(rightSection).toHaveStyle('display: flex');
    expect(rightSection).toHaveStyle('justify-content: flex-end');
    expect(rightSection).toHaveStyle('gap: 10px');

    const language = screen.getByTestId('language');
    const account = screen.getByTestId('account');
    const orders = screen.getByTestId('orders');
    const cart = screen.getByTestId('cart');

    expect(language).toBeInTheDocument();
    expect(account).toBeInTheDocument();
    expect(orders).toBeInTheDocument();
    expect(cart).toBeInTheDocument();
  });

  it('should apply the default font family to all text elements', () => {
    const logo = screen.getByTestId('logo');
    const deliveryInfo = screen.getByTestId('delivery-info');
    const language = screen.getByTestId('language');
    const account = screen.getByTestId('account');
    const orders = screen.getByTestId('orders');
    const cart = screen.getByTestId('cart');

    expect(logo).toHaveStyle('font-family: inherit');
    expect(deliveryInfo).toHaveStyle('font-family: inherit');
    expect(language).toHaveStyle('font-family: inherit');
    expect(account).toHaveStyle('font-family: inherit');
    expect(orders).toHaveStyle('font-family: inherit');
    expect(cart).toHaveStyle('font-family: inherit');
  });

  it('should ensure text is black', () => {
    const logo = screen.getByTestId('logo');
    const deliveryInfo = screen.getByTestId('delivery-info');
    const language = screen.getByTestId('language');
    const account = screen.getByTestId('account');
    const orders = screen.getByTestId('orders');
    const cart = screen.getByTestId('cart');

    expect(logo).toHaveStyle('color: black');
    expect(deliveryInfo).toHaveStyle('color: black');
    expect(language).toHaveStyle('color: black');
    expect(account).toHaveStyle('color: black');
    expect(orders).toHaveStyle('color: black');
    expect(cart).toHaveStyle('color: black');
  });
});
