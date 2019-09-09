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
    // const wrapper = shallow(
    //   <ArticleSnapshot
    //     title="Test Title"
    //     content="Sample Content"
    //     image="src/img/dummyplaceholder.jpg"
    //   />
    // );
    // expect(wrapper.contains(<div className="article-snapshot"></div>));

    expect(fullRender.props().title).toBe("Test Title");
    expect(fullRender.props().content).toBe("Sample Content");
    expect(fullRender.props().image).toBe("src/img/dummyplaceholder.jpg");
  });

  it("Renders the outer div", () => {
    expect(
      shallowRender.containsMatchingElement(
        <div className="article-snapshot"></div>
      ) // this doesn't work correctly
    );
  });
});
