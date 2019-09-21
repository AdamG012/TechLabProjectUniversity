import React from "react";
import { shallow, mount } from "enzyme";

import ArticleSnapshot from "../components/ArticleSnapshot";

let fullRender;
let shallowRender;

describe("ArticleSnapshot Component", () => {
  beforeEach(() => {
    fullRender = mount(
      <ArticleSnapshot
        title="Test Title"
        content="Sample Content"
        image="src/img/dummyplaceholder.jpg"
      />
    );
    shallowRender = mount(
      <ArticleSnapshot
        title="Test Title"
        content="Sample Content"
        image="src/img/dummyplaceholder.jpg"
      />
    );
  });

  afterEach(() => {
    fullRender.unmount();
    shallowRender.unmount();
  });

  it("Correctly Receives Props", () => {
    expect(fullRender.props().title).toBe("Test Title");
    expect(fullRender.props().content).toBe("Sample Content");
    expect(fullRender.props().image).toBe("src/img/dummyplaceholder.jpg");
  });

  it("Contains the correct elements", () => {
    expect(shallowRender.find("div").length).toEqual(3);
    expect(shallowRender.find("h6").length).toEqual(1);
    expect(shallowRender.find("p").length).toEqual(1);
    expect(shallowRender.find("img").length).toEqual(1);
  });

  it("Elements have correct classNames", () => {
    expect(shallowRender.find(".article-snapshot").length).toEqual(1);
    expect(
      shallowRender.find(".article-snapshot__img-container").length
    ).toEqual(1);
    expect(shallowRender.find(".article-snapshot__img").length).toEqual(1);
    expect(
      shallowRender.find(".article-snapshot__content-container").length
    ).toEqual(1);
    expect(shallowRender.find(".article-snapshot__heading").length).toEqual(1);
    expect(shallowRender.find(".article-snapshot__text").length).toEqual(1);
  });
});
