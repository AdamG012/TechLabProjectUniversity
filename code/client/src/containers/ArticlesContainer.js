import React from "react";
import axios from "axios";
import { UNSPLASH_ACCESS_KEY } from "../utils/keys";

import ArticleSnapshot from "../components/ArticleSnapshot";

class ArticlesContainer extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      images: []
    };
  }

  componentDidMount() {
    axios
      .get("https://api.unsplash.com/search/photos", {
        headers: {
          Authorization: "Client-ID " + UNSPLASH_ACCESS_KEY
        },
        params: {
          query: "technology",
          page: 1,
          per_page: 10
        }
      })
      .then(res => {
        this.setState({ images: res.data.results });
      });
  }

  renderContent = () => {
    const { images } = this.state;
    return images.map(image => {
      return (
        <ArticleSnapshot
          imageURL={image.urls.full}
          title="Example Article"
          content="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
  tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim
  veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
  commodo consequat. Duis aute irure dolor in reprehenderit in voluptate
  velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint
  occaecat cupidatat non proident, sunt in culpa qui officia deserunt
  mollit anim id est laborum."
        />
      );
    });
  };

  render() {
    return <div className="articles-container">{this.renderContent()}</div>;
  }
}

export default ArticlesContainer;
