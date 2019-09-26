# zabbix-routeros-bgp
Python monitoring Mikrotik BGP peer state and uptime on Zabbix

The script is based on MrCirca/zabbix-routeros-bgp and LaiArturs/RouterOS_API.



# Monitoring Mikrotik BGP peer state and uptime on Zabbix
![Logo of ZABBIX](http://www.zabbix.com/img/logo/zabbix_logo_150x39.png) ![Logo of Mikrotik](https://www.mikrotik.com/logo/files/logo_spacing.jpg)<br>
Using external script method on Zabbix, I made a python script that use LaiArtus RouterOS API.

Files you need to copy to externalscripts path of zabbix server:

1) bgp_peer.py Calls the API and prints state, uptime and peer names.
3) git clone https://github.com/LaiArturs/RouterOS_API.git

*Make sure that the files above are executable by zabbix user.*

You should also import **zbx_routeros_bgp.xml** zabbix template on zabbix server.


**Simple script test**:

```shell
 bgp_peer.py names|uptime|host <RouterOS_HOSTNAME or IP> <RouterOS_USERNAME> <RouterOS_PASSWORD> <BGP_peer_name>
```

**Zabbix Discovery Key**:


bgp_peer.py["names|uptime|host", "{HOST.CONN}","{$ROUTEROS_USERNAME}","{$ROUTEROS_PASSWORD}"]

*You should define these macros:  "{$ROUTEROS_USERNAME}" and "{$ROUTEROS_PASSWORD}"
