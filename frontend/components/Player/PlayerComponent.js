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

class PlayerComponent extends React.Component {

  constructor(props) {
    super(props);
    console.log("props");
    console.log(props);
  }

  render() {
    return (
      <div style={{position: 'fixed', right: '2vw', bottom: '6vh', zIndex: '80'}}>
        {this.props.currentSong ? (
          <div>
            {this.props.isPlaying ?
              <iframe src={this.props.currentSong.play_link} frameborder="1" width="600" height="200" hidden></iframe>
              : ''}
            {this.props.isPlaying ? (
              <button className="mdl-button mdl-js-button mdl-button--fab mdl-js-ripple-effect"
                      onClick={() => this.props.stop()}>
                <i className="material-icons">stop</i>
              </button>
            ) : (
              <button className="mdl-button mdl-js-button mdl-button--fab mdl-js-ripple-effect"
                      onClick={() => this.props.play()}>
                <i className="material-icons">play</i>
              </button>
            )}
          </div>
        ) :
          ''}

      </div>
    )
  }
}

export default PlayerComponent;
