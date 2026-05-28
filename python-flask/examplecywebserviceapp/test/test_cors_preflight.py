import unittest

from examplecywebserviceapp.__main__ import create_app


class TestCorsPreflight(unittest.TestCase):

    def setUp(self):
        self.app = create_app().app.test_client()

    def test_options_base_path_without_trailing_slash_does_not_redirect(self):
        response = self.app.open(
            '/example',
            method='OPTIONS',
            headers={
                'Origin': 'http://localhost:3000',
                'Access-Control-Request-Method': 'POST',
            })

        self.assertEqual(response.status_code, 204)
        self.assertEqual(response.data, b'')
        self.assertEqual(response.headers.get('Access-Control-Allow-Origin'), '*')
        self.assertIn('POST', response.headers.get('Access-Control-Allow-Methods'))


if __name__ == '__main__':
    unittest.main()
