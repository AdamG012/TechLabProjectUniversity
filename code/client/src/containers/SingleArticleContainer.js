import React from "react";
import Article from "../components/Article";

class SingleArticleContainer extends React.Component {
  state = {
    content: "<p>This is the content of my article</p>"
  };
  componentDidMount() {
    const { articleId } = this.props;
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
