/**
 * Component to render a single social media link and image (these are rendered dynamically based on API call by SocialBanner)
 */

import React from "react";
import PropTypes from "prop-types";

const SocialMedia = props => {
  return (
    <div className="social-media">
      <a title={props.alt} target="_blank" href={props.url}>
        <svg className="social-media__svg" style={{ fill: "FFF" }}>
          <use xlinkHref={props.svgId} />
        </svg>
      </a>
    </div>
  );
};

SocialMedia.propTypes = {
  url: PropTypes.string.isRequired,
  svgId: PropTypes.string.isRequired,
  alt: PropTypes.string
};

export default SocialMedia;
