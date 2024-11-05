import React from 'react';
import { render, screen } from '@testing-library/react';
import ContentSection from './ContentSection';


describe('ContentSection Component', () => {
  beforeEach(() => {
    render(<ContentSection />);
  });

  it('should render the content section with correct layout', () => {
    const contentSection = screen.getByTestId('content-section');
    expect(contentSection).toBeInTheDocument();
    expect(contentSection).toHaveStyle('display: grid');
    expect(contentSection).toHaveStyle('grid-template-columns: repeat(4, 1fr)');
    expect(contentSection).toHaveStyle('gap: 20px');
    expect(contentSection).toHaveStyle('padding: 20px');
  });

  it('should contain four ContentColumn components', () => {
    const columns = screen.getAllByRole('contentcolumn');
    expect(columns.length).toBe(4);
  });

  it('should render the first column with correct title and link text', () => {
    const firstColumn = screen.getByText('Being a Prime member adds up');
    expect(firstColumn).toBeInTheDocument();
    const firstLink = screen.getByText('Join Prime');
    expect(firstLink).toBeInTheDocument();
  });

  it('should render the second column with correct title and link text', () => {
    const secondColumn = screen.getByText('Shop the Winterize Your Ride Event');
    expect(secondColumn).toBeInTheDocument();
    const secondLink = screen.getByText('Shop all');
    expect(secondLink).toBeInTheDocument();
  });

  it('should render the third column with correct title and link text', () => {
    const thirdColumn = screen.getByText('Enjoy all the Prime benefits');
    expect(thirdColumn).toBeInTheDocument();
    const thirdLink = screen.getByText('Join Prime');
    expect(thirdLink).toBeInTheDocument();
  });

  it('should render the fourth column with correct title and link text', () => {
    const fourthColumn = screen.getByText('modern moments™ by Gerber');
    expect(fourthColumn).toBeInTheDocument();
    const fourthLink = screen.getByText('Shop new little looks');
    expect(fourthLink).toBeInTheDocument();
  });
});