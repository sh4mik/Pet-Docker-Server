import unittest

from controller import app
from service import Service


class MyTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False

        self.app = app.test_client()
        self.assertEqual(app.debug, False)

    def test_get_returns200(self):
        self.app.put("/storage/first", '{"key": "value"}')
        response = self.app.get('/storage/first')
        self.assertEqual(response.status_code, 200)

    def test_delete_returns204(self):
        self.app.put("/storage/first", '{"key": "value"}')
        response = self.app.delete('/storage/first', follow_redirects=True)

        self.assertEqual(response.status_code, 204)


if __name__ == '__main__':
    unittest.main()
