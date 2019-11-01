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
    articleImageData: "", // url to image for article
    currentContent: "",
    tags: []
  };

  componentDidMount() {
    // TODO: retrieve tags to display
    // user should be able to select
    // and have them applied to the article
  }

  componentDidUpdate() {
    console.log(this.state.currentContent);
  }

  handleInputChange = e => {
    this.setState({ [e.target.name]: e.target.value });
  };

  onImageChange = e => {
    console.log(e.target.files);
  };

  handleSubmit = async () => {
    console.log(this.state);
    const {
      title,
      author,
      abstract,
      articleImage,
      currentContent,
      tags
    } = this.state;
    const bodyData = {
      title: title,
      author: author,
      abstract: abstract,
      image: articleImage,
      tags: tags,
      content: currentContent
    };

    let formData = new FormData();
    formData.append("title", title);
    formData.append("author", author);
    formData.append("abstract", abstract);
    formData.append("image", articleImage);
    formData.append("tags", tags);
    formData.append("content", currentContent);
    const csrf = Cookies.get("csrftoken");

    formData.append("csrfmiddlewaretoken", csrf);
    let response;
    transport.post(`${API_URL}/admin/article-new`, formData).then(res => {
      console.log(res);
    });
    // try {
    //   response = await fetch(`${API_URL}/admin/article-new`, {
    //     method: "POST",
    //     credentials: "same-origin",
    //     headers: {
    //       "X-CSRFToken": csrf
    //     },
    //     body: formData
    //   });
    //   console.log(response);
    window.alert("ARTICLE SUCCESSFULLY CREATED");
    this.setState({
      title: "",
      author: "",
      abstract: "",
      image: "",
      tags: [],
      currentContent: ""
    });
    // } catch (e) {
    //   console.log(e);
    // }
    // TODO: finish this method once API is fixed and working
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
        <label htmlFor="image">Upload Image</label>
        <input name="image" type="file" onChange={this.onImageChange} />
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
