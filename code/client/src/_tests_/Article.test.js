import React from "react";
import { mount } from "enzyme";

import Article from "../components/Article";

let wrapped;

describe("AdminOptions Component", () => {
  beforeEach(() => {
    wrapped = mount(<Article content="<h1>Hello World</h1>" />);
  });

  afterEach(() => {
    wrapped.unmount();
  });

  it("Contains the correct elements", () => {
    expect(wrapped.find("div").length).toEqual(2);
    // expect(wrapped.find("h1").length).toEqual(1);
    // expect(wrapped.find("ul").length).toEqual(1);
  });

  // it("Elements have correct classNames", () => {
  //   expect(wrapped.find(".admin-options").length).toEqual(1);
  //   expect(wrapped.find(".admin-options__list").length).toEqual(1);
  //   expect(wrapped.find(".admin-options__list-item").length).toEqual(12);
  // });

  // it("Contains the correct elements", () => {
  //   expect(wrapped.find("div").length).toEqual(3);
  //   expect(wrapped.find("h1").length).toEqual(1);
  //   expect(wrapped.find(".admin-options__list").length).toEqual(1);
  //   expect(wrapped.find(<Link />).length).toEqual(4);
  // });

  // it("Elements have correct classNames", () => {
  //   expect(wrapped.find(".admin-options").length).toEqual(1);
  //   expect(wrapped.find(".article-snapshot__img-container").length).toEqual(1);
  //   expect(wrapped.find(".article-snapshot__img").length).toEqual(1);
  //   expect(wrapped.find(".article-snapshot__content-container").length).toEqual(
  //     1
  //   );
  //   expect(wrapped.find(".article-snapshot__heading").length).toEqual(1);
  //   expect(wrapped.find(".article-snapshot__text").length).toEqual(1);
  // });
});
