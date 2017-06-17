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

class SongTableRow extends React.Component {
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
    if (this.state.selected !== true && false) {
      return (
        <tr>
          {this.props.dataKeys.map((fn, index) => (<td key={index}><strong>{fn(this.props.song)}</strong></td>))}
          <td>
            <button onClick={() => this.selectSong()} disabled={this.state.selected}
                    className="mdl-button mdl-js-button"
            >
              Select song
            </button>
          </td>
        </tr>
      );
    } else if (this.state.selected !== true) {
      return (
        <div className="mdl-grid">
          {this.props.dataKeys.map((fn, index) => (
            <div className="mdl-cell--2-col" key={index}><strong>{fn(this.props.song)}</strong></div>))}
          <div className="mdl-cell--2-col">
            <button onClick={() => this.selectSong()} disabled={this.state.selected}
                    className="mdl-button mdl-js-button"
            >
              Select song
            </button>
          </div>
        </div>
      )
    } else {
      return (
        <pre style={{display: 'fixed'}}>
          {JSON.stringify(this.props.song, null, 2)}
        </pre>
      )
    }
  }
}

export default SongTableRow;
