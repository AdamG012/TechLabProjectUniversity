import React from "react";
import { mount } from "enzyme";

import Button from "../components/Button";

let wrapped;

describe("AdminOptions Component", () => {
  beforeEach(() => {
    wrapped = mount(<Button color="black" />);
  });

  afterEach(() => {
    wrapped.unmount();
  });

  it("Dummy test", () => {
    expect(1).toEqual(1);
  });

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
