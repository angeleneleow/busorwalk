# This file contains translink API functions
import urllib2
import json

BASE_URL = 'http://api.translink.ca/rttiapi/v1'
API_ARG = '?apikey='

class API:
    '''
    Class API contains an interface to the translink API
    '''
    _key = ''

    def __init__(self, key):
        self._key = key

    def bus_stop_request(self, stopNumber, endpoint):
        '''
        This makes a request to translink's bus stops API
        '''
        # Create request URL
        base = BASE_URL + '/stops'
        if endpoint != '':
            endpoint = '/' + endpoint
        requestURL = base + '/' + stopNumber + endpoint + API_ARG + self._key

        # Make request
        req = urllib2.Request(requestURL, None, {
                            'Content-Type': 'application/json'})
        contents = urllib2.urlopen(req).read()
        contents = json.loads(contents)

        # Return result
        return contents

    def status_update(self):
        '''
        Get all translink status updates
        '''
        # http://api.translink.ca/rttiapi/v1/status/all?apikey=[APIKey]
        base = BASE_URL + '/status/all'
        requestURL = base + API_ARG + self._key

        # Make request
        req = urllib2.Request(requestURL, None, {
                            'Content-Type': 'application/json'})
        contents = urllib2.urlopen(req).read()
        contents = json.loads(contents)

        # Return result
        return contents
