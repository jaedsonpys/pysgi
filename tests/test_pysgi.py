import unittest
from pysgi import Response
from pysgi.response import make_response


class TestPySGI(unittest.TestCase):
    def test_response(self):
        response = Response('Hello', status=200)
        response.set_cookie('authJWT', 'ey2808')
        response.set_header('Authorization', 'Bearer 28082044d2')

        self.assertEqual(response.cookies, {'authJWT': 'ey2808'}, msg='Expected cookies not equal')

    def test_make_response(self):
        expected_message = 'HTTP/1.1 200\n' \
                           'Server: PySGI\n' \
                           'Content-Type: text/html\n' \
                           'Authorization: Bearer 28082044d2\n' \
                           'Set-Cookie: authJWT=ey2808\n\n' \
                           'Hello'

        response = Response('Hello', status=200)
        response.set_cookie('authJWT', 'ey2808')
        response.set_header('Authorization', 'Bearer 28082044d2')

        http_message = make_response(response)
        self.assertEqual(http_message, expected_message, msg='Expected HTTP message not equal')


if __name__ == '__main__':
    unittest.main()
