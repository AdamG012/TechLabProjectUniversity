/**
 * The side banner as seen on the right hand side of the home page
 * Renders MiniArticle components in the banner
 */
import React from "react";
import MiniArticle from "./MiniArticle";

const SideBanner = props => {
  return (
    <div className="side-banner">
      <MiniArticle />
      <MiniArticle />
      <MiniArticle />
    </div>
  );
};

export default SideBanner;
