from nose.tools import *
from ex48 import parser
from ex48 import lexicon

#Test to verify the 'peek' method.
def test_peek():
	vector = [('verb', 'go')]
	assert_equal(parser.peek(vector), 'verb')

#Test to verify the match method.
def test_match():
	vector = lexicon.scan('princess')
	assert_equal(parser.match(vector, 'noun'), ('noun', 'princess'))
	vector = lexicon.scan('go')
	assert_equal(parser.match(vector, 'verb'), ('verb', 'go'))
	vector = lexicon.scan('the')
	assert_equal(parser.match(vector, 'error'), None)

#Test to verify the skip method.
def test_skip():
	vector = lexicon.scan('the')
	parser.skip(vector, 'stop')
	assert_equal(vector, [])
	vector2 = lexicon.scan('bear IAS princess')
	assert_equal(vector2, [('noun','bear'),
							('error','IAS'),
							('noun','princess')])
	parser.skip(vector2, 'noun')
	assert_equal(vector2, [('error','IAS'),
							('noun','princess')])
	parser.skip(vector2, 'error')
	assert_equal(vector2, [('noun','princess')])

#Test to verify the parse_verb method.
def test_parse_verb():
	vector = lexicon.scan('bear eat door')
	assert_raises(parser.ParseError, parser.parse_verb, vector)
	vector2 = lexicon.scan('bear IAS princess')
	assert_raises(parser.ParseError, parser.parse_verb, vector2)
	vector3 = lexicon.scan("go kill eat")
	assert_equal(parser.parse_verb(vector3), ('verb', 'go'))
	vector4 = lexicon.scan("in stop south")
	assert_equal(parser.parse_verb(vector4), ('verb', 'stop'))

#Test to verify the parse_object method.
def test_parse_object():
	vector = lexicon.scan('unknown eat door')
	assert_raises(parser.ParseError, parser.parse_object, vector)
	vector = lexicon.scan('princess go door')
	assert_equal(parser.parse_object(vector), ('noun', 'princess'))
	vector = lexicon.scan('from north')
	assert_equal(parser.parse_object(vector), ('direction', 'north'))

#Test to verify the parse_subject method.
def test_parse_subject():
	vector = lexicon.scan('kill bear jump')
	subject = ('noun','player')
	result = parser.parse_subject(vector, subject)
	assert_equal(result.subject, 'player')
	assert_equal(result.verb, 'kill')
	assert_equal(result.object, 'bear')

#Test to verify the parse_sentence method.
def test_parse_sentence():
	vector = lexicon.scan('bear kill the princess')
	result = parser.parse_sentence(vector)
	assert_equal(result.subject, 'bear')
	assert_equal(result.verb, 'kill')
	assert_equal(result.object, 'princess')
	vector2 = lexicon.scan('VDFVDS eat bear')
	assert_raises(parser.ParseError, parser.parse_sentence, vector2)
