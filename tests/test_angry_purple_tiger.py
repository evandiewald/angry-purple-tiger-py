from angry_purple_tiger import __version__
from angry_purple_tiger import animal_hash


def test_version():
    assert __version__ == '0.2.0'


def test_hash():
    # input strings must be encoded
    name = animal_hash('112CuoXo7WCcp6GGwDNBo6H5nKXGH45UNJ39iEefdv2mwmnwdFt8'.encode())
    assert name == 'feisty-glass-dalmatian'

