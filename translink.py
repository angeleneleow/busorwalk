# This file contains translink API functions
import urllib2
import json

BASE_URL = 'http://api.translink.ca/rttiapi/v1'
API_ARG = '?apikey='


def stops_request(stopNumber, endpoint, key):
    '''
    This makes a request to translink's bus stops API
    '''
    # Create request URL
    base = BASE_URL + '/stops'
    if endpoint != '':
        endpoint = '/' + endpoint
    requestURL = base + '/' + stopNumber + endpoint + API_ARG + key

    # Make request
    req = urllib2.Request(requestURL, None, {
                          'Content-Type': 'application/json'})
    contents = urllib2.urlopen(req).read()
    contents = json.loads(contents)

    # Return result
    return contents
