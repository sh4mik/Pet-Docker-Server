import unittest

from controller import app
from controller import dct
from service import Service


class MyTestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False

        self.app = app.test_client()
        self.assertEqual(app.debug, False)

        self.dct = dct

    def test_put(self):
        self.app.put("/storage/first", data='{"key": "value"}')
        assert self.dct['/storage/first'].decode() == '{"key": "value"}'

    def test_get(self):
        self.dct['/storage/first'] = '{"key": "value"}'
        response = self.app.get('/storage/first')
        self.assertEqual(response.data.decode(), '{"key": "value"}')

    def test_delete(self):
        self.dct['/storage/first'] = '{"key": "value"}'
        self.app.delete('/storage/first', follow_redirects=True)
        self.assertEqual(self.dct.get('/storage/first'), None)

    def test_put_returns201(self):
        response = self.app.put("/storage/first", data='{"key": "value"}')
        self.assertEqual(response.status_code, 201)

    def test_get_returns200(self):
        self.dct['/storage/first'] = {"key": "value"}
        response = self.app.get('/storage/first')
        self.assertEqual(response.status_code, 200)

    def test_get_returns404(self):
        response = self.app.get('/storage/second')
        self.assertEqual(response.status_code, 404)

    def test_delete_returns204(self):
        self.dct['/storage/first'] = {"key": "value"}
        response = self.app.delete('/storage/first', follow_redirects=True)
        self.assertEqual(response.status_code, 204)

    def test_delete_returns404(self):
        response = self.app.delete('/storage/third', follow_redirects=True)
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()
