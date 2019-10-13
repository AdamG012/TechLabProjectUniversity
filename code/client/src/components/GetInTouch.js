import React from "react";

const HEADER_OFFSET = 80;

const GetInTouch = props => {
  const contactFormReference = props.contactRef;
  return (
    <div
      className="get-in-touch"
      onClick={() => {
        window.scrollTo(
          0,
          contactFormReference.current.contactFormRef.current.offsetTop -
            HEADER_OFFSET
        );
      }}
    >
      <p className="get-in-touch__text">Get In Touch</p>
    </div>
  );
};

export default GetInTouch;
