import React from "react";
import HeaderBanner from "../HeaderBanner";
import MeetTheTeam from "../MeetTheTeam";
import Footer from "../Footer";
import {Container} from "react-bootstrap";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";

const AboutPage = () => {
  return (
      <Container fluid>
        <Row>
            <Col>
      <HeaderBanner />
            </Col>
        </Row>
      <MeetTheTeam />
        <Row>
            <Col>
      <Footer />
            </Col>
        </Row>
      </Container>
  );
};

export default AboutPage;
