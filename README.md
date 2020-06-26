wait-for-cassandra
==================

[![Build Status](https://travis-ci.org/smok-serwis/wait-for-cassandra.svg)](https://travis-ci.org/smok-serwis/wait-for-cassandra)
[![PyPI](https://img.shields.io/pypi/pyversions/wait-for-cassandra.svg)](https://pypi.python.org/pypi/wait-for-cassandra)
[![PyPI version](https://badge.fury.io/py/wait-for-cassandra.svg)](https://badge.fury.io/py/wait-for-cassandra)
[![PyPI](https://img.shields.io/pypi/implementation/wait-for-cassandra.svg)](https://pypi.python.org/pypi/wait-for-cassandra)

This is a quick'n'dirty utility to wait for a Cassandra instance 
to become available. This proves to be an issue in CI development,
where jobs that are tested for Cassandra need to wait for it
to become available. Well, no problem with that!

# Installation

`pip install wait-for-cassandra`

# Usage

`wait-for-cassandra <optional hostname> <optional timeout>`

Default hostname is localhost, and default timeout is 5 minutes 
(300 seconds).

If you need to specify an user and a password, call this tool like this:

`wait-for-cassandra <hostname> <timeout> <login> <password>`

Or alternatively you can use it programmatically:

```python
from wait_for_cassandra import wait_for_cassandra

wait_for_cassandra('host', 300, 'login', 'password')
```
