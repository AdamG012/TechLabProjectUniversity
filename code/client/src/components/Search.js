/**
 * Search Bar Component - displays input and search button
 */

import React from "react";
import { Redirect } from "react-router-dom";

class Search extends React.Component {
  state = {
    redirect: false
  };
  enterPressed = e => {
    console.log("key pressed with keycode", e.key);
    let code = e.key || e.which;
    if (code === "Enter") {
      console.log("redirecting");
      this.setState({ redirect: true });
      return;
    }
  };

  render() {
    if (this.state.redirect) {
      return <Redirect to="/search" />;
    } else {
      return (
        <div className="search">
          <svg className="search__svg">
            <use xlinkHref="#search"></use>
          </svg>
          <input
            className="search__input"
            name="search"
            placeholder="Search..."
            onKeyPress={this.enterPressed}
          />
          <button className="search__button">Adv Search</button>
        </div>
      );
    }
  }
}

export default Search;
