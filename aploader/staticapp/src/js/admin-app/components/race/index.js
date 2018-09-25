import React from 'react';
import Candidates from './Candidates';
import Cookies from 'js-cookie';
import getParameterByName from '../../utils/getParameterByName';

import './styles.scss';

const headers = {
  'Access-Control-Allow-Origin': '*',
  'Content-Type': 'application/json',
  'X-CSRFToken': Cookies.get('csrftoken'),
};

class Race extends React.Component {
  render() {
    const { race, actions } = this.props;

    return (
      <div className='race'>
        <h3>
          {race.election.office}
          {this.props.race.override_ap_call && (
            <span 
              className="override"
            >
              Overriding AP
            </span>
          )}
        </h3>
        <Candidates
          candidates={race.election.candidates}
          electionID={race.ap_election_id}
          actions={actions}
          called={race.called}
          overriding={race.override_ap_call}
        />
        <p className="precincts">
          {race.precincts_reporting} of {race.precincts_total} precincts reporting ({Math.round(race.precincts_reporting_pct) * 100}%)
        </p>
      </div>
    )
  }
}

export default Race;
