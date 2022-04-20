from pysgi import PySGI
from pysgi import Response
from pysgi.plugins import IPFilter

server = PySGI()

filter = IPFilter()
filter.add_permitted('127.0.0.1')

# whenever you are using plugins, you need to declare
# the "request" argument in the routes that use the plugin.

@server.route('/user')
def user(request):
    return 'Hello, user!'


@server.route('/admin')
@filter.ipfilter
def admin(request):
    return 'Hello, admin!'


server.run(host='0.0.0.0')
