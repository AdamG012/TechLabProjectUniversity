import React from "react";
import { Link } from "react-router-dom";
import SocialBanner from "./SocialBanner";
import Button from "./Button";

const Footer = () => {
  return (
    <div className="footer">
      <div className="footer__content">
        <div className="footer__img">
          <img src={require("../img/logo.jpeg")}></img>
        </div>
        <ul className="footer__list">
          <li className="footer__list-element">About</li>
          <li className="footer__list-element">Contact Us</li>
          <li className="footer__list-element">Terms of Use</li>
          <li className="footer__list-element">Meet Us</li>
          <li className="footer__list-element">Privacy Policy</li>
        </ul>
        <div className="footer__btn">
          <Link to="/login">
            <Button color="black" text="Admin" />
          </Link>
        </div>
      </div>
      <div className="footer__bottom">
        <SocialBanner />
        <p>&copy;2019 by HandOfTheFek. Proudly created with Wix.com</p>
      </div>
    </div>
  );
};

export default Footer;
