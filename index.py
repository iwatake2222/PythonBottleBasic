#!/bin/env python
# coding: utf-8
import os
import sys
import json
from bottle import route, run, request, HTTPResponse, static_file


@route('/')
def root():
	return 'Hello'


# http://localhost:8080/getTest?prm1=aaa&prm2=bbb
# curl -X GET http://localhost:8080/getTest?'prm1=aaa&prm2=bbb'
@route('/getTest', method='GET')
def getTest():
	print request
	var1 = request.query.prm1
	var2 = request.query.prm2
	retBody = 'Hello Get ' + var1 + ', ' + var2
	r = HTTPResponse(status=200, body=retBody)
	r.set_header('Content-Type', 'text/html')
	return r


# curl -X POST -d prm1=aaa -d prm2=bbb http://localhost:8080/postTest
@route('/postTest', method='POST')
def postTest():
	var1 = request.forms.get('prm1')
	var2 = request.forms.get('prm2')
	retBody = 'Hello Post ' + var1 + ', ' + var2
	r = HTTPResponse(status=200, body=retBody)
	r.set_header('Content-Type', 'text/html')
	return r


# curl -H "Accept: application/json" -H "Content-type: application/json" -X POST -d '{"prm1":"aaa", "prm2":"bbb"}' http://localhost:8080/postTestJson
@route('/postTestJson', method='POST')
def postTestJson():
	var = request.json
	retBody = {
		"ret": "ok",
		"retPrm": "XX " + var["prm1"] + var["prm2"],
	}
	r = HTTPResponse(status=200, body=retBody)
	r.set_header('Content-Type', 'application/json')
	return r


if __name__ == '__main__':
	print('Server Start')
	#run(host='0.0.0.0', port=8080, debug=True, reloader=True)
	run(host='0.0.0.0', port=8080, debug=True, reloader=False)
