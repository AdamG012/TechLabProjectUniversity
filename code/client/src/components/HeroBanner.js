import React from "react";
import {ModalTitle} from "react-bootstrap";

const HeroBanner = () => {
  return (
      <ModalTitle>
    <div className="hero-banner">
      <div className="hero-banner__primary-text">
        <h1 className="h1">The Trend Report</h1>
      </div>
      <div className="hero-banner__secondary-text">
        <h5 className="h5">All the Latest</h5>
      </div>
    </div>
      </ModalTitle>
  );
};

export default HeroBanner;
