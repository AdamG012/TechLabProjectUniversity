/**
 * Search Bar Component - displays input and search button
 */

import React from "react";
import { Redirect } from "react-router-dom";

class Search extends React.Component {
  state = {
    redirect: false,
    searchTerm: ""
  };

  enterPressed = e => {
    let code = e.key || e.which;
    if (code === "Enter") {
      this.setState({ redirect: true });
      return;
    }
  };

  handleClick = () => {
    this.setState({ redirect: true });
  };

  handleInputChange = e => {
    this.setState({ searchTerm: e.target.value });
  };

  render() {
    if (this.state.redirect) {
      return <Redirect to={`/search/${this.state.searchTerm}`} />;
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
            onChange={this.handleInputChange}
            value={this.state.searchTerm}
          />
          <button onClick={this.handleClick} className="search__button">
            Search
          </button>
        </div>
      );
    }
  }
}

export default Search;
