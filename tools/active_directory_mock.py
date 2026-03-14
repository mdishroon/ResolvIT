class ActiveDirectoryMock:
    def __init__(self):
        # simple dictionary simulating Active Directory database state
        self.users = {
            "treasury_user": {
                "status": "locked",
                "department": "Treasury",
                "failed_attempts": 3
            },
            "clerk_user": {
                "status": "active",
                "department": "Clerk",
                "failed_attempts": 0
            }
        }

    def check_user_status(self, username):
        if username in self.users:
            status = self.users[username]['status']
            return f"User {username} status is currently: {status}."
        return f"Error: User {username} not found in Active Directory."

    def unlock_user(self, username):
        if username in self.users:
            self.users[username]['status'] = "active"
            self.users[username]['failed_attempts'] = 0
            return f"Success: User {username} has been unlocked."
        return f"Error: User {username} not found in Active Directory."

    def add_failed_attempt(self, username):
        if username in self.users:
            self.users[username]['failed_attempts'] += 1
            if self.users[username]['failed_attempts'] >= 3:
                self.users[username]['status'] = "locked"
            return f"Attempt logged. Total failures: {self.users[username]['failed_attempts']}."
        return f"Error: User {username} not found in Active Directory."