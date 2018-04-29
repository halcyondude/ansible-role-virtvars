ansible-role-virtvars
=====================

[![Build Status](https://travis-ci.org/halcyondude/ansible-role-virtvars.svg?branch=master)](https://travis-ci.org/halcyondude/ansible-role-virtvars)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Ansible role which sets host variables useful when interacting with libvirt

The role presently supports one specific scenario:

- Given a list of domain names, find MAC addresses using [Ansible's virt module](http://docs.ansible.com/ansible/latest/modules/virt_module.html).
- Query the virthost's ARP table with [python_arptable](http://python-arptable.readthedocs.io) to find domain IP addresses.
- Set facts/variables (with dynamically generated fact names) that can be used in subsequent roles/tasks.

This is useful for the [tripleo-quickstart](https://github.com/openstack/tripleo-quickstart) project, an Ansible based project for setting up [TripleO](http://tripleo.org) environments in openstack CI.

Requirements
------------

- [python_arptable](https://pypi.org/project/python_arptable) must be installed on the target machine
- libvirtd should be installed and running

Role Variables
--------------

### Input Variables

- virtvars_node_list (input, required) list of libvirt domains

```json
"virtvars_node_list": [
    "tiny0",
    "tiny2"
]
```

### Generated Variables

These variables are generated with set_fact, and can be used after invoking this role.

- virtvars_domain_list

```json
"virtvars_domain_list": [
    {
        "domain": "tiny0",
        "mac": "52:54:00:ee:d3:61"
    },
    {
        "domain": "tiny2",
        "mac": "52:54:00:2a:e5:c1"
    }
]
```

- virtvars_mac_dict

```json
"virtvars_mac_dict": {
    "tiny0": "52:54:00:ee:d3:61",
    "tiny2": "52:54:00:2a:e5:c1"
}
```

- virtvars_ip_dict

```json
"virtvars_ip_dict": {
    "tiny0": "192.168.122.249",
    "tiny2": "192.168.122.44"
}
```

Dependencies
------------

- No other galaxy roles are required.
- http://docs.ansible.com/ansible/latest/modules/virt_module.html
- https://docs.ansible.com/ansible/2.4/xml_module.html
- https://pypi.org/project/python_arptable

Example Playbook
----------------

Run the following:

```bash
ANSIBLE_ROLES_PATH=../
ansible-playbook -i tests/inventory tests/local-test.yml
```

[./tests/local-test.yml](https://github.com/halcyondude/ansible-role-virtvars/tree/master/tests/local-test.yml)

```yaml
---
- hosts: localhost
  gather_facts: no
  connection: local

 # note: this assumes these domains are created!
  vars:
    virtvars_node_list:
      - tiny0
      - tiny2

   roles:
    - ansible-role-virtvars
```

Travis CI definition: ([.travis.yml](https://github.com/halcyondude/ansible-role-virtvars/blob/master/.travis.yml))

License
-------

Apache 2.0

Author Information
------------------

Matt Young ([@halcyondude](https://github.com/halcyondude))