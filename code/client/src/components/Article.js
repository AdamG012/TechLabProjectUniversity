import React from "react";
import PropTypes from "prop-types";

class Article extends React.Component {
  render() {
    const html = { __html: this.props.content };
    return (
      <div className="article">
        <p></p>
        <div
          className="article__content-container"
          dangerouslySetInnerHTML={html}
        ></div>
      </div>
    );
  }
}

Article.defaultProps = {
  content: { __html: "<h1>Hello World</h1>" }
};

Article.propTypes = {
  content: PropTypes.string.isRequired
};

export default Article;
