import React from "react";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";

import HeaderBanner from "../HeaderBanner";
import ArticlesContainer from "../../containers/ArticlesContainer";
import HeroBanner from "../HeroBanner";
import ContactForm from "../ContactForm";
import SideBannerContainer from "../../containers/SideBannerContainer";
import Map from "../Map";
import Footer from "../Footer";
import Search from "../Search";
import Tag from "../Tag";
import transport from "../../axios";
import ArticleSnapshot from "../ArticleSnapshot";

class HomePage extends React.Component {
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
    let { searchTerm } = this.props.match.params;
    if (!searchTerm) {
      searchTerm = "";
    }
    this.setState({ query: searchTerm, tags: tags.data.tags });
    setTimeout(() => {
      this.search(this.state.query);
    }, 10);
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
  contactFormRef = React.createRef();
  render() {
    return (
      <div className="overlay" id="overlay">
        <Container fluid>
          <Row>
            <Col className="black-background">
              <HeaderBanner contactRef={this.contactFormRef} />
            </Col>
          </Row>
          <Row>
            <Col className="black-background">
              <HeroBanner />
            </Col>
          </Row>
          <Row>
            <Col xl={8}>
              <div className="homepage__content">
                <div className="homepage__content-leftColumn">
                  <div>
                    <Search />
                    <div className="searchresults__tags">
                      {this.renderTags(this.state.tags)}
                    </div>
                    <ArticlesContainer>
                      {this.renderResults(this.state.results)}
                    </ArticlesContainer>
                  </div>
                </div>
              </div>
            </Col>
            <Col>
              <div className="homepage__content">
                <SideBannerContainer />
              </div>
            </Col>
          </Row>
          <Row>
            <Col className="black-background">
              <div className="homepage__contact">
                <ContactForm ref={this.contactFormRef} />
              </div>
            </Col>
            <Col className="black-background">
              <div className="homepage__map">
                <Map />
              </div>
            </Col>
          </Row>
          <Row>
            <Col className="black-background">
              <div>
                <Footer />
              </div>
            </Col>
          </Row>
        </Container>
      </div>
    );
  }
}

export default HomePage;
