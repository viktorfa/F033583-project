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

function SearchStatistics(props) {
  console.log("PROMP");
  console.log(props.stats);
  if (Object.keys(props.stats).length > 0) {
    return (
      <div>
        <h6>Information about the last query</h6>
        <table className="mdl-data-table mdl-js-data-table mdl-shadow--2dp">
          <thead>
          <tr>
            {Object.keys(props.stats).map((key) => <th key={key}>{key}</th>)}
          </tr>
          </thead>
          <tbody>
          <tr>
            {Object.keys(props.stats).map((key) => <td key={key}>{props.stats[key]}</td>)}
          </tr>
          </tbody>
        </table>
      </div>
    );
  } else {
    return (<div></div>)
  }
}

export default SearchStatistics;
