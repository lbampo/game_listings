from game_class import *

server = 'localhost,1433'

database = 'Game_Listings'

username = 'SA'

password = 'Passw0rd2018'

game_connect = Game(server, database, username, password)

# Print all games
game_connect.print_all_recipes()


# Read one recipe
# input2 = input("\n Insert game name please: ").strip()
# print(game_connect.search_game_title(f"{input2}"))

