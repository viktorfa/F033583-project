export const isNumber = (obj) => {
  return isNaN(Number.parseInt(obj)) && isNaN(Number.parseFloat(obj))
};

export const flatten = list => list.reduce(
  (a, b) => a.concat(Array.isArray(b) ? flatten(b) : b), []
);

export const getSearchUrlParameters = (indices, filters, ranking) => {
  const parameters = [getIndexParameter(indices), getFiltersParameter(filters), getRankingParameter(ranking)]
    .filter((parameter) => parameter !== '');

  return `?${parameters.join('&')}`
};

const getIndexParameter = (indices) => {
  const result = `index=${Object.keys(indices)
    .map((key, i) => indices[key] === true ? (key + '') : '')
    .filter((index) => index !== '')
    }`;
  if (result === 'index=') {
    return ''
  } else {
    return result;
  }
};

const getFiltersParameter = (filters) => {
  const parameterArray = flatten(Object.keys(filters).map((field) => {
    return Object.keys(filters[field]).map((operator) => {
      if (filters[field][operator]) {
        return getFiltersSubParameter(field, operator, filters[field][operator]);
      }
    });
  })).filter((subParameter) => subParameter);
  if (parameterArray.length === 0) {
    return ''
  } else {
    return `filters=${parameterArray}`;
  }
};
const getRankingParameter = (ranking) => {
  return `ranking=${ranking}`;
};

const getFiltersSubParameter = (field, operator, value) => {
  switch (field) {
    case 'year':
      field = 'year_released';
      break;
    case 'rating':
      field = 'album_rating';
      break;
    default:
      break;
  }
  return `${field}:${operator}:${value}`;
};
