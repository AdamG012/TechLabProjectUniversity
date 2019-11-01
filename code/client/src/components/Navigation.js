import React, { Component } from "react";
import Navbar from "react-bootstrap/Navbar";
import Nav from "react-bootstrap/Nav";

import SocialBanner from "./SocialBanner";

class Navigation extends Component {
  render() {
    return (
      <Navbar color="black" expand="lg">
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse className="nav-hamburger" id="basic-navbar-nav">
          <Nav className="mr-auto">
            <Nav.Link className="nav-bar-item" href="/">
              Home
            </Nav.Link>
            <Nav.Link className="nav-bar-item" href="/about">
              About
            </Nav.Link>
            <Nav.Link className="nav-bar-item" href="/">
              Events
            </Nav.Link>
            <SocialBanner />
          </Nav>
        </Navbar.Collapse>
      </Navbar>
    );
  }
}

export default Navigation;
