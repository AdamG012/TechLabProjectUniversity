/**
 * Sticky header component, contains navigation and social media
 */
import React from "react";

import Navigation from "./Navigation";

import SocialBanner from "./SocialBanner";
import GetInTouch from "./GetInTouch";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";

const HeaderBanner = props => {
  return (
    <>
        <Container fluid>
        <Row>
      <div className="header-banner">
        <div className="header-banner__title">
          <Col>
            <h1>TechLab</h1>
          </Col>
        </div>
          <Col>
        <Navigation />
          </Col>
          <Col>
        <SocialBanner />
          </Col>
          <Col>
        <GetInTouch contactRef={props.contactRef} />
          </Col>

      </div>
      <div className="header-banner__filler"/>
        </Row>
        </Container>
    </>
  );
};

export default HeaderBanner;
