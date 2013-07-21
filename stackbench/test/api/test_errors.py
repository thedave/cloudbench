#coding:utf-8
import unittest
from requests import Response

from stackbench.api.client import Client
from stackbench.api.exceptions import APIError

from stackbench.test.api import TEST_ENDPOINT, RepeatingTestAdapter


class ErrorTestCase(unittest.TestCase):
    def test_error_wrapping(self):
        """
        Test that HTTP errors are wrapped into API Errors
        """
        client = Client(TEST_ENDPOINT)
        response = Response()
        response.status_code = 500
        response.reason = "INTERNAL SERVER ERROR"
        adapter = RepeatingTestAdapter(response)

        client._session.mount(TEST_ENDPOINT, adapter)

        # We want a bit more control than just assertRaises
        try:
            client.measurements.get()
        except APIError as e:
            self.assertIsNotNone(e.response)
            self.assertEqual(500, e.response.status_code)
            self.assertEqual("INTERNAL SERVER ERROR", e.response.reason)
            self.assertIsNotNone(e.__cause__)
        else:
            self.fail("No APIError was raised")