import React from "react";
import HeaderBanner from "../HeaderBanner";
import Footer from "../Footer";
import ArticleSnapshot from "../ArticleSnapshot";
import Tag from "../Tag";
import { tags } from "../..//master.json";

class SearchResultsPage extends React.Component {
  state = {
    results: null,
    tags: tags,
    loadingResults: true,
    queryMade: false,
    selectedTag: tags[0]
  };

  componentDidMount() {
    console.log(tags);
    // make api call to get results for query
    // set queryMade to true
    // add results to state.results
    // set loadingResults to false
    this.setState({ loadingResults: false });
  }

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
            ></input>
            <button>X</button>
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
