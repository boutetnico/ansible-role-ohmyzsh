[![tests](https://github.com/boutetnico/ansible-role-ohmyzsh/workflows/Test%20ansible%20role/badge.svg)](https://github.com/boutetnico/ansible-role-ohmyzsh/actions?query=workflow%3A%22Test+ansible+role%22)
[![Ansible Galaxy](https://img.shields.io/badge/galaxy-boutetnico.ohmyzsh-blue.svg)](https://galaxy.ansible.com/boutetnico/ohmyzsh)

ansible-role-ohmyzsh
====================

This role installs and configures [Oh My Zsh](https://github.com/ohmyzsh/ohmyzsh).

Requirements
------------

Ansible 2.10 or newer.

Supported Platforms
-------------------

- [Debian - 11 (Bullseye)](https://wiki.debian.org/DebianBullseye)
- [Debian - 12 (Bookworm)](https://wiki.debian.org/DebianBookworm)
- [Ubuntu - 22.04 (Jammy Jellyfish)](http://releases.ubuntu.com/22.04/)
- [Ubuntu - 24.04 (Noble Numbat)](http://releases.ubuntu.com/24.04/)

Role Variables
--------------

| Variable                     | Required | Default        | Choices   | Comments                                     |
|------------------------------|----------|--------------- |-----------|----------------------------------------------|
| oh_my_zsh_theme              | yes      | `robbyrussell` | string    | Default theme.                               |
| oh_my_zsh_custom_themes      | no       |                | string    | Local path to themes files to install.       |
| oh_my_zsh_plugins            | yes      | `[git]`        | list      | Default plugins.                             |
| oh_my_zsh_users              | yes      | `[]`           | list      | Users to configure. See `defaults/main.yml`. |
| oh_my_zsh_alias              | yes      | `[]`           | list      | Default alias.                               |
| oh_my_zsh_extra_lines        | yes      | `[]`           | list      | Extra config lines in `.zshrc`.              |

Dependencies
------------

None

Example Playbook
----------------

    - hosts: all
      roles:
        - ansible-role-ohmyzsh
          oh_my_zsh_theme: bira
          oh_my_zsh_custom_themes: files/oh-my-zsh/themes/*.zsh-theme
          oh_my_zsh_plugins:
            - git
            - ansible
          oh_my_zsh_users:
            - username: admin
            - username: root
              oh_my_zsh:
                theme: simple
                plugins:
                  - composer
                  - aws
                alias:
                  - 'cu="composer update"'
                extra_config:
                  - "export TOKEN=S3CR3T"
          oh_my_zsh_alias:
            - 'du="docker-compose up"'
          oh_my_zsh_extra_lines:
            - "git config --global oh-my-zsh.hide-status 1"

Testing
-------

    molecule test

License
-------

MIT

Author Information
------------------

Forked from original work of `John Freeman` modified by [@boutetnico](https://github.com/boutetnico).
