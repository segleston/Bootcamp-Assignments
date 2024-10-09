from flask import Flask, jsonify, request
from db_utils import add_sweet, get_sweet_by_id, delete_sweet, get_sweet_by_name, add_order, get_all_sweets

app = Flask(__name__)

@app.route('/')
def hello():
    return {'hello': 'Universe'}

#Get all sweets
@app.route('/sweets', methods=['GET'])
def get_sweets():
    sweets = get_all_sweets()
    return jsonify(sweets)

#Get sweets by their ID
@app.route('/sweets/<int:sid>', methods=['GET'])
def get_sweet_by_id_route(sid):
    sweet = get_sweet_by_id(sid)
    if sweet:
        return jsonify(sweet)
    return jsonify({"message": "Sweet not found."}), 404

# Get sweet by its name
@app.route('/sweets/name/<string:name>', methods=['GET'])
def get_sweet_by_name_route(name):
    sweet = get_sweet_by_name(name)
    if sweet:
        return jsonify(sweet)
    return jsonify({"message": "Sweet not found."}), 404

#Add new sweets
@app.route('/sweets', methods=['POST'])
def add_sweets():
    sweet = request.get_json()
    sweet_id = add_sweet(sweet)
    return jsonify({"message": "Sweet added successfully!", "sweet_id": sweet_id}), 201


# Add a new order
@app.route('/orders', methods=['POST'])
def add_order_route():
    order_data = request.get_json()  # Get the order details from the request body
    try:
        customer_name = order_data['customer_name']
        sweet_ordered = order_data['sweet_ordered']
        total_cost = order_data['total_cost']

        # Call the add_order function to insert into the DB
        add_order(customer_name, sweet_ordered, total_cost)
        return jsonify({"message": "Order added successfully!"}), 201
    except KeyError as e:
        return jsonify({"error": f"Missing field in request: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": f"Failed to add order: {str(e)}"}), 500


if __name__ == '__main__':
    app.run(debug=True)
