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
import {isNumber} from '../../core/util';

class FilterMenu extends React.Component {

  constructor(props) {
    super(props);
  }

  handleChange(event, field) {
    const name = event.target.name;
    const value = event.target.value;
    this.props.handleChange(field, name, value, this.props.state.filters)
  }

  handleYearFilterChange(event) {
    this.handleChange(event, 'year');
  }

  handleRatingFilterChange(event) {
    this.handleChange(event, 'rating');
  }

  render() {
    return (
      <div className="mdl-grid">
        <div className="mdl-cell--6-col">
          <h4>Year released</h4>
          <form onSubmit={(event) => {
            event.preventDefault();
          }}
                onChange={(event) => this.handleYearFilterChange(event)}>
            <div className="form-group mdl-textfield mdl-js-textfield">
              <label htmlFor="gte">After</label>
              <input type="number" name="gte" placeholder="1900"
                     value={this.props.state.filters.year.gte}
                     className="mdl-textfield__input"
              />
            </div>
            <div className="form-group mdl-textfield mdl-js-textfield">
              <label htmlFor="lte">Before</label>
              <input type="number" name="lte" placeholder="2017"
                     value={this.props.state.filters.year.lte}
                     className="mdl-textfield__input"
              />
            </div>
          </form>
        </div>
        <div className="mdl-cell--6-col">
          <h4>Rating</h4>
          <form onSubmit={(event) => {
            event.preventDefault();
          }}
                onChange={(event) => this.handleRatingFilterChange(event)}>
            <div className="form-group mdl-textfield mdl-js-textfield">
              <label htmlFor="gte">Min</label>
              <input type="number" name="gte" placeholder="0"
                     value={this.props.state.filters.rating.gte}
                     className="mdl-textfield__input"
              />
            </div>
            <div className="form-group mdl-textfield mdl-js-textfield">
              <label htmlFor="lte">Max</label>
              <input type="number" name="lte" placeholder="10"
                     value={this.props.state.filters.rating.lte}
                     className="mdl-textfield__input"
              />
            </div>
          </form>
        </div>
      </div>

    );
  }
}

export default FilterMenu;
