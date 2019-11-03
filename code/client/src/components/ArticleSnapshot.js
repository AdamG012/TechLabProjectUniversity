/**
 * Component to display article sneak peek
 */
import React from "react";
import PropTypes from "prop-types";
import { Link } from "react-router-dom";

/**
 * Individual article snapshots which are rendered by the ArticlesContainer
 * @param {} props
 */
const ArticleSnapshot = props => {
  return (
    <Link to={`/article/${props.id}`}>
      <div className="article-snapshot">
        <div
          className="article-snapshot__img-container"
          style={{ backgroundImage: `url(${props.imageURL})` }}
        ></div>
        <div className="article-snapshot__content-container">
          <h6 className="article-snapshot__heading">{props.title}</h6>
          <p className="article-snapshot__text">{props.abstract}</p>
        </div>
      </div>
    </Link>
  );
};

ArticleSnapshot.propTypes = {
  title: PropTypes.string.isRequired,
  content: PropTypes.string.isRequired,
  imageURL: PropTypes.string.isRequired
};

export default ArticleSnapshot;
