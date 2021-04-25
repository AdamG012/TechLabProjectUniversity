import React from "react";
import { mount } from "enzyme";
import { Link, BrowserRouter } from "react-router-dom";

import AdminOptions from "../components/AdminOptions";

let wrapped;

describe("AdminOptions Component", () => {
  beforeEach(() => {
    wrapped = mount(
      <BrowserRouter>
        <AdminOptions />
      </BrowserRouter>
    );
  });

  afterEach(() => {
    wrapped.unmount();
  });

  it("Contains the correct elements", () => {
    expect(wrapped.find("div").length).toEqual(3);
    expect(wrapped.find("h1").length).toEqual(1);
    expect(wrapped.find("ul").length).toEqual(1);
  });

  it("Elements have correct classNames", () => {
    expect(wrapped.find(".admin-options").length).toEqual(1);
    expect(wrapped.find(".admin-options__list").length).toEqual(1);
    expect(wrapped.find(".admin-options__list-item").length).toEqual(12);
  });
});
