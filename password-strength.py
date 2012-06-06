#!/usr/bin/python
import re, sys

ismixedcase = lambda s: not (s == s.lower() or s == s.upper())
hasnonalphanumeric = lambda s: len (re.sub ("[A-Za-z0-9]", "", s)) > 0

def calcEntropy (pw):
	chunks = [4,]*1 + [2,]*7 + [1.5,] * 12
	l = len (pw)
	if l > len (chunks):
		e = reduce (lambda x,y: x + y, chunks) + (l - len (chunks))
	else:
		e = reduce (lambda x,y: x + y, chunks [0:l])
	if ismixedcase (pw) and hasnonalphanumeric (pw):
		e = e + 6
	return e

def test_calcEntropy():
	somePasswords = {
		"Tr0ub4dor&3" : 28.5,
		"correcthorsebatterystaple" : 41,
		"Correcthorsebatterystap!3" : 47,
	}
	for k in somePasswords:
		expected = somePasswords [k]
		actual = calcEntropy (k)
		assert (actual == expected)

if "-t" in sys.argv:
	test_calcEntropy()

