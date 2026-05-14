@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()

    name = data.get("name")
    email = data.get("email")
    password_hash = data.get("password_hash")

    if not name or not email or not password_hash:
        return jsonify({"error":"name, email, pasword_hash are required"}), 400

    conn = get_connection()
    cursor = conn.cursor()

    try:
        sql = """
            INSERT INTO users (name, email, password_hash)
            VALUES (?, ?, ?)
        """
        cursor.execute(sql, (name, email, password_hash))
        conn.commit()

        return jsonify({
            "message":"user created",
            "user_id": cursor.lastrowid
        }),201
    except Exception as e:
        conn.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()