# angry-purple-tiger

Animal-based digests for humans... in Python.

## Overview

Angry Purple Tiger generates animal-based hash digests meant to be memorable and human-readable. Angry Purple Tiger is apt for anthropomorphizing project names, crypto addresses, UUIDs, or any complex string of characters that need to be displayed in a user interface.

This is a Python port of Helium's original [JavaScript implementation](https://github.com/helium/angry-purple-tiger).

## Installation

`pip install angry-purple-tiger`

## Usage

```python
from angry_purple_tiger import animal_hash

# input strings (like wallet addresses) must be encoded
name = animal_hash('112CuoXo7WCcp6GGwDNBo6H5nKXGH45UNJ39iEefdv2mwmnwdFt8'.encode())

print(name)
# feisty-glass-dalmation
```