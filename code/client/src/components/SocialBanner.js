/**
 * Component to display all relevant SocialMedia components
 */
import React from "react";

import SocialMedia from "./SocialMedia";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";

const socialMediaSites = [
  {
    name: "Facebook",
    url: "https://www.facebook.com/usydtechlab/",
    svg: "#facebook-letter-logo"
  },
  {
    name: "Twitter",
    url: "https://twitter.com/usydtechlab?lang=en",
    svg: "#twitter-logo"
  },
  {
    name: "Youtube",
    url: "https://www.youtube.com/channel/UCitvyHTDa2bRaS1oM2XV1vQ",
    svg: "#youtube-play-button"
  },
  {
    name: "Github",
    url: "https://github.com/usydtechlab",
    svg: "#github-logo"
  },
  {
    name: "Github Enterprise",
    url: "https://github.sydney.edu.au/TechLab",
    svg: "#github-logo"
  }
];

class SocialBanner extends React.Component {
  renderContent = () => {
    return socialMediaSites.map((item, index) => {
      return (
          <li className="social-banner__list-item" key={index}>
            <SocialMedia url={item.url} svgId={item.svg} alt={item.name} />
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
