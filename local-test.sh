#!/usr/bin/env bash

set -x

#
# run a local test of the role.  Caveat Emptor! YMMV.
#
# 1. install libvirtd and start it
# 2. download cirros image and create a few (small) domains (tiny0, tiny2)
# 3. run the role
#

ANSIBLE_ROLES_PATH=../
ansible-playbook -i tests/inventory tests/local-test.yml
