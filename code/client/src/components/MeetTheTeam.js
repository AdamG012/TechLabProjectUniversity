import React from "react";
import PersonCard from "./PersonCard";

const teamMembers = [
  {
    name: "Jon Doe",
    linkedInURL: "www.linkedin.com",
    text: "I’m a paragraph. Double click me or click Edit Text, it's easy."
  },
  {
    name: "Jane Doe",
    linkedInURL: "www.linkedin.com",
    text: "I’m a paragraph. Double click me or click Edit Text, it's easy."
  },
  {
    name: "James Doe",
    linkedInURL: "www.linkedin.com",
    text: "I’m a paragraph. Double click me or click Edit Text, it's easy."
  }
];

let renderContent = () => {
  return teamMembers.map(member => {
    return (
      <PersonCard
        name={member.name}
        link={member.linkedInURL}
        text={member.text}
      />
    );
  });
};

const MeetTheTeam = () => {
  return (
    <div className="meet">
      <div className="meet__row">
        <div>
          <h3>Meet The Team</h3>
          <hr></hr>
        </div>
      </div>
      <div className="meet__row">{renderContent()}</div>
    </div>
  );
};

export default MeetTheTeam;
