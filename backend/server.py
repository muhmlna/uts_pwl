from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.view import view_config

import pyramid_default_cors

import produk


@view_config(route_name='index', renderer='json')
def index(request):
    data = []
    if 'id' in request.GET:
        id = request.GET['id']
        data = produk.get_products(id)
    else:
        data = produk.get_products()
    if data == []:
        return {'message': 'data tidak ditemukan', 'status': 404}
    request.response.headers.extend({'Access-Control-Allow-Origin': '*'})
    return {'message': 'success', 'status': 200, 'data': data}


@view_config(route_name='index', request_method='POST', renderer='json')
def add(request):
    name = request.POST['name']
    price = request.POST['price']
    stock = request.POST['stock']
    if name == '' or price == '' or stock == '':
        return {'message': 'data tidak lengkap', 'status': 400}
    produk.add_product(name, price, stock)
    request.response.headers.extend({'Access-Control-Allow-Origin': '*'})
    return {'message': 'data berhasil ditambahkan', 'status': 200}


@view_config(route_name='index', request_method='PUT', renderer='json')
def update(request):
    request.response.headers.extend({'Access-Control-Allow-Origin': '*'})
    id = request.POST['id']
    name = request.POST['name']
    price = request.POST['price']
    stock = request.POST['stock']
    if id == '' or name == '' or price == '' or stock == '':
        return {'message': 'data tidak lengkap', 'status': 400}
    produk.update_product(id, name, price, stock)
    return {'message': 'success', 'status': 200}


@view_config(route_name='index', request_method='DELETE', renderer='json')
def delete(request):
    request.response.headers.extend({'Access-Control-Allow-Origin': '*'})
    id = request.POST['id']
    if id == '':
        return {'message': 'data tidak lengkap', 'status': 400}
    produk.delete_product(id)
    return {'message': 'success', 'status': 200}

# @view_config(route_name='buy', renderer='json', request_method='POST')
# def buy(request):
#     ids = request.POST['ids[]']
#     qtys = request.POST['qtys[]']
#     if ids == [] or qtys == []:
#         return {'message': 'data tidak lengkap', 'status': 400}
#     # ids = ids.split(',')
#     # qtys = qty.split(',')
#     total = produk.get_total(ids, qtys)
#     produk.buy(ids, qtys)
#     return {'message': 'success', 'status': 200, 'total': total}


@view_config(route_name='get_total_price', renderer='json', request_method='POST')
def get_total_price(request):
    request.response.headers.extend({'Access-Control-Allow-Origin': '*'})
    ids = request.POST['ids[]']
    qtys = request.POST['qtys[]']
    if ids == [] or qtys == []:
        return {'message': 'data tidak lengkap', 'status': 400}
    # ids = ids.split(',')
    # qtys = qty.split(',')
    total = produk.get_total(ids, qtys)
    return {'message': 'success', 'status': 200, 'total': total}


if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('index', '/')
        config.add_route('get_total_price', '/get_total_price')
        config.scan()
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 6969, app)
    server.serve_forever()
