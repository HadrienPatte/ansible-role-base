# Ansible Role: Base

[![Build Status](https://travis-ci.com/HadrienPatte/ansible-role-base.svg?branch=master)](https://travis-ci.com/HadrienPatte/ansible-role-base)

An Ansible Role that sets up the base configuration for servers

## Requirements

None.

## Role Variables

* `base_timezone`: Timezone, defaults to `UTC`

# Dependencies

None.

# Example Playbook

```yaml
- name: Base server configuration
  hosts: all
  roles:
    - hadrienpatte.base
```

## License

MIT

## Author Information

Hadrien Patte [![PGP 0xFB500BB0](https://peegeepee.com/badge/orange/FB500BB0.svg)](https://peegeepee.com/FB500BB0)
