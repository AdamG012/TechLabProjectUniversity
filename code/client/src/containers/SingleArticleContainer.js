import React from "react";
import Article from "../components/Article";
import { API_URL } from "../config.json";

class SingleArticleContainer extends React.Component {
  state = {
    articleData: {},
    content: "<p>This is the content of my article</p>"
  };
  async componentDidMount() {
    const { articleId } = this.props;
    // API call to retrieve article data
    const res = await fetch(`${API_URL}/articles/${articleId}`);
    const articleData = await res.json();
    this.setState({ articleData });
    if (articleId) {
      // make api call to retrieve data for specific article
      this.setState({
        content: `<h1>This is article ${articleId}</h1>`
      });
    }
  }

  render() {
    console.log(this.state.content);
    return <Article content={this.state.content} />;
  }
}

export default SingleArticleContainer;
