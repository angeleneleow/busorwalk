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
                    help='Bus stop to find incoming busses',
                    default='', nargs='?')
parser.add_argument('--status', dest='getStatus', action='store_true')
parser.add_argument('-k', '--key', dest='key')

args = parser.parse_args()
# Create new API instance with key
api = translink.API(args.key)

if args.getStatus:
    statuses = api.status_update()
    # [
    #     {'Name', 'Value'},
    #     {'Name', 'Value'},
    # ]
    for status in statuses:
        print '>> ' + status['Name'] + ': ' + status['Value'] 
    exit()

##############

# http://api.translink.ca/rttiapi/v1/stops/[STOPNUMBER]?apikey=[APIKey]
stop = api.bus_stop_request(args.bus_stop, '')
print 'The name of your bus stop is ' + stop['Name']

###############

# http://api.translink.ca/rttiapi/v1/stops/[STOPNUMBER]/estimates?apikey=[APIKey]
# [
#     { RouteNo, RouteName, Schedules: [ { ExpectedCountdown, ExpectedLeaveTime }, { ExpectedCountdown, ExpectedLeaveTime }, { ExpectedCountdown, ExpectedLeaveTime } ] },
#     { RouteNo, RouteName, Schedules: [ { ExpectedCountdown, ExpectedLeaveTime }, { ExpectedCountdown, ExpectedLeaveTime }, { ExpectedCountdown, ExpectedLeaveTime } ] },
#     { RouteNo, RouteName, Schedules: [ { ExpectedCountdown, ExpectedLeaveTime }, { ExpectedCountdown, ExpectedLeaveTime }, { ExpectedCountdown, ExpectedLeaveTime } ]  },
# ]
estimates = api.bus_stop_request(args.bus_stop, 'estimates')
for route in estimates:
    print '##############'
    print "For bus " + route['RouteNo'] + ' (' + route["RouteName"].strip() + '):'
    for bus in route['Schedules']:
        print '>> in ' + str(bus['ExpectedCountdown']) + ' minutes (' + bus['ExpectedLeaveTime'] + ')'
