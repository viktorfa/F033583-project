/**
 * React Static Boilerplate
 * https://github.com/kriasoft/react-static-boilerplate
 *
 * Copyright © 2015-present Kriasoft, LLC. All rights reserved.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE.txt file in the root directory of this source tree.
 */

import {connect} from 'react-redux';
import PlayerComponent from "./PlayerComponent";

const PLAY = 'PLAY';
const STOP = 'STOP';


const play = () => {
  return {type: PLAY, isPlaying: true}
};

const stop = () => {
  return {type: STOP, isPlaying: false}
};


const mapDispatchToProps = (dispatch) => {
  return {
    play: () => {
      dispatch(play());
    },
    stop: () => {
      dispatch(stop());
    },
  }
};

const mapStateToProps = (state) => ({
  isPlaying: state.playerReducer.isPlaying,
  currentSong: state.playerReducer.currentSong
});

export default connect(mapStateToProps, mapDispatchToProps)(PlayerComponent);
