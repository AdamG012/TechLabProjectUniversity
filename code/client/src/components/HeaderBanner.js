/**
 * Sticky header component, contains navigation and social media
 */
import React from "react";

import Navigation from "./Navigation";

import SocialBanner from "./SocialBanner";
import GetInTouch from "./GetInTouch";

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

const HeaderBanner = props => {
  return (
    <div className="header-banner">
      <div className="header-banner__title">
        <h1>TechLab</h1>
      </div>
      <Navigation />
      <SocialBanner data={socialMediaAPIMock} />
      <GetInTouch contactRef={props.contactRef} />
    </div>
  );
};

export default HeaderBanner;
