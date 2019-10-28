import React from "react";
import PersonCard from "./PersonCard";
import { teamMembers } from "../master.json";
import Col from "react-bootstrap/Col";
import Row from "react-bootstrap/Row";

let renderContent = () => {
  return teamMembers.map(member => {
    return (
        <Row>
        <Col>
          <PersonCard
            name={member.name}
            link={member.linkedInURL}
            text={member.text}
            img={member.img}
          />
        </Col>
        </Row>
    );
  });
};

const MeetTheTeam = () => {
  return (
    <div className="meet">
      <div className="meet__row">
        <div className="meet__heading">
          <h3 className="h3">Meet The Team</h3>
          <hr className="hr"/>
        </div>
      </div>
      <div className="meet__row">
          <div className="meet__cards">{renderContent()}</div>
    </div>
    </div>
  );
};

export default MeetTheTeam;
