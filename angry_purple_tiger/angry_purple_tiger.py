from .adjectives import adjectives
from .animals import animals
from .colors import colors
from hashlib import md5
from .compress import compress
import re


def animal_hash(input: bytes):
    hex_digest = md5(input).hexdigest()

    p = re.compile('(..?)', )
    pairs = p.findall(hex_digest)
    bytes = [int(x, base=16) for x in pairs]
    compressed = compress(bytes, 3)

    adjective = adjectives[compressed[0]]
    color = colors[compressed[1]]
    animal = animals[compressed[2]]

    return f"{adjective}-{color}-{animal}"
