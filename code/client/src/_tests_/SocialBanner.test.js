import React from "react";
import { shallow, mount } from "enzyme";

import SocialBanner from "../components/SocialBanner";
import SocialMedia from "../components/SocialMedia";
import { ReactComponent as FacebookLogo } from "../svg/SVG/facebook.svg";
import { ReactComponent as TwitterLogo } from "../svg/SVG/twitter.svg";
import { ReactComponent as YoutubeLogo } from "../svg/SVG/youtube.svg";
let socialBannerMockData = [
  {
    name: "Facebook",
    url: "https://www.facebook.com/usydtechlab/",
    svg: <FacebookLogo />
  },
  {
    name: "Twitter",
    url: "https://twitter.com/usydtechlab?lang=en",
    svg: <TwitterLogo />
  },
  {
    name: "Youtube",
    url: "www.youtube.com",
    svg: <YoutubeLogo />
  }
];

describe("Social Banner Component", () => {
  let wrapped;
  beforeEach(() => {
    wrapped = mount(<SocialBanner data={socialBannerMockData} />);
  });

  it("Renders the correct number of social media components", () => {
    expect(wrapped.find(SocialMedia).length).toEqual(3);
  });

  it("Renders the correct core elements", () => {
    expect(wrapped.find(".social-banner").length).toEqual(1);
    expect(wrapped.find(".social-banner__list").length).toEqual(1);
  });
});
