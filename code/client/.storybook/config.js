import { configure } from "@storybook/react";

import "./css/style.css";

function loadStories() {
  require("./stories/index");
}

configure(loadStories, module);
