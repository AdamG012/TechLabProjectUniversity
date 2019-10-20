import React from "react";

class Login extends React.Component {
  state = {
    username: "",
    password: ""
  };

  onUsernameChange = e => {
    this.setState({
      username: e.target.value
    });
  };

  onPasswordChange = e => {
    this.setState({
      password: e.target.value
    });
  };

  handleSubmit = async e => {
    e.preventDefault();
    console.log(process.env);
    // const response = await fetch(``)
    console.log("submitted login form");
    // make api call to /login endpoint
    // wait for response
    // on successful response change login state to true
    // on failure show error message
  };

  render() {
    return (
      <div className="login">
        <div className="login__heading">
          <h4>Admin Log In</h4>
        </div>
        <form className="login__form">
          <label for="username">Username</label>
          <input
            className="login__input"
            value={this.state.username}
            type="text"
            name="username"
            onChange={this.onUsernameChange}
          ></input>
          <label for="password">Password</label>
          <input
            className="login__input"
            value={this.state.password}
            type="password"
            name="password"
            onChange={this.onPasswordChange}
          ></input>
          <button className="login__button" onClick={this.handleSubmit}>
            Log in
          </button>
        </form>
      </div>
    );
  }
}

export default Login;
