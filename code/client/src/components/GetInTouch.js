import React from "react";
import { Redirect } from "react-router-dom";

const HEADER_OFFSET = 80;

class GetInTouch extends React.Component {
  state = {
    isRedirect: false
  };

  // if (props.contactRef === undefined) {
  handleClick = () => {
    if (this.props.contactRef) {
      const contactFormReference = this.props.contactRef;
      window.scrollTo(
        0,
        contactFormReference.current.contactFormRef.current.offsetTop -
          HEADER_OFFSET
      );
      contactFormReference.current.contactFormRef.current.children[1].elements[0].focus();
    } else {
      this.setState({ isRedirect: true });
    }
  };

  render() {
    if (this.state.isRedirect) {
      return <Redirect to="/contact" />;
    } else {
      return (
        <div className="get-in-touch" onClick={this.handleClick}>
          <p className="get-in-touch__text">Get In Touch</p>
        </div>
      );
    }
  }
}

export default GetInTouch;
