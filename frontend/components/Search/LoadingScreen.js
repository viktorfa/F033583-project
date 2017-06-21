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

class LoadingScreen extends React.Component {

  constructor(props) {
    super(props);
    this.spinnerWidth = 240;
  }

  render() {
    return (
      <div>
        <div
          style={{
            position: 'fixed',
            width: '100vw', height: '100vh',
            top: 0, left: 0,
            backgroundColor: 'rgba(50, 50, 50, 0.5)',
            zIndex: '90',
            visibility: this.props.loading ? 'visible' : 'hidden',
            textAlign: 'center'
          }}
        >
          <div
            style={{
              position: 'fixed',
              bottom: '50vh',
              right: '50vw',
            }}
          >
            <img style={{position: 'absolute', zIndex: '91', margin: '-100px 0 0 -100px'}} width={this.spinnerWidth}
                 src="/sjtu_logo_wheel.png"
                 className="spin"
                 alt="Loading"/>

            <img style={{position: 'absolute', top: '20px', left: '20px', margin: '-100px 0 0 -100px', zIndex: '92'}}
                 width="200px"
                 src="/sjtu_logo_anvil.png"
                 alt="Loading"/>
          </div>
        </div>
      </div>
    );
  }
}

export default LoadingScreen;
