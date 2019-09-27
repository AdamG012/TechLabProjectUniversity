import React from "react";
import { Link } from "react-router-dom";

// TODO: is navigation-container required??

const Navigation = () => {
  return (
    <div className="navigation-container">
      <nav className="navigation">
        <ul className="navigation__list">
          <li className="navigation__list-item">
            <Link className="navigation__link" to="/">
              Home
            </Link>
          </li>
          <li className="navigation__list-item">
            <Link className="navigation__link" to="/about">
              Blog
            </Link>
          </li>
          <li className="navigation__list-item">
            <Link className="navigation__link" to="/contact">
              Contact
            </Link>
          </li>
          <li className="navigation__list-item">
            <Link className="navigation__link" to="/createArticle">
              Create Article
            </Link>
          </li>
        </ul>
      </nav>
    </div>
  );
};

export default Navigation;
