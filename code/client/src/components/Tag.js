import React from "react";
import PropTypes from "prop-types";

const Tag = props => {
  let tagStyle = {
    borderBottom: props.isSelected ? "1px solid black" : "none"
  };
  return (
    <div onClick={props.onClick} style={tagStyle} className="tag">
      <p className="tag__content">{props.content}</p>
    </div>
  );
};

export default Tag;

Tag.propTypes = {
  content: PropTypes.string.isRequired
};
