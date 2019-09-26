#!/usr/bin/python3

from routeros_api.routeros_api import Api
import sys, argparse, json, datetime, re

peers = {}
multipler = [1, 60, 3600, 86400, 604800]
peers['data'] = []

if __name__ == "__main__":
   parser = argparse.ArgumentParser(description='usefull arguments')
   parser.add_argument('-t', '--type', required=True, dest='querytype', choices=['names','field'], help='Define query type: names | field')
   parser.add_argument('--hostname', required=True, dest='hostname')
   parser.add_argument('--username', required=True, dest='username')
   parser.add_argument('--password', required=True, dest='pwd')
   parser.add_argument('--peername', dest='peername')
   parser.add_argument('--peerfieldname', dest='peerfieldname', choices=['state','uptime'])
   args = parser.parse_args()

#   print(args.hostname)

   router = Api(args.hostname, user=args.username, password=args.pwd)

   # return the selected peer state and uptime defined as argument in peerfieldname
   if args.querytype == "field":
      answer = router.talk('/routing/bgp/peer/print\n?name=' + args.peername)
      if args.peerfieldname == "state":
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

      if args.peerfieldname == "uptime":
        rosuptime=0
        uptime = answer[0]['uptime']

        #parse 3d20h9m20s format
        numbers = re.findall(r'\d+', uptime)
        numbers.reverse()

        for current in range(len(numbers)):
           rosuptime += int(numbers[current]) * multipler[current]

        print(rosuptime)

   # return peer names in json for disabled=false peers
   if args.querytype == "names":
      answer = router.talk('/routing/bgp/peer/print\n=status=')
      for val in answer:
         if val['disabled'] == 'false':
           peer = { "{#BGP_PEER_NAME}":val['name'] }
           peers['data'].append(peer)
      print(json.dumps(peers))

