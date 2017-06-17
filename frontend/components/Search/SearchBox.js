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
          <div className="form-group mdl-textfield mdl-js-textfield">
            <input type="text" name="query" placeholder="Enter query here"
                   value={this.state.query}
                   onChange={(event) => this.handleChange(event)}
                   style={{textAlign: 'center'}}
                   className="mdl-textfield__input"
                   autoFocus={true}
            />
          </div>
          <div>
            <button type="submit" className="mdl-button mdl-js-button mdl-js-ripple-effect">
              Search
            </button>
          </div>
        </form>
      </div>
    );
  }
}

export default SearchBox;
