import React, { Component } from "react";
import CKEditor from "@ckeditor/ckeditor5-react";
import ClassicEditor from "@ckeditor/ckeditor5-build-classic";
import Button from "./Button";
import { API_URL } from "../config.json";

class CreateArticle extends Component {
  state = {
    title: "", // add input for this
    author: "",
    abstract: "",
    articleImage: "", // url to image for article
    currentContent: ""
  };

  componentDidUpdate() {
    console.log(this.state.currentContent);
  }

  handleInputChange = e => {
    this.setState({ [e.target.name]: e.target.value });
  };

  handleSubmit = async () => {
    console.log(this.state);
    console.log("making call");
    let response;
    try {
      // https://jsonplaceholder.typicode.com/posts/1
      //${API_URL}/admin/article-new
      response = await fetch(`${API_URL}/admin/article-new`, {
        method: "POST"
      });
      const data = await response.json();
      console.log(data);
    } catch (e) {
      console.log(e);
    }
    // TODO: finish this method once API is fixed and working
  };

  render() {
    return (
      <div className="App">
        <label for="title">Article Name</label>
        <input
          name="title"
          type="text"
          value={this.state.title}
          onChange={this.handleInputChange}
        ></input>
        <label for="author">Author</label>
        <input
          name="author"
          type="text"
          value={this.state.author}
          onChange={this.handleInputChange}
        ></input>
        <label for="abstract">Abstract</label>
        <textarea
          name="abstract"
          type="text"
          value={this.state.abstract}
          onChange={this.handleInputChange}
        ></textarea>

        <h2>Create the article content below</h2>
        <CKEditor
          config={{
            toolbar: [
              "heading",
              "|",
              "bold",
              "italic",
              "link",
              "bulletedList",
              "numberedList",
              "blockQuote"
            ],
            heading: {
              options: [
                {
                  model: "paragraph",
                  title: "Paragraphhhh",
                  class: "ck-heading_paragraph",
                  viewClass: "ck-heading_paragraph"
                },
                {
                  model: "heading1",
                  view: "h1",
                  title: "Heading 1",
                  class: "ck-heading_heading1",
                  viewClass: "ck-heading_heading1"
                },
                {
                  model: "heading2",
                  view: "h2",
                  title: "Heading 2",
                  class: "ck-heading_heading2"
                }
              ]
            }
          }}
          editor={ClassicEditor}
          data="Create an Article for USYD Techlab Trends!!"
          onInit={editor => {
            // You can store the "editor" and use when it is needed.
            console.log("Editor is ready to use!", editor);
          }}
          onChange={(event, editor) => {
            const data = editor.getData();
            console.log({ event, editor, data });
            this.setState({ currentContent: data });
          }}
          onBlur={(event, editor) => {
            console.log("Blur.", editor);
          }}
          onFocus={(event, editor) => {
            console.log("Focus.", editor);
          }}
        />
        <Button handleClick={this.handleSubmit} />
      </div>
    );
  }
}

export default CreateArticle;
