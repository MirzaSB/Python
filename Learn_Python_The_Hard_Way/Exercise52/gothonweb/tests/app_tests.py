from nose.tools import *
from bin.app import app
from tests.tools import assert_response
import unittest

def test_index():
	# Check that we got a 404 in the / URL.
	resp = app.request("/")
	assert_response(resp, status="303 See Other")

def test_paths():

	# Test our first GET request to /hello.
	params = "tell+a+joke"
	resp = app.request("/game", method="POST", data=params)
	verifyResponseCodeAndSessionCookie(resp, "200 OK", "None")

	params = "action=0131"
	resp = app.request("/game", method="POST", data=params)
	verifyResponseCodeAndSessionCookie(resp, "200 OK", "None")
	
	# Make sure that the default values work for the form.
	resp = app.request("/hello", method="POST")
	#assert_response(resp, contains="Nobody")
	verifyResponseCodeAndSessionCookie(resp, "404 Not Found", "not found")

	# Test that we get expected values.
	data = {'name': 'Zed', 'greet': 'Hola'}
	resp = app.request("/hello", method="POST", data=data)
	#assert_response(resp, contains="Zed")
	verifyResponseCodeAndSessionCookie(resp, "404 Not Found", "not found")

def verifyResponseCodeAndSessionCookie(response, expected_response_code, response_data):
	print response
	assert_response(response, status=expected_response_code)
	assert(response.data == response_data)
	assert("webpy_session_id=" in response.headers['Set-Cookie'])