import React from "react";
import HeaderBanner from "../HeaderBanner";
import ContactForm from "../ContactForm";
import Footer from "../Footer";

class ContactPage extends React.Component {
  render() {
    return (
      <>
        <HeaderBanner />
        <ContactForm />
        <Footer />
      </>
    );
  }
}

export default ContactPage;
