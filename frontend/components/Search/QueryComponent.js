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
import FilterMenu from "./FilterMenu";
import IndexMenu from "./IndexMenu";
import RankMenu from "./RankMenu";

class QueryComponent extends React.Component {
  constructor(props) {
    super(props);
  }

  executeQuery = (query) => {
    this.props.executeQuery(
      query,
      this.props.indicesState.indices,
      this.props.filtersState.filters,
      this.props.rankingState.ranking
    )
  };

  render() {
    return (
      <div>
        <div style={{'text-align': 'center'}}>
          <SearchBox executeQuery={this.executeQuery.bind(this)}/>
        </div>
        <div className={['mdl-grid']}>
          <div className={['mdl-cell mdl-cell--3-col']}>
            <RankMenu state={this.props.rankingState} handleChange={this.props.handleQueryRankingChange.bind(this)}/>
          </div>
          <div className={['mdl-cell mdl-cell--6-col']}>
            <FilterMenu state={this.props.filtersState} handleChange={this.props.handleQueryFiltersChange.bind(this)}/>
          </div>
          <div className={['mdl-cell mdl-cell--3-col']}>
            <IndexMenu state={this.props.indicesState} handleChange={this.props.handleQueryIndicesChange.bind(this)}/>
          </div>
        </div>
      </div>
    );
  }
}

export default QueryComponent;
