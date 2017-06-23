import {combineReducers} from 'redux';

const initialResultState = {
  query: '',
  results: [],
  loading: false,
  stats: {}
};
const resultReducer = (state = initialResultState, action) => {
  switch (action.type) {
    case 'START_QUERY':
      return {...state, query: action.query, loading: true};
    case 'UPDATE_SEARCH_RESULTS':
      return {...state, results: action.data.results, stats: action.data.meta, loading: false};
    default:
      return state;
  }
};

const initialQueryState = {
  indicesState: {
    indices: {
      title: true,
      artist: true,
      lyrics: true,
    },
    valid: true
  },
  filtersState: {
    filters: {
      year: {
        gte: undefined,
        lte: undefined,
      },
      rating: {
        gte: undefined,
        lte: undefined,
      }
    },
    valid: true
  },
  rankingState: {
    ranking: 'relevance',
    valid: true
  },
};
const queryReducer = (state = initialQueryState, action) => {
  switch (action.type) {
    case 'UPDATE_QUERY_INDICES':
      return {...state, indicesState: action.indicesState};
    case 'UPDATE_QUERY_FILTERS':
      return {...state, filtersState: action.filtersState};
    case 'UPDATE_QUERY_RANKING':
      return {...state, rankingState: action.rankingState};
    default:
      return state;
  }
};

const initialPlayerState = {isPlaying: false, currentSong: undefined};
const playerReducer = (state = initialPlayerState, action) => {
  switch (action.type) {
    case 'PLAY_SONG':
      return {...state, isPlaying: true, currentSong: action.song};
    case 'PLAY':
      return {...state, isPlaying: true};
    case 'STOP':
      return {...state, isPlaying: false};
    default:
      return state;
  }
};

export default combineReducers({resultReducer, queryReducer, playerReducer});
