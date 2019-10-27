import React from "react";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";

import HeaderBanner from "../HeaderBanner";
import ArticlesContainer from "../../containers/ArticlesContainer";
import HeroBanner from "../HeroBanner";
import ContactForm from "../ContactForm";
import SideBannerContainer from "../../containers/SideBannerContainer";
import Map from "../Map";
import Footer from "../Footer";
import Search from "../Search";

const HomePage = () => {
  const contactFormRef = React.createRef();
  return (
    <div className="overlay" id="overlay">
      <HeaderBanner contactRef={contactFormRef} />
      <Container fluid className="container-fluid">
        <Row>
          <Col className="black-background"></Col>
        </Row>
        <Row>
          <Col className="black-background">
            <HeroBanner />
          </Col>
        </Row>
        <Row>
          <Col>
            <div className="homepage__content">
              <div className="homepage__content-leftColumn">
                <div className="post-filter-and-search">
                  <Search />
                </div>
                <ArticlesContainer />
              </div>
            </div>
          </Col>
          <Col>
            <div className="homepage__content">
              <SideBannerContainer />
            </div>
          </Col>
        </Row>
        <Row>
          <Col className="black-background">
            <div className="homepage__contact">
              <ContactForm ref={contactFormRef} />
            </div>
          </Col>
          <Col className="black-background">
            <div className="homepage__map">
              <Map />
            </div>
          </Col>
        </Row>
        <Row>
          <Col className="black-background">
            <div>
              <Footer />
            </div>
          </Col>
        </Row>
      </Container>
    </div>
  );
};

export default HomePage;
