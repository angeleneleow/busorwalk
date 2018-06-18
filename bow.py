import argparse
import urllib2
import json

# My code
import translink

##############
# My app

parser = argparse.ArgumentParser(description='''bow - bus or walk.
This app talks to Translink and does cool stuff.
''')
parser.add_argument('bus_stop', metavar='[stop]', type=str,
                    help='Bus stop to find incoming busses')
parser.add_argument('-k', '--key', dest='key')

args = parser.parse_args()
print 'You entered: ' + args.bus_stop
print 'Your key:    ' + args.key

##############

# http://api.translink.ca/rttiapi/v1/stops/[STOPNUMBER]?apikey=[APIKey]
stop = translink.stops_request(args.bus_stop, '', args.key)
print 'The name of your bus stop is ' + stop['Name']

###############

# http://api.translink.ca/rttiapi/v1/stops/[STOPNUMBER]/estimates?apikey=[APIKey]
# [
#     { RouteNo, RouteName, Schedules: [ { ExpectedCountdown, ExpectedLeaveTime }, { ExpectedCountdown, ExpectedLeaveTime }, { ExpectedCountdown, ExpectedLeaveTime } ] },
#     { RouteNo, RouteName, Schedules: [ { ExpectedCountdown, ExpectedLeaveTime }, { ExpectedCountdown, ExpectedLeaveTime }, { ExpectedCountdown, ExpectedLeaveTime } ] },
#     { RouteNo, RouteName, Schedules: [ { ExpectedCountdown, ExpectedLeaveTime }, { ExpectedCountdown, ExpectedLeaveTime }, { ExpectedCountdown, ExpectedLeaveTime } ]  },
# ]
estimates = translink.stops_request(args.bus_stop, 'estimates', args.key)
for route in estimates:
    print '##############'
    print "For bus " + route['RouteNo'] + ' (' + route["RouteName"].strip() + '):'
    for bus in route['Schedules']:
        print '>> in ' + str(bus['ExpectedCountdown']) + ' minutes (' + bus['ExpectedLeaveTime'] + ')'
