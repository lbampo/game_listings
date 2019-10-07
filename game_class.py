# import packages

import pyodbc

import json

import requests





# Define class Game
class Game():

    # Assign given attributes
    def __init__(self, server, database, username, password):
        self.server = server

        self.database = database

        self.username = username

        self.password = password

        self.connect_db = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + self.server + ';DATABASE=' + self.database + ';UID=' + self.username + ';PWD=' + self.password)

        self.cursor = self.connect_db.cursor()


# Defining methods

    def filter_query(self, query):
        return self.cursor.execute(query)



    # Method to search game

    def search_game_title(self, GameName):
        find_game = self.filter_query(f"SELECT * FROM games WHERE GameName = '{GameName}'")

        return find_game.fetchone()

# Method to be all so search all from table "games"

    def query_all_games(self):
        return self.filter_query("SELECT * FROM games")


    def print_all_games(self):
        all_games = self.query_all_games()

        while True:

            record = all_games.fetchone()

            if record is None:
                break

            print(record)

    def return_all_games(self):
        all_games = self.query_all_games()

        while True:

            record = all_games.fetchall()

            if record is None:
                break

            return record




# Method to add a game

    def add_game(self, GameName, UserName, PhoneNumber, Price, PostCode, Longitude, Latitude ):
        self.filter_query(f"INSERT INTO games VALUES ('{GameName}', '{UserName}', '{PhoneNumber}', '{Price}', '{PostCode}', '{Longitude}', '{Latitude}')")

        # this .commit() applied to the
        # connection attribute of the database will make sure the changes commit and alters the persistent data

        self.connect_db.commit()

        print('Insertion Complete')

# Method to destroy a game
    def destroy_game(self, game_delete):

        self.filter_query(f"DELETE FROM games WHERE GameID = '{game_delete}'")


        self.connect_db.commit()

        print('Removal complete')

# Method to write DB contents to file
    def write_to_file(self, file, game_item):

        try:
            with open(file, 'w') as opened_file:
                opened_file.write(game_item)

        except FileNotFoundError:
            print("File not found")

# Method to update a game in table
    def update_game_in_table(self, value_to_update, new_value, condition_column, condition_value):

        self.filter_query(f"UPDATE games SET {value_to_update} = '{new_value}' WHERE {condition_column} = '{condition_value}'")

        self.connect_db.commit()

        print('Update Complete')

# Method to get Longitude
    def get_post_json_long(self, p_code):
        req_post = requests.get(f'https://postcodes.io/postcodes/{p_code}')
        req_json = req_post.json()

        json_str = json.dumps(req_json)
        resp = json.loads(json_str)

        return resp["result"]["longitude"]

# Method to get Latitude
    def get_post_json_lat(self, p_code):
        req_post = requests.get(f'https://postcodes.io/postcodes/{p_code}')
        req_json = req_post.json()

        json_str = json.dumps(req_json)
        resp = json.loads(json_str)


        return resp["result"]["latitude"]















