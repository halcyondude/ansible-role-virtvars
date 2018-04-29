ansible-role-virtvars
=====================

[![Build Status](https://travis-ci.org/halcyondude/ansible-role-virtvars.svg?branch=master)](https://travis-ci.org/halcyondude/ansible-role-virtvars) 
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Ansible role which sets host variables useful when interacting with libvirt

The role presently supports one specific scenario:

- Given a list of domain names, find MAC addresses using [Ansible's virt module](http://docs.ansible.com/ansible/latest/modules/virt_module.html)
- Query the virthost's ARP table with [python_arptable](http://python-arptable.readthedocs.io) to find domain IP addresses
- Set facts/variables that can be used in subsequent roles/tasks.

This is useful for the [tripleo-quickstart](https://github.com/openstack/tripleo-quickstart) project, an Ansible based project for setting up [TripleO](http://tripleo.org) environments in openstack CI.

Requirements
------------

- [python_arptable](https://pypi.org/project/jmespath)
- [jmespath](https://pypi.org/project/python_arptable)

Role Variables
--------------

:construction_worker: :construction_worker: :construction_worker: 

Dependencies
------------

- No other galaxy roles are required.
- http://docs.ansible.com/ansible/latest/modules/virt_module.html
- https://docs.ansible.com/ansible/2.4/xml_module.html
- https://pypi.org/project/jmespath
- https://pypi.org/project/python_arptable

Example Playbook
----------------

:construction_worker: :construction_worker: :construction_worker: 

License
-------

Apache 2.0

Author Information
------------------

Matt Young ([@halcyondude](https://github.com/halcyondude))