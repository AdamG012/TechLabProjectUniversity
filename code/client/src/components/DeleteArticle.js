import React from "react";

import transport from "../axios";

class DeleteArticle extends React.Component {
  state = {
    articleToDelete: ""
  };

  handleChange = e => {
    this.setState({ articleToDelete: e.target.value });
  };

  deleteArticle = async () => {
    const res = await transport.post("/admin/article-remove", {
      id: this.state.articleToDelete
    });
    if (res.data.success === "false") {
      window.alert(
        "Unable to delete the given article, check it exists and try again"
      );
    } else {
      window.alert("Article successfully deleted");
    }
  };
  render() {
    return (
      <>
        <label htmlFor="to-delete">Enter Article ID to delete</label>
        <input
          name="to-delete"
          type="text"
          value={this.state.articleToDelete}
          onChange={this.handleChange}
        />
        <button onClick={this.deleteArticle}>Delete Article</button>
      </>
    );
  }
}

export default DeleteArticle;
