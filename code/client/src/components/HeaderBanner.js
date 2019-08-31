/**
 * Header component, contains logo, h1, nav, search, and social media links
 */
import React from "react";

import Navigation from "./Navigation";

import logo from "../img/logo.webp";
import SocialBanner from "./SocialBanner";

const HeaderBanner = () => {
  return (
    <div className="header-banner">
      <div className="header-banner__logo">
        <img src={logo} alt="Techlab Logo" />
      </div>
      <div className="header-banner__title">
        <h1>The Site Name</h1>
      </div>
      <Navigation />
      <SocialBanner />
    </div>
  );
};

export default HeaderBanner;
