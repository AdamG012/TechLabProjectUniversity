import React from "react";
import { Link } from "react-router-dom";

class FourOhFour extends React.Component {
  goBack = () => {
    this.props.history.goBack();
  };

  render() {
    return (
      <div>
        <h4>Page not found</h4>
        <button class="btn">
          <Link to="/">Home</Link>
        </button>
        <button onClick={this.goBack}>
          <p>Go Back</p>
        </button>
      </div>
    );
  }
}

export default FourOhFour;
