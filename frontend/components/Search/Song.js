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


class Song extends React.Component {
  constructor(props) {
    super(props);

    this.state = ({
      selected: false
    })
  }

  selectSong() {
    fetch(`//localhost:8000/click/?qid=${this.props.stats.query_id}&sid=${this.props.song.ranking.id}`, {method: 'POST'})
      .then(response => {
        if (response.ok) {
          console.log("Registred click.");
          console.log(response);
          this.setState({selected: true});
        } else {
          throw new Error(`Could not register click with server: ${response.status} ${response.statusText}`)
        }
      }).catch(error => console.log(error.message));
  }

  render() {
    return (
      <div>
        <button onClick={() => this.selectSong()} disabled={this.state.selected}>Select song</button>
        <pre>
        {JSON.stringify(this.props.song, null, 2)}
      </pre>
      </div>
    );
  }
}

export default Song;
