/**
 * Component to display all relevant SocialMedia components
 */
import React from "react";

import SocialMedia from "./SocialMedia";

class SocialBanner extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      siteData: props.data ? props.data : null
    };
  }

  renderContent = () => {
    const { siteData } = this.state;
    // either use fetch here or read from raw data
    return siteData.map((item, index) => {
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
