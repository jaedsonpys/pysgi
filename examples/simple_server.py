from pysgi import PySGI
from pysgi import make_response

server = PySGI()


@server.route('/')
def index():
    return make_response('Hello World from PySGI!')


@server.route('/methods', methods=['GET', 'POST'])
def methods(request):
    if request.method == 'GET':
        response = make_response('Method GET used')
    elif request.method == 'POST':
        response = make_response('Method POST used')

    return response


if __name__ == '__main__':
    server.run()
