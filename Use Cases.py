class UserManager:
    def __init__(self, user_repository):
        self.user_repository = user_repository

    def create_user(self, email: str, password: str, role: str):
        if self.user_repository.exists(email):
            raise ValueError("User with this email already exists")
        
        user = User(email, password, role)
        self.user_repository.save(user)
        return user

    def add_user_to_group(self, user: User, group_id: int):
        user.group_id = group_id
        self.user_repository.update(user)