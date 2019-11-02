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
    title: "",
    author: "",
    image: "",
    abstract: "",
    currentContent: ""
  };

  fileInputRef = React.createRef();

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
    if (this.fileInputRef.current.file) {
      formData.append("image", this.fileInputRef.current.files[0]);
    }

    formData.append("tags", tags);
    formData.append("time_to_read", Number(timeToRead));
    formData.append("body", currentContent);
    const csrf = Cookies.get("csrftoken");

    formData.append("csrfmiddlewaretoken", csrf);
    transport.post(`${API_URL}/admin/article-edit`, formData).then(res => {
      console.log(res);
    });
    window.alert("ARTICLE SUCCESSFULLY EDITED");
    this.setState({
      title: "",
      author: "",
      abstract: "",
      image: "",
      tags: [],
      currentContent: ""
    });
  };

  handleInputChange = e => {
    this.setState({ [e.target.name]: e.target.value });
  };

  handleChange = e => {
    this.setState({ articleToEdit: e.target.value });
  };

  loadArticleData = async id => {
    const response = await fetch(
      `${API_URL}/articles/${this.state.articleToEdit}`
    );
    const data = await response.json();
    if (!data.success) {
      window.alert("Couldn't load article data");
    }
    const { article } = data;
    this.setState({
      title: article.title,
      author: article.author,
      abstract: article.abstract,
      currentContent: article.content
    });

    // get abstract data
    const abstractData = await transport.get(
      `${API_URL}/abstract/${this.state.articleToEdit}`
    );
    // const d = await abstractData.json();
    console.log(abstractData.data.article.abstract);
    this.setState({ abstract: abstractData.data.article.abstract });
  };

  render() {
    return (
      <div className="App">
        <h2>Edit Article</h2>
        <label htmlFor="articleToEdit">Enter id of article to edit</label>
        <input
          name="articleToEdit"
          type="text"
          value={this.state.articleToEdit}
          onChange={this.handleChange}
        ></input>
        <button onClick={this.loadArticleData}>Get Article Data</button>
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
        <label htmlFor="image">
          Upload Image (if no image is provided, the old image will be used)
        </label>
        <input name="image" type="file" ref={this.fileInputRef} />
        <label htmlFor="abstract">Abstract</label>
        <textarea
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

export default EditArticle;
