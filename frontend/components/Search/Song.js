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
        <table className="mdl-data-table mdl-js-data-table mdl-shadow--2dp" style={{minWidth: '100%'}}>
          <thead>
          <tr>
            <th>Title</th>
            <th>Artist</th>
            <th>Album</th>
            <th>Year</th>
            <th>Rank score</th>
          </tr>
          </thead>
          <tbody>
          <tr>
            <td>{this.props.song.title}</td>
            <td>{this.props.song.artist}</td>
            <td>{this.props.song.album}</td>
            <td>{this.props.song.year_released}</td>
            <td>{this.props.song.ranking.score}</td>
            <td>
              <button onClick={() => this.selectSong()} disabled={this.state.selected}
                      className="mdl-button mdl-js-button"
              >
                Select song</button>
            </td>
          </tr>
          </tbody>
        </table>
        {this.state.selected ? (<pre>
         {JSON.stringify(this.props.song, null, 2)}
         </pre>) : ''}

      </div>
    );
  }
}

export default Song;
