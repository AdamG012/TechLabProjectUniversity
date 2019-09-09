import React from "react";
import { mount } from "enzyme";
import { BrowserRouter } from "react-router-dom";

import HomePage from "../components/Pages/HomePage";
import HeaderBanner from "../components/HeaderBanner";
import ArticlesContainer from "../containers/ArticlesContainer";

describe("HomePage Component", () => {
  let component;
  beforeEach(() => {
    component = mount(
      <BrowserRouter>
        <HomePage />
      </BrowserRouter>
    );
  });

  afterEach(() => {
    // settimeout ensures state update has finished before ending the test (this was causing an error to be thrown by Jest)
    setTimeout(() => {
      component.unmount();
    }, 200);
  });

  it("Renders a HeaderBanner", () => {
    expect(component.find(HeaderBanner).length).toEqual(1);
  });

  it("Renders an ArticlesContainer", () => {
    expect(component.find(ArticlesContainer).length).toEqual(1);
  });
});
