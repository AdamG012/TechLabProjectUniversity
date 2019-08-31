'use strict';

const e = React.createElement;
class LikeButton extends React.Component {
	constructor(props) {
		super(props);
		this.state = { liked: false };
	}

	render() {
		if (this.state.liked) {
			// Add some call to backed so user can store this article
			return 'You liked this. The article will be added to your selection.';
		}
		
		return e(
			'button',
			{ onClick: () => this.setState({ liked: true }), }, 'Like'); 
	}
}

const domContainer = document.querySelector('#like_button_container');
ReactDOM.render(e(LikeButton), domContainer);
