# import the function that will return an instance of a connection
from mysqlconnection import MySQLConnection, connectToMySQL

# model the class after the friend table from our database


class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('users').query_db(query)
        # Create an empty list to append our instances of friends
        users = []
        # Iterate over the db results and create instances of friends with cls.
        for dictionary in results:
            users.append(cls(dictionary))
        return users

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users where id = %(id)s;"
        results = connectToMySQL('users').query_db(query, data)
        return cls(results[0])

    @classmethod
    def add_one(cls, data):
        query = "INSERT INTO users (first_name, last_name, email) VALUES(%(first_name)s,%(last_name)s,%(email)s);"
        results = connectToMySQL('users').query_db(query, data)
        print(results)
        return results

    @classmethod
    def update(cls, data):
        query = "UPDATE users SET first_name= %(first_name)s, last_name = %(last_name)s, email = %(email)s WHERE id = %(id)s;"
        return connectToMySQL('users').query_db(query, data)

    @classmethod
    def delete(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s"

        return connectToMySQL('users').query_db(query, data)
