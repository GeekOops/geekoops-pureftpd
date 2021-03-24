# geekoops-pureftpd

Install and configure the secure `PureFTPd` server.

## Role Variables

| Value | Description | Default |
|-------|-------------|---------|
| `config_firewall` | Apply firewall rules | `false` |
| `firewall_zone` | Firewall zone where ftp will be allowed | public |
| `MaxClientsNumber` | Maximum number of anonymous clients | 10 |
| `MaxClientsPerIP` | Maximum clients per IP address | 3 |
| `AnonymousOnly` | Forbid user login | yes |
| `NoAnonymous` | Disallow anonymous | no |
| `PAMAuthentication` | Allow PAM authentication | no |
| `MaxIdleTime` | Maximum idle time in minutes before disconnecting | 5 |
| `MaxLoad` | Disallow anonymous download if system load is above this value | 4 |
| `PassivePortMin` | Passive port range - lower bound | 30000 |
| `PassivePortMax` | Passive port range - upper bound | 30100 |
| `ForcePassiveIP` | Use this IP for passive mode, useful if `PureFTPd` is behind a NAT | `""` (disabled) |
| `Bind` | Bind address and port (e.g. `127.0.0.1,21`) | `""` (disabled) | 
| `Bandwidth` | Max bandwidth for all users in KB/s | `""` (disabled) | 
| `TrustedIP` | Allow login only from this IP | `""` (disabled) | 
| `MaxUserSessions` | Maximum number of open session per user | 3 |
| `MaxAnonSessions` | Maximum number of open anonymous sessions | 20 |
| `IPV4Only` | Bind to IPv4 only. By default we bind to IPv4 and IPv6 | no |
| `IPV6Only` | Bind to IPv6 only. By default we bind to IPv4 and IPv6 | no |

## Example Playbook

    - hosts: jellyfish
      roles:
         - { role: geekoops-pureftp, config_firewall: true }

A more extended example

    - hosts: jellyfish
      roles:
         - role: geekoops-pureftp
           vars:
             config_firewall: true
             AnonymousOnly: yes
             PassivePortMin: 30000
             PassivePortMax: 31000
             MaxAnonSessions: 100


## License

MIT

## Author Information

phoenix

Have a lot of fun!

# Development

## Add githooks

This repository ships pre-commit git hooks that will check the yaml syntax. To configure them do

    git config --local core.hooksPath .githooks/