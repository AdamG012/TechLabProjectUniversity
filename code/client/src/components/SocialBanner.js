/**
 * Component to display all relevant SocialMedia components
 */
import React from "react";

import SocialMedia from "./SocialMedia";

import { ReactComponent as FacebookLogo } from "../svg/SVG/facebook.svg";
import { ReactComponent as InstagramLogo } from "../svg/SVG/instagram.svg";
import { ReactComponent as TumblerLogo } from "../svg/SVG/tumblr.svg";
import { ReactComponent as TwitterLogo } from "../svg/SVG/twitter.svg";
import { ReactComponent as YoutubeLogo } from "../svg/SVG/youtube.svg";

const socialMediaAPIMock = {
  success: true,
  sites: [
    {
      name: "Facebook",
      url: "https://www.facebook.com/usydtechlab/",
      svg: <FacebookLogo />
    },
    {
      name: "Instagram",
      url: "www.instagram.com",
      svg: <InstagramLogo />
    },
    {
      name: "Tumblr",
      url: "www.tumblr.com",
      svg: <TumblerLogo />
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
  ]
};

class SocialBanner extends React.Component {
  renderContent = () => {
    const socialMediaSites = socialMediaAPIMock.sites;
    // either use fetch here or read from raw data
    return socialMediaSites.map((item, index) => {
      return (
        <li className="social-banner__list-item" key={index}>
          <SocialMedia url={item.url} svgSource={item.svg} alt={item.name} />
        </li>
      );
    });
  };

  render() {
    return (
      <div className="social-banner">
        <ul className="social-banner__list">{this.renderContent()}</ul>
      </div>
    );
  }
}

export default SocialBanner;
