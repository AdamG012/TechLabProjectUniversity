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
  constructor(props) {
    super(props);

    this.toggle = this.toggle.bind(this);
    this.state = {
      isOpen: false
    };
  }
  toggle() {
    this.setState({
      isOpen: !this.state.isOpen
    });
  }
  render() {
    return (
        <Navbar color="black" dark expand="lg">

          <Navbar.Toggle aria-controls="basic-navbar-nav" />
          <Navbar.Collapse color="white" id="basic-navbar-nav">
            <Nav className="mr-auto">
              <Nav.Link className="navbar-item" href="/">Home</Nav.Link>
              <Nav.Link className="navbar-item" href="/about">About</Nav.Link>
              <Nav.Link className="navbar-item" href="/">Events</Nav.Link>

            </Nav>
          </Navbar.Collapse>
        </Navbar>
    );
  }
}

export default Navigation;
