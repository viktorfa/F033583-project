/**
 * React Static Boilerplate
 * https://github.com/kriasoft/react-static-boilerplate
 *
 * Copyright © 2015-present Kriasoft, LLC. All rights reserved.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE.txt file in the root directory of this source tree.
 */

import {expect} from 'chai';

import {getSearchUrlParameters} from '../core/util';

describe('test suite', () => {

  it('test', () => {
    expect(true).to.be.equal.true;
  });
});

describe('test url parameters generator', () => {
  const indicesObject1 = {
    title: true,
    artist: true,
    lyrics: true,
  };

  const filtersObject1 = {
    year: {
      gte: undefined,
      lte: undefined,
    },
    rating: {
      gte: undefined,
      lte: undefined,
    }
  };
  const filtersObject2 = {
    year: {
      gte: 2010,
      lte: undefined,
    },
    rating: {
      gte: undefined,
      lte: undefined,
    }
  };
  const filtersObject3 = {
    year: {
      gte: 2010,
      lte: 2012,
    },
    rating: {
      gte: 5,
      lte: 10,
    }
  };

  const rankingObject1 = 'relevance';

  it('should return a string', () => {
    const result = getSearchUrlParameters({}, {}, {});
    expect(result).to.be.a.string;
  });
  it('should include indices when index object is provided', () => {
    const result = getSearchUrlParameters(indicesObject1, {}, {});
    expect(result).to.be.a.string;
    const expectedSubstring = 'index=title,artist,lyrics';
    expect(result).to.contain(expectedSubstring);
  });
  it('should not include filters when empty filters object is provided', () => {
    const result = getSearchUrlParameters({}, filtersObject1, {});
    expect(result).to.be.a.string;
    const notExpectedSubstring = 'filters=';
    expect(result).to.not.contain(notExpectedSubstring);
  });
  it('should include filters when one simple filters object is provided', () => {
    const result = getSearchUrlParameters({}, filtersObject2, {});
    expect(result).to.be.a.string;
    const expectedSubstring = 'filters=year_released:gte:2010';
    expect(result).to.contain(expectedSubstring);
  });
  it('should include filters when one complicated filters object is provided', () => {
    const result = getSearchUrlParameters({}, filtersObject3, {});
    expect(result).to.be.a.string;
    const expectedSubstring = 'filters=year_released:gte:2010,year_released:lte:2012,album_rating:gte:5,album_rating:lte:10';
    expect(result).to.contain(expectedSubstring);
  });
  it('should include ranking when ranking object is provided', () => {
    const result = getSearchUrlParameters({}, {}, rankingObject1);
    expect(result).to.be.a.string;
    const expectedSubstring = 'ranking=relevance';
    expect(result).to.contain(expectedSubstring);
  });
  it('should include all parameters when complicated objects are provided', () => {
    const result = getSearchUrlParameters(indicesObject1, filtersObject3, rankingObject1);
    expect(result).to.be.a.string;
    const expectedSubstring1 = 'index=title,artist,lyrics';
    const expectedSubstring2 = 'filters=year_released:gte:2010,year_released:lte:2012,album_rating:gte:5,album_rating:lte:10';
    const expectedSubstring3 = 'ranking=relevance';
    expect(result).to.contain(expectedSubstring1);
    expect(result).to.contain(expectedSubstring2);
    expect(result).to.contain(expectedSubstring3);
  });
});
