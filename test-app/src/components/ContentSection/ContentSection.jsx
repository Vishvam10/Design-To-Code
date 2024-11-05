import React from 'react';
import ContentColumn from './../ContentColumn/ContentColumn';

import './index.css';

const ContentSection = () => (
  <section className="content-section" data-testid="content-section">
    <ContentColumn title="Being a Prime member adds up" linkText="Join Prime" />
    <ContentColumn title="Shop the Winterize Your Ride Event" linkText="Shop all" />
    <ContentColumn title="Enjoy all the Prime benefits" linkText="Join Prime" />
    <ContentColumn title="modern moments™ by Gerber" linkText="Shop new little looks" />
  </section>
);

export default ContentSection;