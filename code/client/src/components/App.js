import React from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";

import HomePage from "./Pages/HomePage";
import AboutPage from "./Pages/AboutPage";
import ArticlePage from "./Pages/ArticlePage";
import CreateArticle from "./CreateArticle";
import LoginPage from "./Pages/LoginPage";
import FourOhFour from "./Pages/FourOhFour";

import "../styling/compiledStyles.css";

class App extends React.Component {
  render() {
    return (
      <Router>
        <Switch>
          <Route exact path="/" component={HomePage} />
          <Route exact path="/createArticle" component={CreateArticle} />
          <Route path="/about" component={AboutPage} />
          <Route path="/articles" component={ArticlePage} />
          <Route path="/article/:id" component={ArticlePage} />
          <Route path="/login" component={LoginPage}></Route>
          <Route component={FourOhFour} />
        </Switch>
      </Router>
    );
  }
}

export default App;
