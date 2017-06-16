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
import SearchBox from "./SearchBox";
import Song from "./Song";
import SearchStatistics from "./SearchStatistics";

function SearchComponent(props) {
  return (
    <div>
      <SearchStatistics stats={props.stats}/>
      <SearchBox executeQuery={props.executeQuery}/>
      {props.results.map((song, index) => {
        return (<div><h3>{index}</h3> <Song song={song} stats={props.stats}/></div>);
      })}
    </div>
  );
}

export default SearchComponent;
