This is official zabbix template for zabbix 4.4 with minor changes. Set of scripts and user parameters copies behaviour of zabbix_agent2. This is needed when your OS has only old zabbix_agent in repos. 

Requires python3. Tested with python-redis >= 3.4.1

It can work either with tcp or unix sockets.

Redis server side:
* Copy files to corresponding directories. Restart agent

Zabbix UI.
* If you have password protected redis server set password as a template macros ${REDIS.AUTH}


