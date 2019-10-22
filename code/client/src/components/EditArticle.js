import React from 'react';
import HeaderBanner from "../HeaderBanner";
import Footer from "../Footer";
import { API_URL } from '../../config.json';

class EditArticle extends React.Component {
  state = {
    articleBeingEdited: props.match.params.id,
    // TODO: need same state as createArticle Page
  }

  componentDidMount() {
    this.loadArticleData();
  }

  loadArticleData = async (id) => {
    const response = await fetch(`${API_URL}/articles/${articleBeingEdited}`);
    const data = await response.json();
    this.setState(data); // TODO: check this part works, may need to be more explicir
  }

  render() {
    return (

    )
  }
}