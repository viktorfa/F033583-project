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
import QueryComponent from "./QueryComponent";
import {isNumber, getSearchUrlParameters} from '../../core/util';

const START_QUERY = 'START_QUERY';
const UPDATE_SEARCH_RESULTS = 'UPDATE_SEARCH_RESULTS';
const UPDATE_QUERY_INDICES = 'UPDATE_QUERY_INDICES';
const UPDATE_QUERY_FILTERS = 'UPDATE_QUERY_FILTERS';
const UPDATE_QUERY_RANKING = 'UPDATE_QUERY_RANKING';

const startQuery = (query) => {
  return {
    type: START_QUERY,
    query
  }
};

const executeQuery = (query, indices, filters, ranking) => {
  return dispatch => {
    dispatch(startQuery(query));
    fetch(`//localhost:8000/search/${query}/${getSearchUrlParameters(indices, filters, ranking)}`)
      .then(response => response.json())
      .then(json => dispatch(updateSearchResults(json)))
  }
};

const updateSearchResults = (data) => {
  console.log("Updating search results:");
  console.log(data);
  return {
    type: UPDATE_SEARCH_RESULTS,
    data
  }
};

const handleQueryIndicesChange = (name, checked, indices) => {
  indices[name] = checked;
  const indicesState = Object.assign({}, {indices, valid: queryIndicesIsValid(indices)});
  return {
    type: UPDATE_QUERY_INDICES,
    indicesState
  }

};
const queryIndicesIsValid = (indices) => {
  return Object.keys(indices).reduce((acc, key) => acc || indices[key], false);
};

const handleQueryFiltersChange = (field, name, value, filters) => {
  console.log(field, name, value, filters);
  filters[field][name] = value;
  const filtersState = Object.assign({}, {filters, valid: queryFiltersIsValid(filters)});
  return {
    type: UPDATE_QUERY_FILTERS,
    filtersState
  }
};
const queryFiltersIsValid = (filters) => {
  return Object.keys(filters).reduce((acc, key) => {
      return acc && ((Number.parseInt(filters[key].lte) >= Number.parseInt(filters[key].gte)) ||
        isNumber(filters[key].lte) || isNumber(filters[key].gte))
    },
    true
  );
};

const handleQueryRankingChange = (name) => {
  const rankingState = Object.assign({}, {ranking: name, valid: queryRankingIsValid(name)});
  return {
    type: UPDATE_QUERY_RANKING,
    rankingState
  }

};
const queryRankingIsValid = (name) => {
  return typeof name === 'string';
};

const mapDispatchToProps = (dispatch) => {
  return {
    executeQuery: (query, indices, filters, ranking) => {
      dispatch(executeQuery(query, indices, filters, ranking));
    },
    handleQueryIndicesChange: (name, checked, indices) => {
      dispatch(handleQueryIndicesChange(name, checked, indices));
    },
    handleQueryFiltersChange: (field, name, value, filters) => {
      dispatch(handleQueryFiltersChange(field, name, value, filters));
    },
    handleQueryRankingChange: (name) => {
      dispatch(handleQueryRankingChange(name));
    },
  }
};

const mapStateToProps = (state) => ({
  indicesState: state.queryReducer.indicesState,
  filtersState: state.queryReducer.filtersState,
  rankingState: state.queryReducer.rankingState
});

export default connect(mapStateToProps, mapDispatchToProps)(QueryComponent);
