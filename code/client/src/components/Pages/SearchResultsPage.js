import React from "react";
import HeaderBanner from "../HeaderBanner";
import Footer from "../Footer";
import ArticleSnapshot from "../ArticleSnapshot";
import Tag from "../Tag";
import { tags } from "../../master.json";
import transport from "../../axios";

class SearchResultsPage extends React.Component {
  state = {
    results: [], // stores abstract responses
    tags: tags,
    loadingResults: true,
    queryMade: false,
    selectedTag: tags[0],
    query: ""
  };

  componentDidMount() {
    const { searchTerm } = this.props.match.params;
    this.setState({ query: searchTerm });
    this.search();
    // make api call to get results for query
    // set queryMade to true
    // add results to state.results
    // set loadingResults to false
  }

  search = async query => {
    this.setState({ loadingResults: true, results: [] });
    const res = await transport.post("/search", {
      query: query
    });
    if (!res.data.results) {
      // no results found
      this.setState({ results: [], loadingResults: false });
      return;
    }

    const { results } = res.data;
    results.map(async id => {
      const d = await transport.get(`/abstract/${id}`);
      d.data.article.id = id;
      this.setState({ results: [...this.state.results, d.data.article] });
      return;
    });
    this.setState({ loadingResults: false });
  };

  enterPressed = e => {
    let code = e.key || e.which;
    if (code === "Enter") {
      this.search(this.state.query);
      return;
    }
  };

  handleInputChange = e => {
    this.setState({ query: e.target.value });
  };

  clearQuery = () => {
    this.setState({ query: "" });
    this.search("");
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
            key={index}
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
    if (results.length < 1) {
      if (loadingResults) {
        return <p>Loading Results</p>;
      } else {
        return <p>No Results for the given query</p>;
      }
    }

    return results.map(article => {
      return (
        <ArticleSnapshot
          id={article.id}
          key={article.id}
          author={article.author}
          abstract={article.abstract}
          imageURL={article.image}
          title={article.title}
          timeToRead={article.time_to_read}
          tags={article.tags}
          content={article.abstract}
        />
      );
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
          <div className="searchresults__results">
            {this.renderResults(this.state.results)}
          </div>
        </div>
        <Footer />
      </>
    );
  }
}

export default SearchResultsPage;
