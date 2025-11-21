# zscaler-json-to-txt
Python script that parses Zscaler's dynamically updated json files for CIDR blocks then exports them to a .txt file. The .txt file can be used to dynamically add to firewall ACL and SSL decryption bypass.

Zscaler Config Page: https://config.zscaler.com/
In the file we are selecting the json specific to zscalertwo.net = https://config.zscaler.com/api/zscalertwo.net/cenr/json
Also ZPA = https://config.zscaler.com/api/private.zscaler.com/zpa/json 
