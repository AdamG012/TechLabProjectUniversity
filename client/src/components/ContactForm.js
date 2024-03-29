import React from "react";
import transport from "../axios";

class ContactForm extends React.Component {
  constructor(props) {
    super(props);
    this.contactFormRef = React.createRef();
    this.state = {
      name: "",
      email: "",
      subject: "",
      content: ""
    };
  }
  handleFormSubmit = async e => {
    e.preventDefault();
    const { name, email, subject, content } = this.state;
    const res = await transport.post("/contact", {
      name: name,
      subject: subject,
      email: email,
      content: content
    });
    console.log("RES: ", res);
    const { data } = res;
    if (data.success) {
      window.alert("Successfully submitted contact form");
    } else {
      window.alert("There was an error submitting your form, please try again");
    }
    this.setState({ name: "", email: "", subject: "", content: "" });
  };

  handleNameChange = e => {
    this.setState({ name: e.target.value });
  };

  handleEmailChange = e => {
    this.setState({ email: e.target.value });
  };

  handleSubjectChange = e => {
    this.setState({ subject: e.target.value });
  };

  handleContentChange = e => {
    this.setState({ content: e.target.value });
  };

  render() {
    const { name, email, subject, content } = this.state;
    return (
      <div ref={this.contactFormRef} className="contact-form" id="contact-form">
        <h4 className="h4">Contact</h4>
        <form
          id="contact-form"
          className="contact-form__form"
          onSubmit={this.handleFormSubmit}
        >
          <input
            onChange={this.handleNameChange}
            className="contact-form__input contact-form__input--small"
            name="name"
            type="text"
            placeholder="Name"
            value={name}
          />
          <input
            onChange={this.handleEmailChange}
            className="contact-form__input contact-form__input--small"
            name="email"
            type="text"
            placeholder="Email"
            value={email}
          />
          <input
            onChange={this.handleSubjectChange}
            className="contact-form__input contact-form__input--small"
            name="subject"
            type="text"
            placeholder="Subject"
            value={subject}
          />
          <textarea
            form="contact-form"
            onChange={this.handleContentChange}
            className="contact-form__input contact-form__input--large"
            name="content"
            rows="8"
            placeholder="Type your message here..."
            value={content}
          />
          <button className="btn btn--black contact-form__submit" type="submit">
            Submit
          </button>
        </form>
      </div>
    );
  }
}

export default ContactForm;
