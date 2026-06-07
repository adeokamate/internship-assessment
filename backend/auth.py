import bcrypt
from backend.db import get_connection


def hash_password(password):
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


def check_password(password, password_hash):
    return bcrypt.checkpw(
        password.encode("utf-8"),
        password_hash.encode("utf-8")
    )


def register_user(username, password):
    username = username.strip()

    if not username or not password:
        return False, "Username and password are required."

    if len(password) < 6:
        return False, "Password must be at least 6 characters long."

    password_hash = hash_password(password)

    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            "INSERT INTO users (username, password_hash) VALUES (%s, %s)",
            (username, password_hash)
        )

        conn.commit()
        cur.close()
        conn.close()

        return True, "Registration successful. Please log in."

    except Exception as e:
        if "duplicate key" in str(e).lower():
            return False, "Username already exists."

        return False, f"Registration failed: {e}"


def login_user(username, password):
    username = username.strip()

    if not username or not password:
        return False, "Username and password are required."

    try:
        conn = get_connection()
        cur = conn.cursor()

        cur.execute(
            "SELECT password_hash FROM users WHERE username = %s",
            (username,)
        )

        result = cur.fetchone()

        cur.close()
        conn.close()

        if not result:
            return False, "User not found."

        stored_hash = result[0]

        if not check_password(password, stored_hash):
            return False, "Incorrect password."

        return True, "Login successful."

    except Exception as e:
        return False, f"Login failed: {e}"