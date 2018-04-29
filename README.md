Role Name
=========

Ansible role which sets host variables useful when interacting with libvirt

Requirements
------------

pip packages:
- python_arptable
- jmespath

Role Variables
--------------

A description of the settable variables for this role should go here, including any variables that are in defaults/main.yml, vars/main.yml, and any variables that can/should be set via parameters to the role. Any variables that are read from other roles and/or the global scope (ie. hostvars, group vars, etc.) should be mentioned here as well.

Dependencies
------------

- No other galaxy roles are required.
- http://docs.ansible.com/ansible/latest/modules/virt_module.html

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

    - hosts: servers
      roles:
         - { role: username.rolename, x: 42 }

License
-------

Apache 2.0

Author Information
------------------

Matt Young (@halcyondude)