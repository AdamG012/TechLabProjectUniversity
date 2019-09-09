import React from "react";
import { mount, shallow } from "enzyme";

import ArticlePage from "../components/Pages/ArticlePage";
import ArticlesContainer from "../containers/ArticlesContainer";

describe("ArticlePage Component", () => {
  let component;
  beforeEach(() => {
    component = shallow(<ArticlePage />);
  });

  afterEach(() => {
    component = null;
  });

  it("Renders Single ArticlesContainer", () => {
    expect(component.find(ArticlesContainer).length).toEqual(1);
  });
});
