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
import Song from "./Song";
import QueryContainer from './QueryContainer';
import SearchStatistics from "./SearchStatistics";
import LoadingScreen from './LoadingScreen';

function SearchComponent(props) {
  return (
    <div>
      <LoadingScreen loading={props.loading}/>
      <QueryContainer/>
      <SearchStatistics stats={props.stats}/>
      {(props.query && props.results) ? <h5>Results for "{props.query}"</h5> : ''}
      {props.results.map((song, index) => {
        return (<div key={song.id + props.stats.query_id}><Song song={song} stats={props.stats} rank={index} playSong={props.playSong}/></div>);
      })}
    </div>
  );
}

export default SearchComponent;
