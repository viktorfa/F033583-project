/**
 * React Static Boilerplate
 * https://github.com/kriasoft/react-static-boilerplate
 *
 * Copyright © 2015-present Kriasoft, LLC. All rights reserved.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE.txt file in the root directory of this source tree.
 */

import React, {PropTypes} from 'react';
import Layout from '../../components/Layout';
import SearchContainer from '../../components/Search';
import PlayerContainer from '../../components/Player';
import s from './styles.css';
import {title, html} from './index.md';

class HomePage extends React.Component {


  componentDidMount() {
    document.title = title;
  }

  render() {
    return (
      <Layout className={s.content}>
        <div dangerouslySetInnerHTML={{__html: html}}/>
        <PlayerContainer/>
        <SearchContainer/>
        <p>
          <br /><br />
        </p>
      </Layout>
    );
  }

}

export default HomePage;
