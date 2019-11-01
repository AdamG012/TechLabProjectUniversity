import React from "react";
import { Route, Redirect } from "react-router-dom";

const ProtectedRoute = ({ isAllowed, ...props }) => {
  if (!isAllowed) {
    window.alert("You must be logged in to view that page");
    return <Redirect to="/login" />;
  } else {
    return <Route {...props} />;
  }
};
export default ProtectedRoute;
