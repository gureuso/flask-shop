from flask import Blueprint, request

from apps.common.response import ok
from apps.database.models import Product

app = Blueprint('apis_products', __name__, url_prefix='/apis/products')


@app.route('', methods=['GET'])
def products():
    args = request.args
    page = int(args.get('page', 1))
    category_id = args.get('category_id')

    products = Product.query
    if category_id:
        products = products.filter(Product.category_id == category_id)
    products = products.order_by(Product.id.desc()).offset(page*12).limit(12).all()
    return ok([dict(id=p.id, name=p.name, category_id=p.category_id, image_url=p.image_url) for p in products])
