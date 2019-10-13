/**
 * The side banner as seen on the right hand side of the home page
 * Renders MiniArticle components in the banner
 */
import React from "react";
import MiniArticle from "./MiniArticle";

const events = [
  {
    title: "Urban Life",
    text: "Your Text Here"
  },
  {
    title: "Gals & Pals",
    text: "Your Text Here"
  },
  {
    title: "Lost Soles",
    text: "Your Text Here"
  },
  {
    title: "Running Suits",
    text: "Your Text Here"
  }
];

const renderContent = data => {
  return data.map(element => {
    return <MiniArticle title={element.title} content={element.text} />;
  });
};

const SideBanner = props => {
  return (
    <div className="side-banner">
      <div className="side-banner__heading-container">
        <h6 className="side-banner__heading-text">UPCOMING EVENTS</h6>
      </div>
      <div className="side-banner__content">{renderContent(events)}</div>
    </div>
  );
};

export default SideBanner;
