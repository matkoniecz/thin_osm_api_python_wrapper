import unittest
import thin_osm_api_wrapper
import json

class Tests(unittest.TestCase):
    def test_basic_math(self):
        self.assertEqual(2-2, 0)

    def test_example_code_history(self):
        object_type = "way"
        object_id = 10101010
        data = thin_osm_api_wrapper.api.history_json(object_type, object_id)
        print(json.dumps(data, indent=3))

    def test_example_code_changeset_listing(self):
        data = thin_osm_api_wrapper.api.changeset_list_json()
        print(json.dumps(data, indent=3))
        closed_after = "2021-12-26"
        created_before = "2021-12-27"
        data = thin_osm_api_wrapper.api.changeset_list_json(closed_after=closed_after, created_before=created_before)
        print(json.dumps(data, indent=3))

if __name__ == '__main__':
    unittest.main()
