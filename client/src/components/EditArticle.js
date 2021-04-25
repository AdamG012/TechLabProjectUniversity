import React from "react";
import { API_URL } from "../config.json";
import CKEditor from "@ckeditor/ckeditor5-react";
import ClassicEditor from "@ckeditor/ckeditor5-build-classic";
import Button from "./Button";

import Cookies from "js-cookie";
import transport from "../axios";

class EditArticle extends React.Component {
  state = {
    articleToEdit: "",
    articleId: "",
    title: "",
    author: "",
    image: "",
    abstract: "",
    timeToRead: "",
    currentContent: "",
    tags: ""
  };

  fileInputRef = React.createRef();

  handleSubmit = async () => {
    const {
      articleId,
      title,
      author,
      abstract,
      currentContent,
      tags,
      timeToRead
    } = this.state;

    let formData = new FormData();
    formData.append("title", title);
    formData.append("id", articleId);
    formData.append("author", author);
    formData.append("abstract", abstract);
    if (this.fileInputRef.current.file) {
      formData.append("image", this.fileInputRef.current.files[0]);
    }

    formData.append("tags", tags);
    formData.append("time_to_read", Number(timeToRead));
    formData.append("body", currentContent);
    const csrf = Cookies.get("csrftoken");

    formData.append("csrfmiddlewaretoken", csrf);
    const res = await transport.post(`${API_URL}/admin/article-edit`, formData);
    if (res.data.success === "false") {
      window.alert("Unable to edit the article at this time");
      return;
    }
    window.alert("ARTICLE SUCCESSFULLY EDITED");
    this.setState({
      title: "",
      author: "",
      abstract: "",
      image: "",
      tags: "",
      timeToRead: "",
      currentContent: ""
    });
  };

  handleInputChange = e => {
    this.setState({ [e.target.name]: e.target.value });
  };

  handleChange = e => {
    this.setState({ articleToEdit: e.target.value });
  };

  loadArticleData = async () => {
    const response = await fetch(
      `${API_URL}/articles/${this.state.articleToEdit}`
    );
    const data = await response.json();
    if (data.success === "false") {
      window.alert("Couldn't load article data");
      return;
    }
    const { article } = data;
    const tagArray = article.tags;
    const tagString = tagArray.join(",");
    this.setState({
      articleId: this.state.articleToEdit,
      title: article.title,
      author: article.author,
      abstract: article.abstract,
      currentContent: article.content,
      timeToRead: article.time_to_read,
      tags: tagString
    });

    // get abstract data
    const abstractData = await transport.get(
      `${API_URL}/abstract/${this.state.articleToEdit}`
    );
    // const d = await abstractData.json();
    this.setState({ abstract: abstractData.data.article.abstract });
  };

  render() {
    return (
      <div className="edit-article">
        <h2>Edit Article</h2>
        <label className="create-article__label" htmlFor="articleToEdit">
          Enter id of article to edit
        </label>
        <div>
          <input
            className="create-article__input"
            name="articleToEdit"
            type="text"
            value={this.state.articleToEdit}
            onChange={this.handleChange}
          ></input>
          <button onClick={this.loadArticleData}>Get Article Data</button>
        </div>

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
        <label className="create-article__label" htmlFor="tags">
          Tags
        </label>
        <input
          className="create-article__input"
          name="tags"
          type="text"
          value={this.state.tags}
          onChange={this.handleInputChange}
        ></input>
        <label className="create-article__label" htmlFor="image">
          Upload Image (if no image is provided, the old image will be used)
        </label>
        <input name="image" type="file" ref={this.fileInputRef} />
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
        <h2>Edit the article content below</h2>
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
          }}
          onChange={(event, editor) => {
            const data = editor.getData();
            this.setState({ currentContent: data });
          }}
          onBlur={(event, editor) => {}}
          onFocus={(event, editor) => {}}
        />
        <Button handleClick={this.handleSubmit} />
      </div>
    );
  }
}

export default EditArticle;
