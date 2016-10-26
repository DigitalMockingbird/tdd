from fabric.api import env, run


def _get_base_folder(host):
    return '~/sites/' + host


def _get_manage_dot_py(host):
    return '{path}/virtualenv/bin/python {path}/source/manage.py'.format(
        path=_get_base_folder(host)
    )


def _reset_database():
    run('{manage_py} flush --noinput'.format(
        manage_py=_get_manage_dot_py(env.host)
    ))


def create_session_on_server(email):
    session_key = run('{manage_py} create_session {email}'.format(
        manage_py=_get_manage_dot_py(env.host),
        email=email
    ))
    print(session_key)


def _update_settings(source_folder, site_name):
    settings_path = source_folder + '/superlists/settings.py'
    # sed(settings_path, "DEBUG = True", "DEBUG = False")
    # sed(settings_path, 'DOMAIN = "localhost"', 'DOMAIN = "%s"' % (site_name,))
    secret_key_file = source_folder + '/superlists/secret_key.py'
    if not secret_key_file:
        print('fabfile called. something goes past this.')
