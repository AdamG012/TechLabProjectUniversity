import React from "react";
import HeaderBanner from "../HeaderBanner";
import Footer from "../Footer";
import ArticleSnapshot from "../ArticleSnapshot";
import Tag from "../Tag";
import transport from "../../axios";

class SearchResultsPage extends React.Component {
  state = {
    results: [], // stores abstract responses
    tags: [],
    loadingResults: true,
    queryMade: false,
    selectedTags: [],
    query: ""
  };

  async componentDidMount() {
    // get the tags
    const tags = await transport.get("/tags");
    const { searchTerm } = this.props.match.params;
    this.setState({ query: searchTerm, tags: tags.data.tags });
    this.search();
  }

  search = async query => {
    this.setState({ loadingResults: true, results: [] });
    const res = await transport.post("/search", {
      query: query,
      tags: this.state.selectedTags
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
    this.setState({ query: "", selectedTags: [] });
    this.search("");
  };

  selectTag = tagNumber => {
    // this.setState({ selectedTag: tags[tagNumber] });
  };

  toggleTagSelected = index => {
    const { selectedTags, tags } = this.state;
    // if the tag is in selectedTags, remove it
    if (selectedTags.includes(tags[index])) {
      const updatedTags = selectedTags.filter(tag => {
        return tag !== tags[index];
      });
      this.setState({ selectedTags: updatedTags });
    } else {
      // else add the tag to selectedTags
      this.setState({ selectedTags: [...selectedTags, tags[index]] });
    }
    setTimeout(() => {
      this.search(this.state.query);
    }, 10);
  };

  renderTags = tags => {
    if (!tags) {
      return null;
    } else {
      return tags.map((tag, index) => {
        // const selected = tag === selectedTag ? true : false;
        const selected = this.state.selectedTags.includes(tag);
        return (
          <Tag
            key={index}
            onClick={() => this.toggleTagSelected(index)}
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
