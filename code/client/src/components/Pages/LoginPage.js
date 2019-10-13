import React from "react";
import HeaderBanner from "../HeaderBanner";
import Login from "../Login";
import Footer from "../Footer";

class LoginPage extends React.Component {
  render() {
    return (
      <>
        <HeaderBanner />
        <Login />
        <Footer />
      </>
    );
  }
}

export default LoginPage;
