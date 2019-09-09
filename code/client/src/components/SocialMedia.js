/**
 * Component to render a single social media link and image (these are rendered dynamically based on API call by SocialBanner)
 */

import React from "react";
import PropTypes from "prop-types";

const SocialMedia = props => {
  return (
    <div>
      <a title={props.alt} href={props.url}>
        {props.svgSource}
      </a>
    </div>
  );
};

SocialMedia.propTypes = {
  url: PropTypes.string.isRequired,
  svgSource: PropTypes.object.isRequired,
  alt: PropTypes.string
};

export default SocialMedia;
