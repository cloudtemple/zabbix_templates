#!/usr/bin/env python3

import sys, redis, json, argparse

parser = argparse.ArgumentParser(description='Zabbix Redis status script')
parser.add_argument('--host', dest='redis_host', help='Redis server hostname', nargs='?')
parser.add_argument('-p', dest='redis_port', action='store', help='Redis server port', default=6379, type=int)
parser.add_argument('-a', dest='redis_pass', action='store', nargs='?', help='Redis server pass', default=None)
parser.add_argument('--info', action='store_true', help='Get Info Metrics', default=False)
parser.add_argument('--ping', action='store_true', help='Ping', default=False)
parser.add_argument('--slowlog', action='store_true', help='Slowlog Number of Items', default=False)
parser.add_argument('--config', action='store_true', help='Get Config Params', default=False)
args = parser.parse_args()

sections = ('Server', 'Clients', 'Memory', 'Persistence', 'Stats', 'Replication', 'CPU', 'Cluster', 'Keyspace')

info = {}

def compact_json(data):
    return json.dumps(data, separators=(',', ':'))

try:
    with redis.Redis(host=args.redis_host, port=args.redis_port, password=args.redis_pass) as client:
        if args.ping:
            ping = client.ping()
            if ping:
                print(1)
            else:
                print(0)

        if args.info:
            for section in sections:
                info[section] = client.info(section)
            print(compact_json(info))

        if args.slowlog:
            number = client.slowlog_len()
            print(number)

        if args.config:
            config = client.config_get()
            print(compact_json(config))

except redis.AuthenticationError as err:
    message = {'ZBX_NOTSUPPORTED': err}
    print(compact_json(message))
    sys.exit(1)
except redis.ConnectionError:
    message = {'ZBX_NOTSUPPORTED': err}
    print(compact_json(message))
    sys.exit(1)
except redis.RedisError:
    message = {'ZBX_NOTSUPPORTED': err}
    print(compact_json(message))
    sys.exit(1)

sys.exit()

