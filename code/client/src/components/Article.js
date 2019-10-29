import React from "react";
import PropTypes from "prop-types";

class Article extends React.Component {
  render() {
    const html = { __html: this.props.content };
    return (
      <div className="article">
        <h6>Title</h6>
        <p>{this.props.title}</p>
        <h6>Author</h6>
        <p>{this.props.author}</p>
        <h6>Time to read</h6>
        <p>{this.props.timeToRead} min</p>
        <h6>Content</h6>
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
  content: PropTypes.string.isRequired,
  title: PropTypes.string,
  author: PropTypes.string
};

export default Article;
