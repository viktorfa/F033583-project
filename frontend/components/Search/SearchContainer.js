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
import fetch from 'isomorphic-fetch';
import SearchComponent from "./SearchComponent";

const START_QUERY = 'START_QUERY';
const UPDATE_SEARCH_RESULTS = 'UPDATE_SEARCH_RESULTS';

const startQuery = (query) => {
  return {
    type: START_QUERY,
    query
  }
};

const executeQuery = (query) => {
  return dispatch => {
    dispatch(startQuery(query));
    fetch(`//localhost:8000/search/${query}/`)
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


const mapDispatchToProps = (dispatch) => {
  return {
    executeQuery: (query) => {
      dispatch(executeQuery(query))

    },
  }
};

const mapStateToProps = (state) => ({
  query: state.query,
  results: state.results,
  stats: state.stats
});

export default connect(mapStateToProps, mapDispatchToProps)(SearchComponent);
