import React from "react";

import HeaderBanner from "../HeaderBanner";
import ArticlesContainer from "../../containers/ArticlesContainer";

const HomePage = () => {
  return (
    <div className="page-container">
      <HeaderBanner />
      <ArticlesContainer />
    </div>
  );
};

export default HomePage;
