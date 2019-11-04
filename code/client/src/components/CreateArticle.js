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
    tags: "",
    timeToRead: ""
  };

  fileInputRef = React.createRef();

  componentDidMount() {
    // TODO: retrieve tags to display
    // user should be able to select
    // and have them applied to the article
  }

  handleInputChange = e => {
    this.setState({ [e.target.name]: e.target.value });
  };

  handleSubmit = async () => {
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
    // formData.append("tags", tagArray);
    formData.append("tags", tags);
    formData.append("time_to_read", Number(timeToRead));
    formData.append("body", currentContent);
    const csrf = Cookies.get("csrftoken");

    formData.append("csrfmiddlewaretoken", csrf);
    const res = await transport.post(`${API_URL}/admin/article-new`, formData);
    if (res.data.success === "true") {
      window.alert("Article Successfully Created");
      this.setState({
        title: "",
        author: "",
        abstract: "",
        image: "",
        tags: "",
        currentContent: ""
      });
    } else {
      window.alert("Article couldn't be created at this time");
    }
  };

  render() {
    return (
      <div className="create-article">
        <label className="create-article__label" htmlFor="title">
          Article Name
        </label>
        <input
          className="create-article__input"
          name="title"
          type="text"
          value={this.state.title}
          onChange={this.handleInputChange}
        ></input>
        <label className="create-article__label" htmlFor="author">
          Author
        </label>
        <input
          className="create-article__input"
          name="author"
          type="text"
          value={this.state.author}
          onChange={this.handleInputChange}
        ></input>
        <label className="create-article__label" htmlFor="timeToRead">
          Time To Read
        </label>
        <input
          className="create-article__input"
          name="timeToRead"
          type="text"
          value={this.state.timeToRead}
          onChange={this.handleInputChange}
        ></input>
        <label className="create-article__label" htmlFor="image">
          Upload Image
        </label>
        <input
          className="create-article__input"
          name="image"
          type="file"
          ref={this.fileInputRef}
        />
        <label className="create-article__label" htmlFor="abstract">
          Abstract
        </label>
        <textarea
          className="create-article__input"
          name="abstract"
          type="text"
          value={this.state.abstract}
          onChange={this.handleInputChange}
        ></textarea>

        <h2>Create the article content below</h2>
        <CKEditor
          editor={ClassicEditor}
          data={this.state.currentContent}
          onInit={editor => {
            // You can store the "editor" and use when it is needed.
          }}
          onChange={(event, editor) => {
            const data = editor.getData();
            this.setState({ currentContent: data });
          }}
          onBlur={(event, editor) => {}}
          onFocus={(event, editor) => {}}
        />
        <div className="create-article__button">
          <Button text="Add Article" handleClick={this.handleSubmit} />
        </div>
      </div>
    );
  }
}

export default CreateArticle;
