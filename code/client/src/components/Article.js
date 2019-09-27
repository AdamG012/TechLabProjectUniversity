import React from "react";
import PropTypes from "prop-types";

class Article extends React.Component {
  render() {
    return (
      <div className="article">
        <div
          className="article__content-container"
          dangerouslySetInnerHTML={this.props.content}
        ></div>
      </div>
    );
  }
}

Article.defaultProps = {
  content: "No Content To Display"
};

Article.propTypes = {
  content: PropTypes.string.isRequired
};

export default Article;
