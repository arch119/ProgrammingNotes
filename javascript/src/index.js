import data from './data/data'
import _ from 'lodash'


function getHosts(data){
    return _.values(data['hosts'])
}
window.a = getHosts(data)
window._ = _