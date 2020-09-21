ansible-role-oh-my-zsh
======================

This role configures oh-my-zsh.

Requirements
------------

Ansible 2.6 or newer.

Supported Platforms
-------------------

- [Debian - 9 (Stretch)](https://wiki.debian.org/DebianStretch)
- [Debian - 10 (Buster)](https://wiki.debian.org/DebianBuster)
- [Ubuntu - 18.04 (Bionic Beaver)](http://releases.ubuntu.com/18.04/)
- [Ubuntu - 20.04 (Focal Fossa)](http://releases.ubuntu.com/20.04/)

Role Variables
--------------

| Variable                     | Required | Default        | Choices   | Comments                                    |
|------------------------------|----------|--------------- |-----------|---------------------------------------------|
| oh_my_zsh_theme              | yes      | `robbyrussell` | string    | Default theme                               |
| oh_my_zsh_custom_themes      | no       |                | string    | Local path to themes files to install       |
| oh_my_zsh_plugins            | yes      | `[git]`        | list      | Default plugins                             |
| oh_my_zsh_users              | yes      | `[]`           | list      | Users to configure. See `defaults/main.yml` |
| oh_my_zsh_alias              | yes      | `[]`           | list      | Default alias                               |
| oh_my_zsh_extra_lines        | yes      | `[]`           | list      | Extra config lines in `.zshrc`              |

Dependencies
------------

None

Example Playbook
----------------

    - hosts: all
      roles:
        - ansible-role-oh-my-zsh
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
