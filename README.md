See also [osm_bot_abstraction_layer](https://github.com/matkoniecz/osm_bot_abstraction_layer) and [osmapi](https://github.com/metaodi/osmapi) 

This is intended as a minimal wrapper over OSM Editing API, to make easy to understand what is going on.

It contains thin wrapper only for parts that I needed so far.

Sister of [taginfo equivalent](https://github.com/matkoniecz/taginfo_api_wrapper_in_python).

# Usage examples

```
import thin_osm_api_wrapper

object_type = "way"
id = 10101010
print(thin_osm_api_wrapper.api.history_json(object_type, object_id))
```

# pypi

See [https://pypi.org/project/thin-osm-api-wrapper/](https://pypi.org/project/thin-osm-api-wrapper/)

# Run tests

```
python3 -m unittest
```
