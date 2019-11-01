import React from "react";
import Article from "../components/Article";
import { API_URL } from "../config.json";

class SingleArticleContainer extends React.Component {
  state = {
    title: "",
    author: "",
    date: "",
    timeToRead: "",
    imageURL: "",
    tags: [],
    content: "<p>This is the content of my article</p>"
  };
  async componentDidMount() {
    const { articleId } = this.props;
    // API call to retrieve article data
    const res = await fetch(`${API_URL}/articles/${articleId}`);
    const data = await res.json();
    if (data.success === "false") {
      window.alert("Article data could not be retrieved");
      return;
    }
    const { article } = data;
    this.setState({
      title: article.title,
      author: article.author,
      date: article.date,
      imageURL: article.image,
      tags: article.tags,
      timeToRead: article.time_to_read,
      content: article.content
    });
  }

  render() {
    console.log("ARTICLE CONTAINER CONTENT: ", this.state);
    const {
      title,
      author,
      date,
      imageURL,
      tags,
      timeToRead,
      content
    } = this.state;
    return (
      <Article
        title={title}
        author={author}
        date={date}
        imageURL={imageURL}
        tags={tags}
        timeToRead={timeToRead}
        content={content}
      />
    );
  }
}

export default SingleArticleContainer;
