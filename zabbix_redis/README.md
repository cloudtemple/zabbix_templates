This is official zabbix template for zabbix 4.4 with minor changes. Set of scripts and user parameters copies behaviour of zabbix_agent2. This is needed when you stuck with CentOS7 and old zabbix_agent. 

Requires python3. Tested with python-redis >= 3.4.1

Redis server side:
* Copy files to corresponding directories. Restart agent

Zabbix UI.
* If you have password protected redis server add it as a template macros ${REDIS.AUTH}


