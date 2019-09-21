import React from "react";

const GetInTouch = props => {
  const contactFormReference = props.contactRef;
  return (
    <div
      className="get-in-touch"
      onClick={() => {
        window.scrollTo(
          0,
          contactFormReference.current.contactFormRef.current.offsetTop
        );
      }}
    >
      <p className="get-in-touch__text">Get In Touch</p>
    </div>
  );
};

export default GetInTouch;
