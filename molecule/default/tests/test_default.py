import os

import testinfra.utils.ansible_runner

import pytest

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('name', [
    ('openssh-server'),
    ('fail2ban'),
])
def test_package_is_installed(host, name):
    package = host.package(name)
    assert package.is_installed


@pytest.mark.parametrize('name', [
    ('ssh'),
    ('fail2ban'),
])
def test_service_is_running(host, name):
    service = host.service(name)
    assert service.is_running


@pytest.mark.parametrize('name', [
    ('ssh'),
    ('fail2ban'),
])
def test_service_is_enabled(host, name):
    service = host.service(name)
    assert service.is_enabled


@pytest.mark.parametrize('port', [
    ('22'),
])
def test_socket(host, port):
    assert host.socket('tcp://0.0.0.0:' + port).is_listening


@pytest.mark.parametrize('line', [
    ('PermitRootLogin no'),
    ('PasswordAuthentication no'),
])
def test_ssh_config(host, line):
    file = host.file('/etc/ssh/sshd_config')
    assert file.exists
    assert file.contains(line)
