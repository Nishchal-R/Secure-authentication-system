# auth.py
# Authentication module for the secure user authentication system.
# Handles user registration, login, password hashing, and user data persistence.

import json
import os

# Path to the JSON file where user credentials are stored
USER_DB = "users.json"


class User:
    """Represents a user account with a username, hashed password, and salt."""

    def __init__(self, username, password_hash, salt):
        """Initialise an User instance.
            username (str): The user's login name.
            password_hash (str): The hashed password string.
            salt (str): The hex-encoded salt used during hashing.
        """
        self.username = username
        self.password_hash = password_hash
        self.salt = salt

    def to_dict(self):
        """Convert the User object to a dictionary for JSON serialisation.
            dict: A dictionary containing username, password_hash, and salt.
        """
        return {
            "username": self.username,
            "password_hash": self.password_hash,
            "salt": self.salt,
        }


def hash_password(password):
    """Hash a password securely using a salt.

    TODO: implement secure password hashing with salt.

        tuple: (hashed_password_hex, salt_hex) or None if not implemented.
    """
    pass


def verify_password(password, stored_hash, salt):
    """Verify a plaintext password against a stored hash and salt.

    TODO: verify a password against a stored hash by re-hashing and comparing.

        bool: True if the password matches, False otherwise.
    """
    pass


def load_users(filepath=USER_DB):
    """Load the user database from a JSON file.
        dict: A dictionary of user records keyed by username.
        Returns an empty dict if the file does not exist.
    """
    if not os.path.exists(filepath):
        return {}
    with open(filepath, "r") as f:
        return json.load(f)


def save_users(users, filepath=USER_DB):
    """Save the user database to a JSON file.

        users (dict): The dictionary of user records to persist.
    """
    with open(filepath, "w") as f:
        json.dump(users, f, indent=2)


def register_user(username, password):
    """Register a new user account.

    TODO: implement user registration — check for duplicates, hash the password,
    create a User object, and save it to the database.

        bool or None: True on success, False if the user already exists.
    """
    pass


def login_user(username, password):
    """Authenticate a user by verifying their credentials.

    TODO: implement login — load the user record, re-hash the provided password,

    and compare it against the stored hash.

        bool or None: True if authentication succeeds, False otherwise.
    """
    pass