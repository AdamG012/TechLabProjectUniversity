import React from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import axios from "axios";

import HomePage from "./Pages/HomePage";
import AboutPage from "./Pages/AboutPage";
import ArticlePage from "./Pages/ArticlePage";
import LoginPage from "./Pages/LoginPage";
import FourOhFour from "./Pages/FourOhFour";
import CreateArticlePage from "./Pages/CreateArticlePage";
import ContactPage from "./Pages/ContactPage";
import AdminOptionsPage from "./Pages/AdminOptionsPage";
import ProtectedRoute from "./hocs/ProtectedRoute";
import EditArticlePage from "./Pages/EditArticlePage";
import DeleteArticlePage from "./Pages/DeleteArticlePage";

import transport from "../axios.js";

import { API_URL } from "../config.json";

import "../styling/compiledStyles.css";
import SearchResultsPage from "./Pages/SearchResultsPage";

class App extends React.Component {
  state = {
    isAuthed: false
  };

  componentDidUpdate() {
    console.log("IS AUTHED", this.state.isAuthed);
  }

  authenticate = async (username, password) => {
    const loginData = {
      username,
      password
    };
    transport
      .post(`${API_URL}/admin/login`, {
        username,
        password
      })
      .then(res => {
        console.log(res);
        if (res.data.success === "true") {
          this.setState({ isAuthed: true });
          window.alert("SUCCESSFULLY LOGGED IN");
        } else {
          window.alert("incorrect credentials");
        }
      });
    // const res = await fetch(`${API_URL}/admin/login`, {
    //   method: "POST",
    //   body: JSON.stringify(loginData)
    // });
    // console.log("auth returned");
    // console.log(res);

    // const resData = await res.json();

    // if (resData.success === "true") {
    //   this.setState({ isAuthed: true });
    //   window.alert("SUCCESSFULLY LOGGED IN");
    // } else {
    //   window.alert("incorrect credentials");
    // }
  };

  logout = () => {
    this.setState({ isAuthed: false }); // make API call with credentials

    // parse API call result
    // const { username } = response;te({ isAuthed: false });
  };

  render() {
    return (
      <Router>
        <Switch>
          <Route exact path="/" component={HomePage} />
          <ProtectedRoute
            isAllowed={this.state.isAuthed}
            path="/admin/article/create"
            component={CreateArticlePage}
          />
          <Route
            isAllowed={this.state.isAuthed}
            path="/admin/article/edit"
            component={EditArticlePage}
          />
          <Route
            isAllowed={this.state.isAuthed}
            path="/admin/article/delete"
            component={DeleteArticlePage}
          />
          <Route path="/about" component={AboutPage} />
          <Route path="/contact" component={ContactPage} />
          <Route path="/article/:id" component={ArticlePage} />
          <Route path="/login">
            <LoginPage authFunc={this.authenticate} />
          </Route>
          <Route
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
