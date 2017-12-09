from pygments.util import get_bool_opt
from pygments.token import Name, Error
from pygments.filter import Filter
from pprint import pprint

class ServiceFilter(Filter):

    def __init__(self, **options):
        Filter.__init__(self, **options)

    def filter(self, lexer, stream):
	error = ''
        for ttype, value in stream:
	    if ttype == Error:
		error = value
		continue
	    if error != '':
		value = "'" + error + value + "'"
		error = ''
            yield ttype, value