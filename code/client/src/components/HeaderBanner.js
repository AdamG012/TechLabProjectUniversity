/**
 * Sticky header component, contains navigation and social media
 */
import React from "react";

import Navigation from "./Navigation";

import SocialBanner from "./SocialBanner";
import GetInTouch from "./GetInTouch";

const HeaderBanner = props => {
  return (
    <div className="header-banner">
      <div className="header-banner__title">
        <h1>TechLab</h1>
      </div>
      <Navigation />
      <SocialBanner />
      <GetInTouch contactRef={props.contactRef} />
    </div>
  );
};

export default HeaderBanner;
