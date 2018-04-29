#!/usr/bin/python

# Copyright (c) 2018, Matt Young
# Subject to Apache License 2.0. (See LICENSE or http://www.apache.org/licenses/LICENSE-2.0)

#
# to test this module locally
#
# http://docs.ansible.com/ansible/latest/dev_guide/developing_modules_general.html#local-direct-module-testing
#
# TL;DR
#
# virtualenv .venv && source .venv/bin/activate && pip install python_arptable
# git clone git@github.com:ansible/ansible.git
# source {ansible_root}/hacking/env-setup
# python ./arptable_ip_from_mac.py ./arptable_ip_from_mac.testargs.json
#

ANSIBLE_METADATA = {
    'metadata_version': '1.0',
    'status': ['preview'],
    'supported_by': 'community'
}

DOCUMENTATION = '''
---
module: arptable_ip_from_mac

short_description: Retrieve IP address from ARP table for the given MAC

version_added: "2.4.1"

description:
    - ARP table is read with python_arptable (http://python-arptable.readthedocs.io)
    - An array of IP's matching MAC is returned

options:
    mac_address:
        description:
            - MAC address to search for in the target ARP table
        required: true
requirements:
    - python-arptable

author:
    - Matt Young (@halcyondude)
'''

RETURN = '''
ip_address:
    description: The IP found for the given MAC address
    type: str
'''

from ansible.module_utils.basic import AnsibleModule
from python_arptable import ARPTABLE

def search_arptable(mac, table=ARPTABLE):
    """Scan ARP table, returning array of IPs for 'mac', or None if not found.

    An example one row ARP table is:

    [{   'Device': 'virbr0',
         'Flags': '0x2',
         'HW address': '52:54:00:71:fb:51',
         'HW type': '0x1',
         'IP address': '192.168.122.15',
         'Mask': '*'}]

    It is possible to have multiple IP addresses in the ARP table due
    to IP aliasing, libvirt domain clone / snapshot / restore, etc...

    This function returns all that match (though it'll nearly always be one)
    so a warning can be raised by the caller.  As this functionality exists
    to support libvirt scenarios, duplicate MAC's are quite possible.
    """

    ip_list = [row['IP address'] for row in table if row['HW address'] == mac]

    return ip_list

def run_module():
    # arguments/parameters that a user can pass to the module
    module_args = dict(
        mac_address=dict(type='str', required=True),
    )

    # this module does not make stateful changes to the target (changed param)
    result = dict(
        changed=False,
        ip_address='',
    )

    # the AnsibleModule object will be our abstraction working with Ansible
    # this includes instantiation, a couple of common attr would be the
    # args/params passed to the execution, as well as if the module
    # supports check mode
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # no stateful changes are made to target, so 'changed' is never 'True'
    result['changed'] = False

    mac = module.params['mac_address']

    ip_list = search_arptable(mac)

    if not ip_list:
        module.fail_json(msg="No IP was found for the MAC: %s" % mac, **result)

    if len(ip_list) > 1:
            module.warn("WARNING: Duplicate IP addresses for MAC '%s': %s " % (mac, ', '.join(ip_list)))

    result['ip_address'] = ip_list[0]
    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()