import React from "react";
import PropTypes from "prop-types";

const PersonCard = props => {
  return (
    <div className="person-card">
      <div className="person-card__img">
        <img src={require(`../img/${props.img}`)} alt={props.name} />
      </div>
      <div className="person-card__content">
        <h6 className="h6">{props.name}</h6>
        <a href={props.link}>
          <svg className="person-card__svg" style={{ fill: "#AAA" }}>
            <use xlinkHref="#linked-in-logo-of-two-letters" />
          </svg>
        </a>

        <p>{props.text}</p>
      </div>
    </div>
  );
};

export default PersonCard;

PersonCard.propTypes = {
  name: PropTypes.string,
  link: PropTypes.string,
  text: PropTypes.string,
  img: PropTypes.string
};
