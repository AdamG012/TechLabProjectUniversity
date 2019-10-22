import React from "react";
import { Link } from "react-router-dom";

const navLinks = [
  {
    text: "Home",
    toPath: "/",
    requiresAuth: false
  },
  {
    text: "Blog",
    toPath: "/articles",
    requiresAuth: false
  },
  {
    text: "Events",
    toPath: "/events",
    requiresAuth: false
  },
  {
    text: "About",
    toPath: "/about",
    requiresAuth: false
  },
  {
    text: "Create Article",
    toPath: "/createArticle",
    requiresAuth: true
  }
];

const renderLinks = linkData => {
  return linkData.map(link => {
    return (
      <li key={link.toPath} className="navigation__list-item">
        <Link className="navigation__link" to={link.toPath}>
          {link.text}
        </Link>
      </li>
    );
  });
};

const Navigation = () => {
  return (
    <div className="navigation-container">
      <nav className="navigation">
        <ul className="navigation__list">{renderLinks(navLinks)}</ul>
      </nav>
    </div>
  );
};

export default Navigation;
