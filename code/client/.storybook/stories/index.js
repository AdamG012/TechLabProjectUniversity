import React from "react";
import { storiesOf } from "@storybook/react";
import SocialBanner from "../../src/components/SocialBanner";
import SocialMedia from "../../src/components/SocialMedia";
import HeaderBanner from "../../src/components/HeaderBanner";
import Search from "../../src/components/Search";
import Navigation from "../../src/components/Navigation";
import ArticleSnapshot from "../../src/components/ArticleSnapshot";
import ArticlesContainer from "../../src/containers/ArticlesContainer";

storiesOf("Test", module)
  .add("Social Banner Component", () => {
    return <SocialBanner />;
  })
  .add("Social Media Single Component", () => {
    return <SocialMedia />;
  })
  .add("Header Component", () => {
    return <HeaderBanner />;
  })
  .add("Search Component", () => {
    return <Search />;
  })
  .add("Navigation Component", () => {
    return <Navigation />;
  })
  .add("Article Snapshot Component", () => {
    return (
      <ArticleSnapshot
        title="Example Article"
        content="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod
    tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim
    veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea
    commodo consequat. Duis aute irure dolor in reprehenderit in voluptate
    velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint
    occaecat cupidatat non proident, sunt in culpa qui officia deserunt
    mollit anim id est laborum."
      />
    );
  })
  .add("Articles Container", () => {
    return <ArticlesContainer />;
  });
