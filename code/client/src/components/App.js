import React from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";

import HomePage from "./Pages/HomePage";
import AboutPage from "./Pages/AboutPage";
import ArticlePage from "./Pages/ArticlePage";
import CreateArticle from "./CreateArticle";
import LoginPage from "./Pages/LoginPage";
import FourOhFour from "./Pages/FourOhFour";
import ContactPage from "./Pages/ContactPage";
import AdminOptionsPage from "./Pages/AdminOptionsPage";
import ProtectedRoute from "./hocs/ProtectedRoute";

import "../styling/compiledStyles.css";
import SearchResultsPage from "./Pages/SearchResultsPage";

class App extends React.Component {
  state = {
    isAuthed: true
  };

  componentDidUpdate() {
    console.log("IS AUTHED", this.state.isAuthed);
  }
  authenticate = (username, password) => {
    console.log("authenticate called");
    // make API call with credentials

    // parse API call result
    // const { username } = response;

    if (username) {
      this.setState({ isAuthed: true });
    }
  };

  logout = () => {
    this.setState({ isAuthed: false });
  };

  render() {
    return (
      <Router>
        <Switch>
          <Route exact path="/" component={HomePage} />
          <Route
            exact
            path="/admin/articles/create"
            component={CreateArticle}
          />
          <Route path="/about" component={AboutPage} />
          <Route path="/contact" component={ContactPage} />
          <Route path="/article/:id" component={ArticlePage} />
          <Route path="/login">
            <LoginPage authFunc={this.authenticate} />
          </Route>
          <ProtectedRoute
            isAllowed={this.state.isAuthed}
            path="/admin"
            component={AdminOptionsPage}
          />
          <Route path="/search/:searchTerm?" component={SearchResultsPage} />
          <Route component={FourOhFour} />
        </Switch>
      </Router>
    );
  }
}

export default App;
