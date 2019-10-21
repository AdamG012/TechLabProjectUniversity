import React, {Component} from "react";
import { Link } from "react-router-dom";
import Col from "react-bootstrap/Col";
import {Container} from "react-bootstrap";
import Row from "react-bootstrap/Row";
import NavbarBrand from "react-bootstrap/NavbarBrand";
import Navbar from "react-bootstrap/Navbar";
import Nav from "react-bootstrap/Nav";
import NavLink from "react-bootstrap/NavLink";
import NavItem from "react-bootstrap/NavItem";
import Collapse from "react-bootstrap/Collapse";
import NavbarToggle from "react-bootstrap/NavbarToggle";
import NavDropdown from "react-bootstrap/NavDropdown";
import FormControl from "react-bootstrap/FormControl";
import Button from "./Button";
import Form from "react-bootstrap/Form";
import SocialBanner from "./SocialBanner";
import GetInTouch from "./GetInTouch";

const navLinks = [
  {
    text: "Home",
    toPath: "/",
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
];

const renderLinks = linkData => {
  return linkData.map(link => {
    return (
        <Nav  navbar>
          <NavItem>
            <NavLink className="mr-auto">
                <li className="navigation__list-item">
                <Link className="navigation__link" to={link.toPath}>
                  {link.text}
                </Link>
              </li>
            </NavLink>
        </NavItem>
      </Nav>

    );
  });
};

// const Navigation = () => {
//   return (
//       <Navbar color="light" light expand="lg">
//         <NavbarBrand href="/">
//           Home
//         </NavbarBrand>
//         <Collapse isOpen={true} navbar>
//         <div className="navigation-container">
//           <nav className="navigation">
//             <ul className="navigation__list">{renderLinks(navLinks)}</ul>
//           </nav>
//         </div>
//         </Collapse>
//       </Navbar>
//   );
//
// };

class Navigation extends Component {
  render() {
    return (
        <Navbar color="black" dark expand="lg">
          <Navbar.Toggle aria-controls="basic-navbar-nav"/>
          <Navbar.Collapse className="nav-hamburger" id="basic-navbar-nav">
            <Nav className="mr-auto">
              <Nav.Link className="nav-bar-item" href="/">Home</Nav.Link>
              <Nav.Link className="nav-bar-item" href="/about">About</Nav.Link>
              <Nav.Link className="nav-bar-item" href="/">Events</Nav.Link>
              <SocialBanner/>
            </Nav>
          </Navbar.Collapse>
        </Navbar>
    );
  }
}


export default Navigation;
