import React from "react";
import { shallow, mount } from "enzyme";

import SocialBanner from "../components/SocialBanner";
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
  let shallowRender;
  beforeEach(() => {
    shallowRender = shallow(<SocialBanner data={socialBannerMockData} />);
  });
  it("Renders the correct number of social media icons", () => {});
});
