import React from "react";
import { API_URL } from "../config.json";

import ArticleSnapshot from "../components/ArticleSnapshot";
import Button from "../components/Button";

class ArticlesContainer extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      currentPage: 1,
      articles: [],
      articlesRemain: true // flag showing whether more articles can be loaded
    };
  }

  componentDidUpdate() {
    console.log(this.state);
  }

  async componentDidMount() {
    const response = await fetch(`${API_URL}/articles`, {
      method: "GET"
    });
    const data = await response.json();
    this.setState({ articles: data });
  }

  getNextPage = async () => {
    const { currentPage } = this.state;
    console.log("CURRENT PAGE: ", currentPage);
    const response = await fetch(`${API_URL}/articles?page=${currentPage + 1}`);
    const data = await response.json();
    if (data.length === 0) {
      this.setState({ articlesRemain: false });
      window.alert("No more articles available at this time");
    }
    this.setState({
      articles: [...this.state.articles, ...data],
      currentPage: currentPage + 1
    });
  };

  renderContent = () => {
    const { articles } = this.state;
    return articles.map(article => {
      return (
        <ArticleSnapshot
          id={article.id}
          key={article.id}
          author={article.author}
          abstract={article.abstract}
          imageURL={article.image}
          title={article.title}
          timeToRead={article.time_to_read}
          tags={article.tags}
          content={article.content}
        />
      );
    });
  };

  render() {
    return (
      <div className="articles-container">
        <div>{this.renderContent()}</div>
        <div>
          <Button
            handleClick={this.getNextPage}
            color="white"
            text="Load More Articles"
          ></Button>
        </div>
      </div>
    );
  }
}

export default ArticlesContainer;
