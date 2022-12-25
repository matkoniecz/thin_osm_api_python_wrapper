import requests

def history_json(object_type, object_id):
    url = 'https://api.openstreetmap.org/api/0.6/' + object_type + '/' + str(object_id) + '/history.json'
    params = {
        'user_agent': 'who_added_this_tag_script'
    }
    json_data = {}
    r = make_get_request(url, params, json_data)
    if r.status_code != 200:
        print(r.status_code)
    return r.json()['elements']

def make_get_request(url, params, json_data):
    # unifiy it with overpass downloader code?
    while True:
        try:
            return requests.get(url, params=params, json=json_data)
        except requests.exceptions.ConnectionError as e:
            print(e)
            sleep_before_retry("requests.exceptions.ConnectionError", url, params, json_data)
            continue
        except requests.exceptions.HTTPError as e:
            print(e.response.status_code)
            if e.response.status_code == 503:
                sleep_before_retry("requests.exceptions.HTTPError", url, params, json_data)
                continue
            raise e
        except requests.exceptions.ReadTimeout as e:
            sleep_before_retry("requests.exceptions.ReadTimeout", url, params, json_data)
            continue
        except requests.exceptions.ChunkedEncodingError as e:
            print(e)
            sleep_before_retry("requests.exceptions.ChunkedEncodingError", url, params, json_data)
            continue
        # for example
        # ConnectionResetError(104, 'Connection reset by peer')
        # not sure is it happening on poor connection or explicit request by server
        # to slow down, in either case waiting a bit is a good idea
        except urllib3.exceptions.ProtocolError as e:
            print(e)
            sleep_before_retry("urllib3.exceptions.ProtocolError", url, params, json_data)
            continue
