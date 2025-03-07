from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from datetime import datetime

app = Flask(__name__)
CORS(app)
bcrypt = Bcrypt(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://admin:password@db/inventory"
app.config["JWT_SECRET_KEY"] = "your_secret_key"
jwt = JWTManager(app)
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    rfid = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

class Tool(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    barcode = db.Column(db.String(50), unique=True, nullable=False)
    status = db.Column(db.String(50), default="Available")

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    tool_id = db.Column(db.Integer, db.ForeignKey("tool.id"), nullable=False)
    action = db.Column(db.String(50), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

@app.route("/scan_rfid", methods=["POST"])
def scan_rfid():
    data = request.json
    rfid = data.get("rfid")
    return jsonify({"message": f"RFID {rfid} scanned successfully"})

@app.route("/scan_barcode", methods=["POST"])
def scan_barcode():
    data = request.json
    barcode = data.get("barcode")
    return jsonify({"message": f"Barcode {barcode} scanned successfully"})

if __name__ == "__main__":
    db.create_all()
    app.run(host="0.0.0.0", port=5000)
