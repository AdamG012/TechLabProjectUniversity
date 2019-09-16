import React from "react";

class ContactForm extends React.Component {
  constructor(props) {
    super(props);
    this.contactFormRef = React.createRef();
  }
  handleFormSubmit = e => {
    e.preventDefault();
    console.log("form submitted");
  };

  render() {
    return (
      <div ref={this.contactFormRef} className="contact-form" id="contact-form">
        <h4 className="h4">Contact</h4>
        <form className="contact-form__form" onSubmit={this.handleFormSubmit}>
          <input
            className="contact-form__input contact-form__input--small"
            name="name"
            type="text"
            placeholder="Name"
          />
          <input
            className="contact-form__input contact-form__input--small"
            name="email"
            type="text"
            placeholder="Email"
          />
          <input
            className="contact-form__input contact-form__input--small"
            name="subject"
            type="text"
            placeholder="Subject"
          />
          <textarea
            className="contact-form__input contact-form__input--large"
            name="content"
            rows="8"
            placeholder="Type your message here..."
          />
          <button type="submit">Submit</button>
        </form>
      </div>
    );
  }
}

export default ContactForm;
