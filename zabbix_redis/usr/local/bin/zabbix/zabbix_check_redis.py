#!/usr/bin/env python3

import os, sys, redis, json, argparse

parser = argparse.ArgumentParser(description='Zabbix Redis status script')
parser.add_argument('--unix', help='Path to unix socket file')
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


def print_json(msg):
    print(compact_json(msg))


if args.unix:
    if os.path.exists(args.unix):
        pool = redis.ConnectionPool(connection_class=redis.UnixDomainSocketConnection,
				    path=args.unix, 
				    password=args.redis_pass)
    else:
        message = 'ZBX_NOTSUPPORTED: {} File Not Found'.format(args.unix)
        print_json(message)
        sys.exit(1)
else:
    pool = redis.ConnectionPool(host=args.redis_host, port=args.redis_port, password=args.redis_pass)


try:
    with redis.Redis(connection_pool=pool) as client:
        if args.ping:
            ping = client.ping()
            if ping:
                print(1)
            else:
                print(0)

        if args.info:
            for section in sections:
                info[section] = client.info(section)
            print_json(info)

        if args.slowlog:
            number = client.slowlog_len()
            print(number)

        if args.config:
            config = client.config_get()
            print_json(config)

except redis.AuthenticationError as err:
    message = {'ZBX_NOTSUPPORTED': err}
    print_json(message)
    sys.exit(1)
except redis.ConnectionError as err:
    message = {'ZBX_NOTSUPPORTED': err}
    print_json(message)
    sys.exit(1)
except redis.RedisError as err:
    message = {'ZBX_NOTSUPPORTED': err}
    print_json(message)
    sys.exit(1)

sys.exit()
