import json
import urllib2


def getData(data_type):
    req = urllib2.Request('https://jawbone.com/nudge/api/v.1.1/users/@me/'+data_type)
    req.add_header('Authorization', 'Bearer DCEOB729f3iUCtygqTYU9U9aliRj0wuOHcGsYF_JuLwT6kBY2Qwif92vmggM0gXmUz5jHG9F8mwSAqLvkYReeFECdgRlo_GULMgGZS0EumxrKbZFiOmnmAPChBPDZ5JP')
    req.add_header('Accept', 'application/json')

    resp = urllib2.urlopen(req)
    content = resp.read()
    alldat = json.loads(content)
    return alldat


clientid = '1QcHq0B_THg'
client_secret='70534a74b2f62bbfca58dda2b756ccc9787ccf6b'

#date = getData('bandevents')['data']['remaining_for_day']

goaldat = getData('goals')
time = int(goaldat['meta']['time'])
goals = goaldat['data']['remaining_for_day']
steps = goals['move_steps_remaining']
sleep = goals['sleep_seconds_remaining']

bool_steps = int(steps)<=0
bool_sleep = int(sleep)<=0

print time
print bool_steps, bool_sleep

#excercise = getData('goals')['data']
#numex = excercise['size']
#excercise_list = excercise['items']
#print excercise_list[0].keys()
#print excercise_list[0]['details'].keys()