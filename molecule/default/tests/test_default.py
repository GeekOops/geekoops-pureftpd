#!/usr/bin/python3
# -*- coding: utf-8 -*-


import testinfra.utils.ansible_runner
import os

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')
 
def test_ftp(host):
	cmd = host.run("curl -v ftp://127.0.0.1/testfile.txt")
	assert cmd.succeeded
	assert "Happy test file" in cmd.stdout
	cmd = host.run("curl -v ftp://127.0.0.1/secrets.txt")
	assert cmd.failed
	assert "550" in cmd.stderr

