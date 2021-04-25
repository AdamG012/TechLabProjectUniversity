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
            <Col className="black-background">
                <HeaderBanner />
            </Col>
        </Row>
          <Row>
              <Col>
                  <MeetTheTeam />
              </Col>
          </Row>
        <Row>
            <Col className="black-background">
      <Footer />
            </Col>
        </Row>
      </Container>
    );
};

export default AboutPage;
