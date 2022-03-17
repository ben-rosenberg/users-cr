from mysqlconnection import connectToMySQL

class User:
    def __init__(self, data) -> None:
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.updated_at = data['updated_at']
        self.created_at = data['created_at']
    
    @classmethod
    def get_all(cls) -> list:
        query = 'SELECT * FROM users;'
        db = connectToMySQL('users_db')
        query_results = db.query_db(query)
        all_users = []
        for user in query_results:
            all_users.append(cls(user))
        return all_users

    @classmethod
    def create(cls, data: dict) -> int:
        query = 'INSERT INTO users (first_name, last_name, email)\
            VALUES(%(first_name)s, %(last_name)s, %(email)s);'
        return connectToMySQL('users_db').query_db(query, data)
        