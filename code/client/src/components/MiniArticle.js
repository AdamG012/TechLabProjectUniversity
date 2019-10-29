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
      <div className="mini-article__image">
        <img
          alt="Techlab Event"
          src="https://static.wixstatic.com/media/fd5752f4ee5b4580b359d3ea16c8b715.jpeg/v1/fill/w_125,h_120,al_c,q_80,usm_0.66_1.00_0.01/fd5752f4ee5b4580b359d3ea16c8b715.webp"
        />
      </div>
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
