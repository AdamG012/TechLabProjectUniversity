import React from 'react';
import HeaderBanner from '../HeaderBanner';
import EditArticle from '../EditArticle';
import Footer from '../Footer';

class EditArticlePage extends React.Component {

  componentDidMount() {
    
  }

  render() {
    return (
      <HeaderBanner />
      <EditArticle />
      <Footer />
    )
  }
}