import React from "react";
import { API_URL } from "../config.json";
import CKEditor from "@ckeditor/ckeditor5-react";
import ClassicEditor from "@ckeditor/ckeditor5-build-classic";
import Button from "./Button";

class EditArticle extends React.Component {
  state = {
    articleBeingEdited: this.props.match.params.id
    // TODO: need same state as createArticle Page
  };

  componentDidMount() {
    this.loadArticleData();
  }

  loadArticleData = async id => {
    const response = await fetch(
      `${API_URL}/articles/${this.state.articleBeingEdited}`
    );
    const data = await response.json();
    this.setState(data); // TODO: check this part works, may need to be more explicir
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

export default EditArticle;
