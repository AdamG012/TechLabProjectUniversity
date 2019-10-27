import React from "react";

import HeaderBanner from "../HeaderBanner";
import Footer from "../Footer";
import SingleArticleContainer from "../../containers/SingleArticleContainer";
import Col from "react-bootstrap/Col";
import Row from "react-bootstrap/Row";
import Container from "react-bootstrap/Container";

const ArticlePage = props => {
  console.log(props);
  return (
    <Container fluid>
        <Row>
            <Col className="black-background">
                <HeaderBanner />
            </Col>
        </Row>
        <Row>
            <Col className="black-background">
                <div style={{height: "7rem"}}/>
                <SingleArticleContainer articleId={props.match.params.id} />            </Col>
        </Row>
        <Row>
            <Col className="black-background">
                <Footer />
            </Col>
        </Row>
    </Container>
  );
};

export default ArticlePage;
