import React from "react";
import HeaderBanner from "../HeaderBanner";
import CreateArticle from "../CreateArticle";
import Footer from "../Footer";

class CreateArticlePage extends React.Component {
  render() {
    return (
      <div>
        <HeaderBanner />
        <CreateArticle />
        <Footer />
      </div>
    );
  }
}

export default CreateArticlePage;
