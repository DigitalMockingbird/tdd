import subprocess
from os import path

THIS_FOLDER = path.dirname(path.abspath(__file__))


def create_session_on_server(host, email):
    return subprocess.check_output(
        [
            'fab',
            'create_session_on_server:email={}'.format(email),
            '--host={}'.format(host),
            '--hide=everthing,status',
        ],
        cwd=THIS_FOLDER
    ).decode().strip()


def reset_database(host):
    subprocess.check_call(
        ['fab', 'reset_database', '--host={}'.format(host)],
        cwd=THIS_FOLDER
    )
