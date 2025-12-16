import hashlib
import os

CREDENTIALS_FILE = "credentials.txt"
DELIMITER = ";"


class User:
    def __init__(self, user_id: int, username: str, password_hash: str):
        self.user_id = user_id
        self.username = username
        self.password_hash = password_hash


def hash_password(password: str) -> str:
  
    md5 = hashlib.md5()
    md5.update(password.encode("utf-8"))
    return md5.hexdigest()


def ensure_credentials_file_exists() -> None:
   
    if not os.path.exists(CREDENTIALS_FILE):
        # Luodaan tyhjä tiedosto, jos ei ole
        with open(CREDENTIALS_FILE, "w", encoding="utf-8") as f:
            pass


def load_users() -> list[User]:
    
    ensure_credentials_file_exists()
    users: list[User] = []

    with open(CREDENTIALS_FILE, "r", encoding="utf-8") as f:
        for line in f:
            row = line.strip()
            if row == "":
                continue

            parts = row.split(DELIMITER)
            # odotettu formaatti: id;username;hash
            user_id = int(parts[0])
            username = parts[1]
            password_hash = parts[2]
            users.append(User(user_id, username, password_hash))

    return users


def save_user(user: User) -> None:
  
    ensure_credentials_file_exists()
    with open(CREDENTIALS_FILE, "a", encoding="utf-8") as f:
        line = f"{user.user_id}{DELIMITER}{user.username}{DELIMITER}{user.password_hash}\n"
        f.write(line)


def register_user() -> None:
    """Hoitaa rekisteröitymisen."""
    username = input("Insert username: ")
    password = input("Insert password: ")

    password_hash = hash_password(password)

    users = load_users()
 
    new_id = len(users)

    new_user = User(new_id, username, password_hash)
    save_user(new_user)

    print("User registration completed!")
    print()  


def login_user() -> None:
   
    username = input("Insert username: ")
    password = input("Insert password: ")
    password_hash = hash_password(password)

    users = load_users()

    logged_in_user: User | None = None

    for user in users:
        if user.username == username and user.password_hash == password_hash:
            logged_in_user = user
            break

    if logged_in_user is None:
        print("Login failed: invalid username or password.")
        print()
        return

    print(f"Welcome, {logged_in_user.username}!")
    print()
    user_menu(logged_in_user)


def user_menu(user: User) -> None:
  
    while True:
        print("User menu:")
        print("1 - View profile")
        print("2 - Change password")
        print("0 - Logout")
        choice = input("Your choice: ")

        if choice == "1":
            view_profile(user)
        elif choice == "2":
            change_password_stub()
        elif choice == "0":
            print("Logging out.")
            print()
            break
        else:
            print("Invalid choice.")
            print()


def view_profile(user: User) -> None:
    print("User profile:")
    print(f" - ID: {user.user_id}")
    print(f" - Username: {user.username}")
    print(f" - Password hash: {user.password_hash}")
    print()


def change_password_stub() -> None:
    print("Change password is not implemented.")
    print()


def main_menu() -> None:
   
    while True:
        print("Options:")
        print("1 - Login")
        print("2 - Register")
        print("0 - Exit")
        choice = input("Your choice: ")

        if choice == "1":
            login_user()
        elif choice == "2":
            register_user()
        elif choice == "0":
            print("Exiting program.")
            print()
            break
        else:
            print("Invalid choice.")
            print()


def main() -> None:
    print("Program starting.")
    main_menu()
    print("Program ending.")


if __name__ == "__main__":
    main()
