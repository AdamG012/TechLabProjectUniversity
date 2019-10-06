import React from "react";
import PropTypes from "prop-types";
import { NONAME } from "dns";

const Tag = props => {
  let tagStyle = {
    borderBottom: props.isSelected ? "1px solid black" : "none"
  };
  return (
    <div style={tagStyle} className="tag">
      <p className="tag__content">{props.content}</p>
    </div>
  );
};

export default Tag;

Tag.propTypes = {
  content: PropTypes.string.isRequired
};
