# JSONAPI

A Python package to extend the capabilities of the built-in JSON module.

## Installation

Make sure you install json library first:

```
pip3 install json
```

## Usage

```
from jsonapi import loads, dumps

data = {"complex_number": complex(1, 2)}
encoded = dumps(data)
```

How to run the test_jsonapi.py file?
In the directory of jsonapi folder (top level), run command:

```
PYTHONPATH=src python3 tests/test_jsonapi.py
```
