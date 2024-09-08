# from flask import Blueprint, jsonify, request, abort
# from models.trip_model import get_all_trips, get_trip_by_id, create_trip, delete_trip_by_id
# from app import get_db_connection

# trip_bp = Blueprint('trip_bp', __name__)

# @trip_bp.route('/trips', methods=['GET'])
# def get_trips():
#     conn = get_db_connection()
#     trips = get_all_trips(conn)
#     conn.close()
#     return jsonify(trips), 200

# @trip_bp.route('/trips/<int:id>', methods=['GET'])
# def get_trip(id):
#     conn = get_db_connection()
#     trip = get_trip_by_id(conn, id)
#     conn.close()
    
#     if not trip:
#         abort(404, description="Trip not found")
    
#     return jsonify(trip), 200

# @trip_bp.route('/trips', methods=['POST'])
# def add_trip():
#     data = request.get_json()
#     if not data or not all([data.get('name'), data.get('location'), data.get('price')]):
#         abort(400, description="Missing fields")
    
#     conn = get_db_connection()
#     trip_id = create_trip(conn, data['name'], data['location'], data['price'])
#     conn.close()
    
#     if trip_id:
#         return jsonify({"id": trip_id, "message": "Trip created successfully"}), 201
#     else:
#         abort(500, description="Failed to create trip")

# @trip_bp.route('/trips/<int:id>', methods=['DELETE'])
# def delete_trip(id):
#     conn = get_db_connection()
#     trip = get_trip_by_id(conn, id)
    
#     if not trip:
#         conn.close()
#         abort(404, description="Trip not found")
    
#     delete_trip_by_id(conn, id)
#     conn.close()
    
#     return jsonify({"message": "Trip deleted successfully"}), 200


from flask import Blueprint, jsonify, request, abort
from models.trip_model import get_all_trips, get_trip_by_id, create_trip, delete_trip_by_id

trip_bp = Blueprint('trip_bp', __name__)

@trip_bp.route('/trips', methods=['GET'])
def get_trips():
    # Import get_db_connection inside the function to avoid circular imports
    from app import get_db_connection
    conn = get_db_connection()
    trips = get_all_trips(conn)
    conn.close()
    return jsonify(trips), 200

@trip_bp.route('/trips/<int:id>', methods=['GET'])
def get_trip(id):
    from app import get_db_connection
    conn = get_db_connection()
    trip = get_trip_by_id(conn, id)
    conn.close()
    
    if not trip:
        abort(404, description="Trip not found")
    
    return jsonify(trip), 200

@trip_bp.route('/trips', methods=['POST'])
def add_trip():
    from app import get_db_connection
    data = request.get_json()
    if not data or not all([data.get('name'), data.get('location'), data.get('price')]):
        abort(400, description="Missing fields")
    
    conn = get_db_connection()
    trip_id = create_trip(conn, data['name'], data['location'], data['price'])
    conn.close()
    
    if trip_id:
        return jsonify({"id": trip_id, "message": "Trip created successfully"}), 201
    else:
        abort(500, description="Failed to create trip")

@trip_bp.route('/trips/<int:id>', methods=['DELETE'])
def delete_trip(id):
    from app import get_db_connection
    conn = get_db_connection()
    trip = get_trip_by_id(conn, id)
    
    if not trip:
        conn.close()
        abort(404, description="Trip not found")
    
    delete_trip_by_id(conn, id)
    conn.close()
    
    return jsonify({"message": "Trip deleted successfully"}), 200

