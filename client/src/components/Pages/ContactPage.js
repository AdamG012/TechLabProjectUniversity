import React from "react";
import HeaderBanner from "../HeaderBanner";
import ContactForm from "../ContactForm";
import Map from "../Map";
import Footer from "../Footer";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";

class ContactPage extends React.Component {
  render() {
    return (
      <>
        <HeaderBanner />
        <Row>
          <Col className="black-background">
            <div className="homepage__contact">
              <ContactForm />
            </div>
          </Col>
          <Col className="black-background">
            <div className="homepage__map">
              <Map />
            </div>
          </Col>
        </Row>
        <Footer />
      </>
    );
  }
}

export default ContactPage;
