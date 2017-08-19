import json
import os
import requests


def checkin():
    oauth_token = os.environ.get("oauth_token")
    venue_id = os.environ.get("venue_id")
    url = 'https://api.foursquare.com/v2/checkins/add?oauth_token={0}&v=20170601&venueId={1}'.format(
        oauth_token, venue_id)
    r = requests.post(url, data={})
    return json.loads(r.text)


def handle(req):
    result = checkin()
    print json.dumps(result)