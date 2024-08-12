class InMemoryUserRepository:
    def __init__(self):
        self.users = []

    def exists(self, email: str) -> bool:
        return any(user.email == email for user in self.users)

    def save(self, user: User):
        self.users.append(user)

    def update(self, user: User):
        for u in self.users:
            if u.email == user.email:
                u.group_id = user.group_id