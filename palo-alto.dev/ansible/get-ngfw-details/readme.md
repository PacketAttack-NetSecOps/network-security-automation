# Prep Environment #

### Install the PAN-OS Ansible collection ###

```
ansible-galaxy collection install paloaltonetworks.panos
```

### Install pandevice dependencies (if not already installed) ###

```
sudo apt install python3-pip
```
```
pip install pan-os-python
```

### Set environment variables (optional but recommended for credentials) ###

```
export PAN_HOST=192.168.1.1
export PAN_USERNAME=admin
export PAN_PASSWORD=yourpassword
```
### If you need to bypass SSL ###
add
```
verify_ssl: false
```
under
```
- name: Get system information
  panos_op:
    provider:
      ip_address: "{{ ansible_host }}"
      username: "{{ ansible_user }}"
      password: "{{ ansible_password }}"
      verify_ssl: false
    cmd: "show system info"
  register: result
```

### Now run the playbook ###

```
ansible-playbook -i inventory.yml get-ngfw-details.yml
```