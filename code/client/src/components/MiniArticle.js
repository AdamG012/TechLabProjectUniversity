/**
 * Component which renders miniaturised versions of articles for
 * display in the HomePage SideBanner
 *
 * Is rendered by SideBanner component
 */

import React from "react";

const MiniArticle = props => {
  return (
    <div className="mini-article">
      <div className="mini-article__image"></div>
      <div className="mini-article__content">
        <h6 className="h6">{props.title}</h6>
        <hr></hr>
        <p className="paragraph">{props.content}</p>
      </div>
    </div>
  );
};

MiniArticle.defaultProps = {
  title: "No Title",
  content: "No Content"
};

export default MiniArticle;
