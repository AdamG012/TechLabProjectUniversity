import React from "react";
import SocialBanner from "./SocialBanner";
import Button from "./Button";
import Navigation from "./Navigation";
import Navbar from "react-bootstrap/Navbar";
import NavbarBrand from "react-bootstrap/NavbarBrand";
import NavbarToggle from "react-bootstrap/NavbarToggle";
import Collapse from "react-bootstrap/Collapse";
import Nav from "react-bootstrap/Nav";
import NavItem from "react-bootstrap/NavItem";
import NavLink from "react-bootstrap/NavLink";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";

const Footer = () => {
  return (
      <Container fluid>
      <Row>
    <div className="footer">
      <div className="footer__content">
        <div className="footer__img">
          <img src={require("../img/logo.jpeg")}></img>
        </div>
        <ul className="footer__list">
          <Col>
          <li className="footer__list-element">About</li>
          </Col>
          <Col>
            <li className="footer__list-element">Contact Us</li>
          </Col>
          <Col>
            <li className="footer__list-element">Terms of Use</li>
          </Col>
          <Col>
            <li className="footer__list-element">Meet Us</li>
          </Col>
          <Col>
            <li className="footer__list-element">Privacy Policy</li>
          </Col>
        </ul>
        <Col>
        <div className="footer__btn">
          <Button color="black" text="Admin" />
        </div>
        </Col>
      </div>
      <div className="footer__bottom">
        <SocialBanner />
        <p>&copy;2019 by HandOfTheFek. Proudly created with Wix.com</p>
      </div>
    </div>
      </Row>
      </Container>
  );
};

export default Footer;
