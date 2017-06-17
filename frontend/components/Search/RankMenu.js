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

class RankMenu extends React.Component {

  constructor(props) {
    super(props);
  }

  handleChange(event) {
    this.props.handleChange(event.target.name);
  }

  render() {
    return (
      <div>
        <h4>Rank by</h4>
        <form onSubmit={(event) => {
          event.preventDefault();
        }}
              onChange={(event) => this.handleChange(event)}
        >
          <label htmlFor="relevance" className="mdl-radio mdl-js-radio mdl-js-ripple-effect">
            <input type="radio" name="relevance" id="relevance"
                   checked={this.props.state.ranking === 'relevance'}
                   onChange={(event) => {
                   }}
                   className="mdl-radio__button"
            />
            <span className="mdl-radio__label">Relevance</span>
          </label>
          <br/>
          <label htmlFor="popularity" className="mdl-radio mdl-js-radio mdl-js-ripple-effect">
            <input type="radio" name="popularity" id="popularity"
                   checked={this.props.state.ranking === 'popularity'}
                   onChange={(event) => {
                   }}
                   className="mdl-radio__button"
            />
            <span className="mdl-radio__label">Popularity</span>
          </label>
          <br/>
          <label htmlFor="date" className="mdl-radio mdl-js-radio mdl-js-ripple-effect">
            <input type="radio" name="date" id="date"
                   checked={this.props.state.ranking === 'date'}
                   onChange={(event) => {
                   }}
                   className="mdl-radio__button"
            />
            <span>Date</span>
          </label>
        </form>
      </div>

    );
  }
}

export default RankMenu;
