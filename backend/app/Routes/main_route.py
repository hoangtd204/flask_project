from flask import Blueprint, render_template
from Services.read_inf import read_student
from flask import jsonify

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')



student_bp = Blueprint('students', __name__)

@student_bp.route('/students', methods=['GET'])
def get_all_students():
    products = read_student()
    return jsonify(products)
