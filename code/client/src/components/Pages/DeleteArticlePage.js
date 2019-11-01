import React from "react";
import HeaderBanner from "../HeaderBanner";
import DeleteArticle from "../DeleteArticle";
import Footer from "../Footer";

class DeleteArticlePage extends React.Component {
  render() {
    return (
      <div>
        <HeaderBanner />
        <DeleteArticle />
        <Footer />
      </div>
    );
  }
}

export default DeleteArticlePage;
