import React from "react";
import { Link } from "react-router-dom";

class AdminOptions extends React.Component {
  renderListItems = () => {
    const listItems = [
      { name: "Create Article", link: "/admin/article/create" },
      { name: "Edit Article", link: "/admin/article/edit" },
      { name: "Delete Article", link: "/admin/article/delete" },
      { name: "Log out", link: "/admin/logout" }
    ];

    return listItems.map(item => {
      return (
        <Link to={item.link} key={item.link}>
          {item.name}
        </Link>
      );
    });
  };

  render() {
    return (
      <div className="admin-options">
        <div>
          <h1>Admin Options</h1>
        </div>
        <div>
          <ul className="admin-options__list">{this.renderListItems()}</ul>
        </div>
      </div>
    );
  }
}

export default AdminOptions;
