import React from "react";
import axios from "axios";
import { UNSPLASH_ACCESS_KEY } from "../utils/keys";

import ArticleSnapshot from "../components/ArticleSnapshot";

class ArticlesContainer extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      images: [],
      currentPage: 0
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
          per_page: 3
        }
      })
      .then(res => {
        this.setState({ images: res.data.results, currentPage: 1 });
      })
      .catch(err => console.log(err));
  }

  getNextPage = () => {
    console.log("getNextPage called");
    axios
      .get("https://api.unsplash.com/search/photos", {
        headers: {
          Authorization: "Client-ID " + UNSPLASH_ACCESS_KEY
        },
        params: {
          query: "technology",
          page: this.state.currentPage + 1,
          per_page: 3
        }
      })
      .then(res => {
        console.log("ARRAYS: ", [...this.state.images, ...res.data.results]);
        this.setState({
          images: [...this.state.images, ...res.data.results], // check this
          currentPage: this.state.currentPage + 1
        });
        console.log("STATE: ", this.state);
      })
      .catch(err => console.log(err));
  };

  renderContent = () => {
    const { images } = this.state;
    return images.map(image => {
      console.log(image);
      return (
        <ArticleSnapshot
          key={image.urls.full}
          imageURL={image.urls.full}
          title="Example Article"
          content="This is your blog post. To really engage your site visitors we suggest you blog about subjects that are related to your site or business. Blogging is really great for SEO, so we recommend including keywords that relate to your services, products or industry within your posts"
        />
      );
    });
  };

  render() {
    return (
      <div className="articles-container">
        <div>{this.renderContent()}</div>
        <div>
          <button onClick={this.getNextPage}>Load More</button>
        </div>
      </div>
    );
  }
}

export default ArticlesContainer;
