/**
 * Sticky header component, contains navigation and social media
 */
import React from "react";

import Navigation from "./Navigation";

import SocialBanner from "./SocialBanner";
import GetInTouch from "./GetInTouch";
import { Link } from "react-router-dom";

const HeaderBanner = props => {
  console.log(props);
  return (
    <>
      <div className="header-banner">
        <div className="header-banner__title">
          <Link className="navigation__link" to="/">
            <h1>TechLab</h1>
          </Link>
        </div>
        <Navigation />
        <SocialBanner />
        <GetInTouch contactRef={props.contactRef} />
      </div>
      <div className="header-banner__filler"></div>
    </>
  );
};

export default HeaderBanner;
