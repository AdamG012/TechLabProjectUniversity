import React from "react";
import PersonCard from "./PersonCard";
import { teamMembers } from "../master.json";

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
