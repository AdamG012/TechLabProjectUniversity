import React, { Component } from "react";
import CKEditor from "@ckeditor/ckeditor5-react";
import ClassicEditor from "@ckeditor/ckeditor5-build-classic";
import Cookies from "js-cookie";

import Button from "./Button";
import { API_URL } from "../config.json";
import transport from "../axios";

class CreateArticle extends Component {
  state = {
    title: "", // add input for this
    author: "",
    abstract: "",
    currentContent: "",
    tags: [],
    timeToRead: ""
  };

  fileInputRef = React.createRef();

  componentDidMount() {
    // TODO: retrieve tags to display
    // user should be able to select
    // and have them applied to the article
  }

  componentDidUpdate() {
    // console.log(this.state.currentContent);
  }

  handleInputChange = e => {
    this.setState({ [e.target.name]: e.target.value });
  };

  onImageChange = e => {
    console.log("FILES: ", e.target.files);
  };

  handleSubmit = async () => {
    console.log(this.state);
    // console.log("SELECTED FILE: ", this.fileInputRef.current.files[0]);
    const {
      title,
      author,
      abstract,
      currentContent,
      tags,
      timeToRead
    } = this.state;

    let formData = new FormData();
    formData.append("title", title);
    formData.append("author", author);
    formData.append("abstract", abstract);
    formData.append("image", this.fileInputRef.current.files[0]);
    formData.append("tags", tags);
    formData.append("time_to_read", Number(timeToRead));
    formData.append("body", currentContent);
    const csrf = Cookies.get("csrftoken");

    formData.append("csrfmiddlewaretoken", csrf);
    transport.post(`${API_URL}/admin/article-new`, formData).then(res => {
      console.log(res);
    });
    window.alert("ARTICLE SUCCESSFULLY CREATED");
    this.setState({
      title: "",
      author: "",
      abstract: "",
      image: "",
      tags: [],
      currentContent: ""
    });
  };

  render() {
    return (
      <div className="App">
        <label htmlFor="title">Article Name</label>
        <input
          name="title"
          type="text"
          value={this.state.title}
          onChange={this.handleInputChange}
        ></input>
        <label htmlFor="author">Author</label>
        <input
          name="author"
          type="text"
          value={this.state.author}
          onChange={this.handleInputChange}
        ></input>
        <label htmlFor="timeToRead">Time To Read</label>
        <input
          name="timeToRead"
          type="text"
          value={this.state.timeToRead}
          onChange={this.handleInputChange}
        ></input>
        <label htmlFor="image">Upload Image</label>
        <input name="image" type="file" ref={this.fileInputRef} />
        <label htmlFor="abstract">Abstract</label>
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
          data={this.state.currentContent}
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
