from logger import log_event

class UserManager:
    def __init__(self):
        self.users = []

    def load_users(self, user_list):
        self.users = user_list
        log_event("USERS_LOADED", f"{len(user_list)} users loaded.")
        print(f"Users added: {self.users}\n")

    def get_all_users(self):
        return self.users
