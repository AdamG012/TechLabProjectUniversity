import { Link } from "react-router-dom";
import React from "react";
import SocialBanner from "./SocialBanner";
import Button from "./Button";
import Navigation from "./Navigation";

const Footer = () => {
  return (
    <div className="footer">
      <div className="footer__content">
        <div className="black-background">
          <img src={require("../img/logo.jpeg")}></img>
        </div>
        <ul className="footer__list">
          <li className="footer__list-element">
            <b>About</b>
          </li>
          <li className="footer__list-element">
            <Link className="navigation__link" to="/">
              Contact Us
            </Link>
          </li>
          <li className="footer__list-element">
            <Link className="navigation__link" to="/about">
              Meet us
            </Link>
          </li>
        </ul>
        <ul className="footer__list">
          <li className="footer__list-element">
            <a
              className="navigation__link"
              target="_blank"
              href={"https://sydney.edu.au/privacy-statement.html"}
            >
              Privacy Policy
            </a>
          </li>
          <div className="footer__list-element">
            <Link className="navigation__link" to="/admin">
              Admin
            </Link>
          </div>
        </ul>
      </div>
      <div className="footer__bottom">
        <SocialBanner />
        <p>&copy;2019 by HandOfTheFek. Proudly created with Wix.com</p>
      </div>
    </div>
  );
};

export default Footer;
