#!/usr/bin/python3

from routeros_api.routeros_api import Api
import sys, json, re

peers = {}
multipler = [1, 60, 3600, 86400, 604800]
peers['data'] = []

if len(sys.argv) >= 5:
  querytype = sys.argv[1]
  hostname = sys.argv[2]
  username = sys.argv[3]
  pwd = sys.argv[4]
if len(sys.argv) == 6:
  peername = sys.argv[5]

if __name__ == "__main__":
  if len(sys.argv) != 1:
    router = Api(hostname, user=username, password=pwd)

    # return the selected peer state and uptime defined as argument in peerfieldname
    if (querytype == "state") or (querytype == "uptime"):
      answer = router.talk('/routing/bgp/peer/print\n?name=' + peername)
      if querytype == "state":
        state = answer[0]['state']
        if state == 'established':
           print(4)
        elif state == 'active':
           print(3)
        elif state == 'opensent':
           print(2)
        elif state == 'openconfirm':
           print(2)
        elif state == 'idle':
           print(1)

      if querytype == "uptime":
        rosuptime=0
        uptime = answer[0]['uptime']

        #parse 3d20h9m20s format
        numbers = re.findall(r'\d+', uptime)
        numbers.reverse()

        for current in range(len(numbers)):
           rosuptime += int(numbers[current]) * multipler[current]

        print(rosuptime)

    # return peer names in json for disabled=false peers
    if querytype == "names":
      answer = router.talk('/routing/bgp/peer/print\n=status=')
      for val in answer:
         if val['disabled'] == 'false':
           peer = { "{#BGP_PEER_NAME}":val['name'] }
           peers['data'].append(peer)
      print(json.dumps(peers))

