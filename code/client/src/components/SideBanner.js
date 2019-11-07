/**
 * The side banner as seen on the right hand side of the home page
 * Renders MiniArticle components in the banner
 */
import React from "react";
import MiniArticle from "./MiniArticle";
import { events } from "../master.json";

const renderContent = data => {
  return data.map(element => {
    return (
      <MiniArticle
        key={element.title}
        title={element.title}
        content={element.text}
        image={element.image}
      />
    );
  });
};

const SideBanner = props => {
  if (events.length === 0) {
    return null;
  }
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
