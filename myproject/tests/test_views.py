import unittest

from pyramid import testing


class ViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_my_view(self):
        from myproject.views.root import index
        request = testing.DummyRequest()
        info = index(request)
        self.assertEqual(info['project'], 'myproject')
