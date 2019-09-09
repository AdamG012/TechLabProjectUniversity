import React from "react";
import { Link } from "react-router-dom";

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
              About
            </Link>
          </li>
          <li className="navigation__list-item">
            <Link className="navigation__link" to="/articles">
              Articles
            </Link>
          </li>
          <li className="navigation__list-item">
            <Link className="navigation__link" to="/contact">
              Contact
            </Link>
          </li>
        </ul>
      </nav>
    </div>
  );
};

export default Navigation;
