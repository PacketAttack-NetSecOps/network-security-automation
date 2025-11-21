#!/bin/bash
countryList="us"
firewallGroupName=countries_allowed

#mkdir /config/zonefiles
function loadcountry () {
        firewallGroupName=$1
        country=$2

        echo "Downloading country definition for $country..." >> /var/log/alex
        wget http://www.ipdeny.com/ipblocks/data/countries/${country}.zone -O /config/zonefiles/${country}.zone -q
        echo "Adding rules to firewall group $firewallGroupName..." >> /var/log/alex
        for rule in `cat /config/zonefiles/${country}.zone`; do
                ipset add $firewallGroupName $rule
        done
}

ipset -F $firewallGroupName
for country in $countryList; do
        loadcountry $firewallGroupName $country
done
