import sys
import unittest

sys.path.insert(0, './')

from pysgi.response import make_response

class TestPySGI(unittest.TestCase):
    def test_make_response(self):
        headers = {'Content-Type': 'text/plain', 'Auth': '120h'}
        cookies = {'authJwt': 'ey2723base', 'sessionId': '2324'}

        response = make_response('Hello', status=200, headers=headers, cookies=cookies)
        expected_response = 'HTTP/1.1 200\n'\
                            'Server: PySGI\n'\
                            'Content-Type: text/plain\n'\
                            'Auth: 120h\n'\
                            'Set-Cookie: authJwt=ey2723base; sessionId=2324\n\n'\
                            'Hello'

        self.assertEqual(response, expected_response, msg='Expected response not equal')


if __name__ == '__main__':
    unittest.main()
