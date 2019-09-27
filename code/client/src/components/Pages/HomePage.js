import React from "react";

import HeaderBanner from "../HeaderBanner";
import ArticlesContainer from "../../containers/ArticlesContainer";
import HeroBanner from "../HeroBanner";
import ContactForm from "../ContactForm";
import SideBannerContainer from "../../containers/SideBannerContainer";
import Map from "../Map";

const HomePage = () => {
  const contactFormRef = React.createRef();
  return (
    <div className="page-container">
      <HeaderBanner contactRef={contactFormRef} />
      <HeroBanner />
      <div className="main-content">
        <ArticlesContainer />
        <SideBannerContainer />
      </div>
      <ContactForm ref={contactFormRef} />
      <Map />
    </div>
  );
};

export default HomePage;
