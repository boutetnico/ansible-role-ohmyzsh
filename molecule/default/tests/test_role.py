import pytest


@pytest.mark.parametrize(
    "username",
    [
        "test_usr1",
        "test_usr2",
    ],
)
def test_oh_my_zsh_install(host, username):
    oh_my_zsh = host.file("/home/" + username + "/.oh-my-zsh")
    assert oh_my_zsh.exists
    assert oh_my_zsh.is_directory
    assert oh_my_zsh.user == username
    assert oh_my_zsh.group in [username, "users"]


@pytest.mark.parametrize(
    "username,theme,plugins,alias,extra",
    [
        (
            "test_usr1",
            "test_theme1",
            "test_plugin1 test_plugin2",
            "test_alias2",
            "test_line2",
        ),
        (
            "test_usr2",
            "test_theme2",
            "test_plugin3 test_plugin4",
            "test_alias1",
            "test_line1",
        ),
    ],
)
def test_oh_my_zsh_config(host, username, theme, plugins, alias, extra):
    zshrc = host.file("/home/" + username + "/.zshrc")
    assert zshrc.exists
    assert zshrc.is_file
    assert zshrc.user == username
    assert zshrc.group in [username, "users"]
    assert zshrc.contains(theme)
    assert zshrc.contains(plugins)
    assert zshrc.contains(alias)
    assert zshrc.contains(extra)


def test_console_setup(host):
    # console-setup is Debian family specific
    if host.file("/etc/debian_version").exists:
        setup = host.file("/etc/default/console-setup")
        assert setup.exists
        assert setup.is_file
        assert setup.user == "root"
        assert setup.group == "root"
        assert setup.contains('CHARMAP="UTF-8"')


@pytest.mark.parametrize(
    "username,theme",
    [
        ("test_usr1", "test_theme1.zsh-theme"),
    ],
)
def test_oh_my_zsh_custom_theme(host, username, theme):
    theme = host.file("/home/" + username + "/.oh-my-zsh/custom/themes/" + theme)
    assert theme.exists
    assert theme.is_file
    assert theme.user == username
    assert theme.group in [username, "users"]


@pytest.mark.parametrize("username", ["test_usr1", "test_usr2"])
def test_zsh_package_installed(host, username):
    """Test that zsh is installed for the users."""
    pkg = host.package("zsh")
    assert pkg.is_installed


@pytest.mark.parametrize("username", ["test_usr1", "test_usr2"])
def test_user_shell_is_zsh(host, username):
    """Test that user's shell is set to zsh."""
    user = host.user(username)
    assert user.shell == "/bin/zsh"


@pytest.mark.parametrize("username", ["test_usr1", "test_usr2"])
def test_oh_my_zsh_directory_structure(host, username):
    """Test that oh-my-zsh directory structure exists."""
    base_dir = f"/home/{username}/.oh-my-zsh"
    for subdir in ["custom", "custom/themes", "custom/plugins", "lib", "tools"]:
        d = host.file(f"{base_dir}/{subdir}")
        assert d.exists
        assert d.is_directory
