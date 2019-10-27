import React from "react";

import HeaderBanner from "../HeaderBanner";
import AdminOptions from "../AdminOptions";
import Footer from "../Footer";

class AdminOptionsPage extends React.Component {
  render() {
    return (
      <>
        <HeaderBanner />
        <AdminOptions />
        <Footer />
      </>
    );
  }
}

export default AdminOptionsPage;
