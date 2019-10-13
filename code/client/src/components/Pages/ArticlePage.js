import React from "react";

import HeaderBanner from "../HeaderBanner";
import Footer from "../Footer";
import SingleArticleContainer from "../../containers/SingleArticleContainer";

const ArticlePage = props => {
  console.log(props);
  return (
    <>
      <HeaderBanner />
      <div style={{ height: "7rem" }}></div>
      <SingleArticleContainer articleId={props.match.params.id} />
      <Footer />
    </>
  );
};

export default ArticlePage;
