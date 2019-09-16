import React from "react";
import { shallow, mount } from "enzyme";
import AboutPage from "../components/Pages/AboutPage";

describe("AboutPage Component", () => {
  let component;
  beforeEach(() => {
    component = shallow(<AboutPage />);
  });

  afterEach(() => {
    setTimeout(() => {}, 100);
  });

  it("Dummy Test", () => {
    expect(true).toEqual(true);
  });
});
