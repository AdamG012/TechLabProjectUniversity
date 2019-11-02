import React from "react";
import HeaderBanner from "../HeaderBanner";
import Footer from "../Footer";
import ArticleSnapshot from "../ArticleSnapshot";
import Tag from "../Tag";
import { tags } from "../../master.json";
import transport from "../../axios";

class SearchResultsPage extends React.Component {
  state = {
    results: null,
    tags: tags,
    loadingResults: true,
    queryMade: false,
    selectedTag: tags[0],
    query: ""
  };

  componentDidMount() {
    console.log(tags);
    console.log(this.props.match.params.searchTerm);
    const { searchTerm } = this.props.match.params;
    this.setState({ query: searchTerm });
    // make api call to get results for query
    // set queryMade to true
    // add results to state.results
    // set loadingResults to false
    this.setState({ loadingResults: false });
  }

  search = async () => {
    this.setState({ loadingResults: true });
    const res = await transport.post("/search", {
      query: this.state.query
    });
    console.log("SEARCH RES: ", res);
    // query the api
    // load the results
    // set state of results and loadingResults
  };

  enterPressed = e => {
    let code = e.key || e.which;
    if (code === "Enter") {
      this.search();
      return;
    }
  };

  handleInputChange = e => {
    this.setState({ query: e.target.value });
  };

  clearQuery = () => {
    this.setState({ query: "" });
  };

  selectTag = tagNumber => {
    this.setState({ selectedTag: tags[tagNumber] });
  };

  renderTags = tags => {
    const { selectedTag } = this.state;
    if (!tags) {
      return null;
    } else {
      return tags.map((tag, index) => {
        const selected = tag === selectedTag ? true : false;
        return (
          <Tag
            onClick={() => this.selectTag(index)}
            isSelected={selected}
            content={tag}
          />
        );
      });
    }
  };

  renderResults = results => {
    const { loadingResults } = this.state;
    if (!results) {
      if (loadingResults) {
        return <p>Loading Results</p>;
      } else {
        return <p>No Results for the given query</p>;
      }
    }

    return results.map(result => {
      return <ArticleSnapshot />; //
    });
  };

  render() {
    return (
      <>
        <HeaderBanner />
        <div className="searchresults">
          <div className="searchresults__heading">
            <h4 className="h4">Search</h4>
          </div>
          <div className="searchresults__search">
            <svg className="searchresults__search-icon">
              <use xlinkHref="#search"></use>
            </svg>
            <input
              className="searchresults__input"
              name="search"
              type="text"
              placeholder="Search ..."
              onChange={this.handleInputChange}
              value={this.state.query}
              onKeyPress={this.enterPressed}
            ></input>
            <button onClick={this.clearQuery}>X</button>
          </div>
          <div className="searchresults__tags">
            {this.renderTags(this.state.tags)}
          </div>
          <div className="searchresults__results">{this.renderResults()}</div>
        </div>
        <Footer />
      </>
    );
  }
}

export default SearchResultsPage;
