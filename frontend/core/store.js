/**
 * React Static Boilerplate
 * https://github.com/kriasoft/react-static-boilerplate
 *
 * Copyright © 2015-present Kriasoft, LLC. All rights reserved.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE.txt file in the root directory of this source tree.
 */

import {createStore, applyMiddleware} from 'redux';
import thunkMiddlware from 'redux-thunk';

const initialState = {
  query: '',
  results: [],
  loading: false,
  stats: {}
};

// Centralized application state
// For more information visit http://redux.js.org/
const store = createStore((state = initialState, action) => {
  // TODO: Add action handlers (aka "reduces")
  switch (action.type) {
    case 'START_QUERY':
      return {...state, query: action.query, loading: true};
    case 'UPDATE_SEARCH_RESULTS':
      return {...state, results: action.data.results, stats: action.data.meta, loading: false};
    default:
      return state;
  }
},
applyMiddleware(thunkMiddlware));

const executeQuery = (query) => {

};

export default store;
