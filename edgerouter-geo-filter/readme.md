The EdgeRouter X is old but still a great router. You can add Geo filtering by following this guide.
You can use this method to block certain countries but in my case, i only wanted to allow only US to my external facing applications.

Credits:
https://www.cron.dk/firewalling-by-country-on-edgerouter/
https://www.youtube.com/watch?v=Qn5hbdijYJM&t=3s
These guides were a bit old so i updated them. Also i believe they were testing this on a Edge Router 4. I carried this out on a smaller Edge Router X

IP Deny EDL Used - https://www.ipdeny.com/ipblocks/


I carried this out version: EdgeRouter X v2.0.9-hotfix.7


1. Create a firewall group:

ssh into your firewall

configure
set firewall group network-group countries_allowed description 'Allowed countries'
set firewall group network-group countries_allowed network 10.254.254.254/31
commit
save

Adding the network 10.254.254.254/31 is just a placeholder

2.
Still using ssh in your firewall create the script under /config/scripts/post-config.d/country-load
See file country-load in this repo.

3. On the EdgeRouter X i was getting the following error when trying to download the list: ipset v6.30: Hash is full, cannot add more elements
To resolve I had to do the following:
Create start-up script
sudo vi /config/scripts/post-config.d/custom-ipset.sh

add:
#!/bin/bash
ipset create countries_allowed hash:ip maxelem 80000

This allows additional items to be added to the group

Make the script executable:
sudo chmod +x /config/scripts/post-config.d/custom-ipset.sh

4.
Reboot the EdgeRouter X
As the router is booting up it will download the ip list.

6.
Login again, verify the list
sudo ipset -L countries_allowed

7. You can now apply the list you created to your WAN IN rule.