import React from "react";
import HeaderBanner from "./HeaderBanner";
import ArticlesContainer from "../containers/ArticlesContainer";

import "./../../src/css/style.css";

//background video
// https://video.wixstatic.com/video/11062b_6743da5900054f1f8e69f53302930a6a/1080p/mp4/file.mp4

class App extends React.Component {
  render() {
    return (
      <div className="page-container">
        <HeaderBanner />
        <ArticlesContainer />
      </div>
    );
  }
}

{
  /* <video className="background-video" autoPlay muted loop height="100%">
          <source
            src="https://video.wixstatic.com/video/11062b_6743da5900054f1f8e69f53302930a6a/1080p/mp4/file.mp4"
            type="video/mp4"
          />
        </video> */
}

export default App;
