import unittest
import thin_osm_api_wrapper

class Tests(unittest.TestCase):
    def test_basic_math(self):
        self.assertEqual(2-2, 0)

    def test_example_code(self):
        object_type = "way"
        object_id = 10101010
        print(thin_osm_api_wrapper.api.history_json(object_type, object_id))

if __name__ == '__main__':
    unittest.main()
