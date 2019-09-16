import React from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";

import HomePage from "./Pages/HomePage";
import AboutPage from "./Pages/AboutPage";
import ArticlePage from "./Pages/ArticlePage";
import CreateArticle from "./CreateArticle";
import FourOhFour from "./Pages/FourOhFour";

import "../styling/compiledStyles.css";

//background video
// https://video.wixstatic.com/video/11062b_6743da5900054f1f8e69f53302930a6a/1080p/mp4/file.mp4

/* <video className="background-video" autoPlay muted loop height="100%">
          <source
            src="https://video.wixstatic.com/video/11062b_6743da5900054f1f8e69f53302930a6a/1080p/mp4/file.mp4"
            type="video/mp4"
          />
        </video> */

class App extends React.Component {
  render() {
    return (
      <Router>
        <Switch>
          <Route exact path="/" component={HomePage} />
          <Route exact path="/createArticle" component={CreateArticle} />
          <Route path="/about" component={AboutPage} />
          <Route path="/articles" component={ArticlePage} />
          <Route component={FourOhFour} />
        </Switch>
      </Router>
    );
  }
}

export default App;
