from datetime import datetime

from flask import Blueprint, request
from flask_login import current_user

from apps.common.auth import api_signin_required
from apps.common.response import ok, error
from apps.database.models import Order, Delivery, Product, Cart
from apps.database.session import db

app = Blueprint('apis_orders', __name__, url_prefix='/apis/orders')


@app.route('', methods=['POST'])
@api_signin_required
def create_order():
    form = request.form
    product_ids = form['product_ids'].split(',')
    product_cnt = form['product_cnt'].split(',')

    delivery = Delivery.query.filter(Delivery.user_id == current_user.id).first()
    if not delivery:
        return error(40000)

    for product_id in product_ids:
        product = Product.query.filter(Product.id == product_id).first()
        if not product:
            return error(40000)

    now = datetime.now()
    for idx, product_id in enumerate(product_ids):
        for _ in range(int(product_cnt[idx])):
            order = Order(product_id=product_id, user_id=current_user.id, delivery_id=delivery.id, created_at=now)
            db.session.add(order)

    Cart.query.filter(Cart.user_id == current_user.id).delete()
    db.session.commit()
    return ok()
