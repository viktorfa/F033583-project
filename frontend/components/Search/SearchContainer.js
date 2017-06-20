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
import SearchComponent from "./SearchComponent";

const mapDispatchToProps = (dispatch) => {
  return {}
};

const mapStateToProps = (state) => {
  return {
    query: state.resultReducer.query,
    results: state.resultReducer.results,
    stats: state.resultReducer.stats
  }
};

export default connect(mapStateToProps, mapDispatchToProps)(SearchComponent);