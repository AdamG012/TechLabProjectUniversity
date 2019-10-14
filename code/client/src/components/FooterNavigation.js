import React from "react";
import { Link } from "react-router-dom";

const footerLinks = [
    {
        text: "Home",
        toPath: "/",
        requiresAuth: false
    },
    {
        text: "Meet Us",
        toPath: "/about",
        requiresAuth:false
    },
    {
        text: "Privacy Policy",
        toPath: "https://sydney.edu.au/privacy-statement.html",
        requiresAuth: false
    },
    {
        text: "Admin",
        toPath: "/admin_login",
        requiresAuth: false
    }
];

const renderLinks = linkData => {
    return linkData.map(link => {
        return (
            <li className="navigation__list-item">
                <Link className="navigation__link" to={link.toPath}>
                    {link.text}
                </Link>
            </li>
        );
    });
};

const FooterNavigation = () => {
    return (
        <div className="navigation-container">
            <nav className="navigation">
                <ul className="navigation__list">{renderLinks(footerLinks)}</ul>
            </nav>
        </div>
    );
};

export default FooterNavigation;