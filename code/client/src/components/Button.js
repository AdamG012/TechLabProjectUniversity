import React from "react";
import PropTypes from "prop-types";

const Button = props => {
  const buttonColor = props.color;
  return (
    <div className={`btn btn--${buttonColor}`} onClick={props.handleClick}>
      <p className="btn__text">{props.text}</p>
    </div>
  );
};

Button.propTypes = {
  color: PropTypes.string.isRequired
};

Button.defaultProps = {
  text: "Click Here"
};

export default Button;
