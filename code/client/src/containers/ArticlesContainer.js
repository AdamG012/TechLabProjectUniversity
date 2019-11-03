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
    // get the article ids for the first page
    const articleIds = await fetch(
      `${API_URL}/latest-articles/${this.state.currentPage}`,
      {
        method: "GET"
      }
    );
    const data = await articleIds.json();

    data.latest.map(async articleId => {
      const articleData = await fetch(`${API_URL}/abstract/${articleId}`, {
        method: "GET"
      });

      const article = await articleData.json();
      const articleToAdd = article.article;
      article.article.id = articleId;
      this.setState({
        articles: [...this.state.articles, articleToAdd]
      });
    });
    this.setState({ currentPage: this.state.currentPage + 1 });
  }

  getNextPage = async () => {
    const { currentPage } = this.state;
    const response = await fetch(`${API_URL}/latest-articles/${currentPage}`);
    const data = await response.json();
    console.log(data);
    if (data.success === "false") {
      this.setState({ articlesRemain: false });
      window.alert("No more articles available at this time");
      return;
    }
    data.latest.map(async articleId => {
      const articleData = await fetch(`${API_URL}/abstract/${articleId}`, {
        method: "GET"
      });

      const article = await articleData.json();
      const articleToAdd = article.article;
      this.setState({
        articles: [...this.state.articles, articleToAdd]
      });
    });
    this.setState({ currentPage: currentPage + 1 });
  };

  renderContent = () => {
    const { articles } = this.state;
    return articles.map(article => {
      console.log(article);
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
          content={article.abstract}
        />
      );
    });
  };

  render() {
    return (
      <div className="articles-container">
        {this.renderContent()}
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
