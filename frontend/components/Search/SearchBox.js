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

class SearchBox extends React.Component {

  constructor(props) {
    super(props);

    this.state = {
      query: ''
    }
  }

  handleChange(event) {
    this.setState({query: event.target.value});
  }

  render() {
    return (
      <div>
        <form onSubmit={(event) => {
          event.preventDefault();
          this.props.executeQuery(this.state.query)
        }}>
          <div className="form-group">
            <label htmlFor="query">Query</label>
            <input type="text" name="query" placeholder="Enter query here"
                   value={this.state.query}
                   onChange={(event) => this.handleChange(event)}/>
          </div>
          <button type="submit">
            Search
          </button>
        </form>
      </div>
    );
  }
}

export default SearchBox;
