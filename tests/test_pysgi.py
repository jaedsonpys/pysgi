import unittest
from pysgi import Response


class TestPySGI(unittest.TestCase):
    def test_response(self):
        response = Response('Hello', status=200)
        response.set_cookie('authJWT', 'ey2808')
        response.set_header('Authorization', 'Bearer 28082044d2')

        self.assertEqual(response.cookies, {'authJWT', 'ey2808'}, msg='Expected cookies not equal')


if __name__ == '__main__':
    unittest.main()
