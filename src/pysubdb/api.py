# SubDB API library
import os
import hashlib
import requests

API_URL = 'http://api.thesubdb.com'
API_TEST_URL = 'http://sandbox.thesubdb.com'
HEADERS = {
    'User-Agent': 'SubDB/1.0 '
    '(pysubdb/0.1; https://github.com/asermax/pysubdb/tree/master)',
}


class SubDBAPI(object):
    ''' This class instances are the main entry point for SubDB API
    capabilities.
    '''
    def __init__(self, test=False):
        self.url = API_URL if not test else API_TEST_URL

    def get_hash(f):
        ''' Generates the SubDB hash for a file. '''
        readsize = 64 * 1024
        data = f.read(readsize)
        f.seek(-readsize, os.SEEK_END)
        data += f.read(readsize)
        return hashlib.md5(data).hexdigest()

    def _make_request(self, action, **params):
        ''' Auxiliary method that contains the logic to make the requests
        against the API.
        '''
        params['action'] = action

        r = requests.get(self.url, headers=HEADERS, params=params)

        if r.status_code == 200:
            return r.text

    def search(self, video_hash, versions=False):
        ''' Lists the available languages for a certain file given it's hash.
        '''
        params = {
            'hash': video_hash,
        }

        if versions:
            params['versions'] = ''

        return self._make_request('search', **params)

    def download(self, video_hash, language):
        ''' Returns the subtitle text for a file given it's hash and a required
        language.
        '''
        params = {
            'hash': video_hash,
            'language': language,
        }

        return self._make_request('download', **params)
