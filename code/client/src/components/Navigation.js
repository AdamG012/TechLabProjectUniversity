import React, {Component} from "react";
import { Link } from "react-router-dom";
import Navbar from "react-bootstrap/Navbar";
import Nav from "react-bootstrap/Nav";
import NavLink from "react-bootstrap/NavLink";
import NavItem from "react-bootstrap/NavItem";
import SocialBanner from "./SocialBanner";

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
