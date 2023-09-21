from jsonapi.jsonapi import loads, dumps
import unittest

'''
How to run this file? 
In the directory of jsonapi folder (top level), 
run command: PYTHONPATH=src python3 tests/test_jsonapi.py
'''


class TestJsonAPI(unittest.TestCase):
    def test_encode_complex(self):
        data = {"complex_number": complex(1, 2)}
        encoded = dumps(data)
        self.assertIn('"__extended_json_type__": "complex"', encoded)

    def test_decode_complex(self):
        encoded = '{"complex_number": {"__extended_json_type__": "complex", "real": 1.0, "imag": 2.0}}'
        decoded = loads(encoded)
        self.assertIsInstance(decoded["complex_number"], complex)

    def test_encode_range(self):
        data = {"range_data": range(1, 10, 3)}
        encoded = dumps(data)
        self.assertIn('"__extended_json_type__": "range"', encoded)

    def test_decode_range(self):
        encoded = '{"range_data": {"__extended_json_type__": "range", "start": 1, "stop": 10, "step": 3}}'
        decoded = loads(encoded)
        self.assertIsInstance(decoded["range_data"], range)


if __name__ == '__main__':
    unittest.main()
