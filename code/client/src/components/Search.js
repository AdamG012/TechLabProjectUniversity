/**
 * Search Bar Component - displays input and search button
 */

import React from "react";

const Search = () => {
  return (
    <div className="search">
      <input className="search__input" name="search" placeholder="Search..." />
      <button className="search__button">Adv Search</button>
    </div>
  );
};

export default Search;
