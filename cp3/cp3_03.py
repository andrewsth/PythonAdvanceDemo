# _*_ coding:utf-8_*_
# import something
try:
    from cStrngIO import StringIO
except ImportError:
    from StringIO import StringIO

# task
try:
    import json
except ImportError:
    import simplejson as json

print json.dumps({'python': 2.7})
