import React from "react";
import PropTypes from "prop-types";

import SocialMedia from "./SocialMedia";

const PersonCard = props => {
  return (
    <div className="person-card">
      <div className="person-card__img">
        <img />
      </div>
      <h6>{props.name}</h6>
      <SocialMedia url={props.link} svgId="#github-logo" alt="GitHub" />
      <p>{props.text}</p>
    </div>
  );
};

export default PersonCard;

PersonCard.propTypes = {
  name: PropTypes.string,
  link: PropTypes.string,
  text: PropTypes.string
};
