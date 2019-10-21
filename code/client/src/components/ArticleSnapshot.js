/**
 * Component to display article sneak peek
 */
import React from "react";
import PropTypes from "prop-types";

/**
 * Individual article snapshots which are rendered by the ArticlesContainer
 * @param {} props
 */
const ArticleSnapshot = props => {
  return (
      <div>
    <div
      className="article-snapshot"
      onClick={() => console.log("article clicked")}
    >
      <div
        className="article-snapshot__img-container"
        style={{ backgroundImage: `url(${props.imageURL})` }}
      ></div>
      <div className="article-snapshot__content-container">
        <h6 className="article-snapshot__heading">{props.title}</h6>
        <p className="article-snapshot__text">{props.content}</p>
      </div>
    </div>
      </div>
  );
};

ArticleSnapshot.propTypes = {
  title: PropTypes.string.isRequired,
  content: PropTypes.string.isRequired,
  imageURL: PropTypes.string.isRequired
};

export default ArticleSnapshot;
