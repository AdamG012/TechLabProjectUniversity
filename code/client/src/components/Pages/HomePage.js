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
import ArticleFilter from "../ArticleFilter";


const HomePage = () => {
  const contactFormRef = React.createRef();
  return (
      <Container fluid>
          <Row>
              <Col xs={'auto'}>
                  <HeaderBanner contactRef={contactFormRef} />
              </Col>
          </Row>
          <Row>
              <Col xs={'auto'}>
                  <HeroBanner />
              </Col>
          </Row>
          <Row>
              <Col xs={'auto'}>
                      <div className="homepage__content">
                          <div className="homepage__content-leftColumn">
                              <div className="post-filter-and-search">
                                  <ArticleFilter />
                                  <Search />
                              </div>
                              <ArticlesContainer />
                          </div>
                      </div>
              </Col>
          </Row>
          <Row>
              <Col xs={'auto'}>
                  <div className="homepage__content">

                      <div className="homepage__content-rightColumn">
                              <SideBannerContainer />
                      </div>
                  </div>
              </Col>
          </Row>
          <Row>
              <Col xs={'auto'}>
                      <div className="homepage__contact">
                          <ContactForm ref={contactFormRef} />
                          <div>
                              <Map />
                          </div>
                      </div>
                      <div>
                          <Footer />
                      </div>
              </Col>
          </Row>
      </Container>

  );
};

export default HomePage;
