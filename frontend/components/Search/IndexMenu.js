/**
 * React Static Boilerplate
 * https://github.com/kriasoft/react-static-boilerplate
 *
 * Copyright © 2015-present Kriasoft, LLC. All rights reserved.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE.txt file in the root directory of this source tree.
 */

import React from 'react';

class IndexMenu extends React.Component {

  constructor(props) {
    super(props);
  }

  handleChange(event) {
    this.props.handleChange(event.target.name, event.target.checked, this.props.state.indices)
  }

  render() {
    return (
      <div>
        <h4>Indexed fields</h4>
        <form onSubmit={(event) => {
          event.preventDefault();
        }}
              onChange={(event) => this.handleChange(event)}
        >
          <label htmlFor="title" className="mdl-checkbox mdl-js-checkbox mdl-js-ripple-effect">
            <input type="checkbox" name="title" id="title"
                   checked={this.props.state.indices.title}
                   onChange={(event) => {
                   }}
                   className="mdl-checkbox__input"
            />
            <span className="mdl-checkbox__label">Title</span>
          </label>
          <label htmlFor="artist" className="mdl-checkbox mdl-js-checkbox mdl-js-ripple-effect">

            <input type="checkbox" name="artist" id="artist"
                   checked={this.props.state.indices.artist}
                   onChange={(event) => {
                   }}
            />
            <span className="mdl-checkbox__label">Artists</span>
          </label>
          <label htmlFor="lyrics" className="mdl-checkbox mdl-js-checkbox mdl-js-ripple-effect">

            <input type="checkbox" name="lyrics" id="lyrics"
                   checked={this.props.state.indices.lyrics}
                   onChange={(event) => {
                   }}
            />
            <span className="mdl-checkbox__label">Lyrics</span>
          </label>
        </form>
      </div>

    );
  }
}

export default IndexMenu;
