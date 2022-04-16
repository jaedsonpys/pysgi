from pysgi import PySGI
from pysgi import Response

server = PySGI()
products = [{'id': '1', 'name': 'Shampoo', 'description': 'Best for hair', 'price': '13.90'},
            {'id': '2', 'name': 'Car', 'description': 'Car for childs', 'price': '24.50'},
            {'id': '3', 'name': 'Smartphone Xiaomi', 'description': 'High velocity', 'price': '1250.00'},
            {'id': '4', 'name': 'Notebook Acer', 'description': 'For work', 'price': '2500.90'}]


@server.route('/')
def index():
    return Response(products, content_type='application/json')


@server.route('/product')
def get_product_by_id(request):
    product_id = request.args.get('id')
    product_data = None

    for item in products:
        if item['id'] == product_id:
            product_data = item

    if product_data is None:
        response = Response({'status': 'Product not found'}, status=404, content_type='application/json')
    else:
        response = Response(product_data, content_type='application/json')

    return response


if __name__ == '__main__':
    server.run()
