/**
 * Header component, contains logo, h1, nav, search, and social media links
 */
import React from "react";

import Navigation from "./Navigation";

import logo from "../img/logo.webp";
import SocialBanner from "./SocialBanner";

import { ReactComponent as FacebookLogo } from "../svg/SVG/facebook.svg";
import { ReactComponent as TwitterLogo } from "../svg/SVG/twitter.svg";
import { ReactComponent as YoutubeLogo } from "../svg/SVG/youtube.svg";

const socialMediaAPIMock = [
  {
    name: "Facebook",
    url: "https://www.facebook.com/usydtechlab/",
    svg: <FacebookLogo />
  },
  {
    name: "Twitter",
    url: "https://twitter.com/usydtechlab?lang=en",
    svg: <TwitterLogo />
  },
  {
    name: "Youtube",
    url: "www.youtube.com",
    svg: <YoutubeLogo />
  }
];

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
      <SocialBanner data={socialMediaAPIMock} />
    </div>
  );
};

export default HeaderBanner;
