import React from "react";

class DeleteArticle extends React.Component {
  render() {
    return (
      <>
        <label htmlFor="to-delete">Enter Article ID to delete</label>
        <input name="to-delete" type="text" />
      </>
    );
  }
}

export default DeleteArticle;
