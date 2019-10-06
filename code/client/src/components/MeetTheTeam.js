import React from "react";
import PersonCard from "./PersonCard";

const teamMembers = [
  {
    name: "Jon Doe",
    linkedInURL: "www.linkedin.com",
    text: "I’m a paragraph. Double click me or click Edit Text, it's easy.",
    img: "person1.webp"
  },
  {
    name: "Jane Doe",
    linkedInURL: "www.linkedin.com",
    text: "I’m a paragraph. Double click me or click Edit Text, it's easy.",
    img: "person2.webp"
  },
  {
    name: "James Doe",
    linkedInURL: "www.linkedin.com",
    text: "I’m a paragraph. Double click me or click Edit Text, it's easy.",
    img: "person3.webp"
  }
];

let renderContent = () => {
  return teamMembers.map(member => {
    return (
      <PersonCard
        name={member.name}
        link={member.linkedInURL}
        text={member.text}
        img={member.img}
      />
    );
  });
};

const MeetTheTeam = () => {
  return (
    <div className="meet">
      <div className="meet__row">
        <div className="meet__heading">
          <h3 className="h3">Meet The Team</h3>
          <hr className="hr"></hr>
        </div>
      </div>
      <div className="meet__row">
        <div className="meet__cards">{renderContent()}</div>
      </div>
    </div>
  );
};

export default MeetTheTeam;
