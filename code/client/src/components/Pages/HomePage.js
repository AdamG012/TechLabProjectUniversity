import React from "react";

import HeaderBanner from "../HeaderBanner";
import ArticlesContainer from "../../containers/ArticlesContainer";
import HeroBanner from "../HeroBanner";
import ContactForm from "../ContactForm";
import SideBannerContainer from "../../containers/SideBannerContainer";
import Map from "../Map";
import Footer from "../Footer";
import Search from "../Search";
import ArticleFilter from "../ArticleFilter";

const HomePage = () => {
  const contactFormRef = React.createRef();
  return (
    <div className="page-container">
      <HeaderBanner contactRef={contactFormRef} />
      <HeroBanner />
      <div className="homepage__content">
        <div className="homepage__content-leftColumn">
          <div className="post-filter-and-search">
            <ArticleFilter />
            <Search />
          </div>
          <ArticlesContainer />
        </div>
        <div className="homepage__content-rightColumn">
          <SideBannerContainer />
        </div>
      </div>
      <div className="homepage__contact">
        <ContactForm ref={contactFormRef} />
        <div>
          <Map />
        </div>
      </div>
      <div>
        <Footer />
      </div>
    </div>
  );
};

export default HomePage;
