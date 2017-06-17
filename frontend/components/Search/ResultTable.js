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
import SongTableRow from './SongTableRow';

class ResultTable extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      dataKeys: [
        (obj) => obj.title,
        (obj) => obj.artist,
        (obj) => obj.album,
        (obj) => obj.year_released,
        (obj) => obj.ranking.score,
      ]
    }
  }

  headerFields = {
    title: 'Title',
    artist: 'Artist',
    album: 'Album',
    year_released: 'Year',
    ranking: {score: 'Ranking score'},
  };

  render() {
    return (
      <div>
        <div className="mdl-grid">
          {this.state.dataKeys.map((fn, index) => {
            return (
              <div key={index} className="mdl-cell--2-col">
                {fn(this.headerFields)}
              </div>
            )
          })}
        </div>
        {this.props.songs.map((song) => {
          return (<SongTableRow key={song.id + this.props.stats.query_id}
                                song={song} stats={this.props.stats}
                                dataKeys={this.state.dataKeys}
          />)
        })}
      </div>
    );
  }
}

export default ResultTable;
