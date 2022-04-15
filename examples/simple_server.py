from pysgi import PySGI
from pysgi import make_response

server = PySGI()


@server.route('/')
def index():
    return 'Hello World from PySGI!'


@server.route('/methods', methods=['GET', 'POST'])
def methods(request):
    if request.method == 'GET':
        response = 'Method GET used'
    elif request.method == 'POST':
        response = 'Method POST used', 201  # returning body and response status

    return response


if __name__ == '__main__':
    server.run()
