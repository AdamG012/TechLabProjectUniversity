import React from "react";
import PropTypes from "prop-types";
import { Row, Col, Container } from "react-bootstrap";

class Article extends React.Component {
  render() {
    const html = { __html: this.props.content };
    return (
      <Container fluid className="article">
        <Row className="article__row">
          <Col className="article__col">
            <h3 className="h3">{this.props.title}</h3>
          </Col>
        </Row>
        <Row className="article__row">
          <Col className="article__col">
            <h6>Written by: {this.props.author}</h6>
          </Col>
          <Col className="article__col">
            <h6>Time to read: {this.props.timeToRead} min</h6>
          </Col>
        </Row>
        <Row className="article__row">
          <Col className="article__col">
            <div
              className="article__content-container"
              dangerouslySetInnerHTML={html}
            ></div>
          </Col>
        </Row>
      </Container>
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
