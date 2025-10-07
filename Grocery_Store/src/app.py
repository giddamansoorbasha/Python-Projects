from flask import Flask, jsonify, request, abort, send_from_directory

app = Flask(__name__, static_folder='static', static_url_path='')

products = []
current_id = 1

@app.route('/products', methods=['GET'])
def get_all_products():
    return jsonify(products)

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product_by_id(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        return jsonify(product)
    else:
        abort(404, description="Product not found")

@app.route('/products', methods=['POST'])
def create_product():
    global current_id
    data = request.get_json()
    if not data or not data.get('name') or not data.get('price'):
        abort(400, description="Name and price are required")
    new_product = {
        'id': current_id,
        'name': data.get('name'),
        'price': data.get('price'),
        'description': data.get('description', '')
    }
    products.append(new_product)
    current_id += 1
    return jsonify(new_product), 201

@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    data = request.get_json()
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        product['name'] = data.get('name', product['name'])
        product['price'] = data.get('price', product['price'])
        product['description'] = data.get('description', product['description'])
        return jsonify(product)
    else:
        abort(404, description="Product not found")

@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    global products
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        products = [p for p in products if p['id'] != product_id]
        return '', 204
    else:
        abort(404, description="Product not found")

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(debug=True)