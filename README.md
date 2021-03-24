# geekoops-pureftpd

Install and configure the secure `PureFTPd` server.

## Role Variables


## Example Playbook

    - hosts: jellyfish
      roles:
         - { role: geekoops-pureftp }

## License

MIT

## Author Information

phoenix

Have a lot of fun!

# Development

## Add githooks

This repository ships pre-commit git hooks that will check the yaml syntax. To configure them do

    git config --local core.hooksPath .githooks/