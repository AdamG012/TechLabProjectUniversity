import React from "react";
import { shallow, mount } from "enzyme";
import SocialMedia from "../components/SocialMedia";

describe("SocialMedia Component", () => {
  let svgSourceMock = () => "hello";
  let shallow;
  beforeEach(() => {
    shallow = mount(
      <SocialMedia alt="test" url="www.google.com" svgSource={svgSourceMock} />
    );
  });

  it("Receives props", () => {
    expect(shallow.props().alt).toBe("test");
    expect(shallow.props().url).toBe("www.google.com");
    expect(shallow.props().svgSource).toBe(svgSourceMock);
  });

  it("Renders correct elements", () => {
    expect(shallow.find("div").length).toEqual(1);
    expect(shallow.find("a").length).toEqual(1);
  });
});
