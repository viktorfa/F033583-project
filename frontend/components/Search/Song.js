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
      selected: false,
      playing: false
    })
  }

  selectSong() {
    fetch(`//localhost:8000/click/?qid=${this.props.stats.query_id}&sid=${this.props.song.ranking.id}`, {method: 'POST'})
      .then(response => {
        if (response.ok) {
          console.log("Registred select click.");
          console.log(response);
          this.setState({selected: true});
        } else {
          throw new Error(`Could not register click with server: ${response.status} ${response.statusText}`)
        }
      }).catch(error => console.log(error.message));
  }

  playSong() {
    fetch(`//localhost:8000/click/?qid=${this.props.stats.query_id}&sid=${this.props.song.ranking.id}`, {method: 'POST'})
      .then(response => {
        if (response.ok) {
          console.log("Registred play click.");
          console.log(response);
          this.setState({playing: true});
          this.props.playSong(this.props.song)
        } else {
          throw new Error(`Could not register click with server: ${response.status} ${response.statusText}`)
        }
      }).catch(error => console.log(error.message));
  }

  highlightQuery(string) {
    const queryTerms = this.props.stats.query.split(' ').map((token, index) => token.toLowerCase());
    return <span>{string.split(' ').map((token, index) => {
      return queryTerms.includes(token.toLowerCase()) ? <span key={index} className="highlight-text">{token}</span> :
        <span> {token} </span>;
    })}</span>;
  }

  render() {
    if (this.state.selected !== true) {

      return (
        <div className="mdl-shadow--2dp">
          <div className="mdl-grid">
            <div className="mdl-cell--1-col">
              <small>Rank</small>
              <h6 style={{marginTop: 0}}>{this.props.rank}</h6>
            </div>
            <div className="mdl-cell--4-col">
              <p><strong>{(this.highlightQuery(this.props.song.title))} ({this.props.song.year_released})</strong></p>
              <p>{this.highlightQuery(this.props.song.artist)}</p>
            </div>
            <div className="mdl-cell--4-col">
              <p>
                <small>Score</small>
                {this.props.song.ranking.score}</p>
              <p>
                <small>Clicks</small>
                {this.props.song.ranking.clicks}</p>
            </div>
          </div>
          <div>
            {/**<small>{this.highlightQuery(this.props.song.lyrics.replace(/[\n\r]+/g, ' '))}</small>*/}
          </div>
          <button onClick={() => this.selectSong()} disabled={this.state.selected}
                  className="mdl-button mdl-js-button"
          >
            Select song
          </button>
          <button onClick={() => this.playSong()} disabled={this.state.playing}
                  className="mdl-button mdl-js-button"
          >
            Play song
          </button>
          {
            this.state.playing === "anus" ?
              <iframe src={this.props.song.play_link} frameborder="0" width={200} height={200}
                      onLoad={() => console.log("IFRAME LOADED!!1")}></iframe> : ''
          }
        </div>
      );
    } else {
      return (
        <div>
          <pre>{JSON.stringify(this.props.song, null, 2)}</pre>
        </div>
      )
    }
  }
}

export default Song;
