import React from "react";

import HeaderBanner from "../HeaderBanner";
import ArticlesContainer from "../../containers/ArticlesContainer";
import HeroBanner from "../HeroBanner";
import ContactForm from "../ContactForm";
import SideBannerContainer from "../../containers/SideBannerContainer";
import Map from "../Map";
import Footer from "../Footer";

const HomePage = () => {
  const contactFormRef = React.createRef();
  return (
    <div className="page-container">
      <HeaderBanner contactRef={contactFormRef} />
      <HeroBanner />
      <div className="homepage__content">
        <ArticlesContainer />
        <SideBannerContainer />
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
