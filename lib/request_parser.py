from mimetools import Message
from StringIO import StringIO

def parse(request):
	request_line, headers_alone = request.split('\r\n', 1)
	return Message(StringIO(headers_alone))