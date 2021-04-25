/**
 * This container is responsible for making an API request then
 * render the SideBanner component
 */

import React from "react";
import SideBanner from "../components/SideBanner";

class SideBannerContainer extends React.Component {
  componentDidMount() {
    //make api call
  }

  render() {
    return <SideBanner />;
  }
}

export default SideBannerContainer;
