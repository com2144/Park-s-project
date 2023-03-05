name = 'cityEnviroment'

version = '0.0.1'

description = \
    """
    Fundamental package for array computing in Python
    """

requires = [
    're',
    'ephem',
    'requests',
    'geopy'
]

variants = [['platform-linux', 'python-3.9']]


def commands():
    env.PYTHONPATH.append('{root}/python')
