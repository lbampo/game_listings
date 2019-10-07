from game_class import *

server = 'localhost,1433'

database = 'Game_Listings'

username = 'SA'

password = 'Passw0rd2018'

game_connect = Game(server, database, username, password)

# Print all games
# game_connect.print_all_games()


# Search one game
# input1 = input("\n Insert game name please: ").strip()
# print(game_connect.search_game_title(f"{input1}"))


# Add a game
#
# input_gname = input("Please input your game name: ")
# input_uname = input("Please input username: ")
# input_pnumber = input("Please input phone number: ")
# input_price = input("Please input game price: ")
# input_postcode = input("Please input postcode: ")
#
# game_connect.add_game(input_gname, input_uname, input_pnumber, input_price, input_postcode, game_connect.get_post_json_long(input_postcode), game_connect.get_post_json_lat(input_postcode))

# game_connect.print_all_games()
#

# Destroy Game
# game_gone = input("What is the GameID of the game you wish to delete?: ")
# game_connect.destroy_game(game_gone)

# game_connect.print_all_games()


# Write games to file
#
# write_to = str(game_connect.return_all_games())
#
# game_connect.write_to_file('games.txt', write_to )

# Update games

# input_update = input("What row you like to update")
# new_value = input("What would you like to update it with ")
#
# condition_value = input("What GameID would you like to update")
#
# game_connect.update_game_in_table(input_update, new_value, 'GameID', condition_value)

# game_connect.print_all_games()

# Get Longitude of PostCode

# print(game_connect.get_post_json_long('BR53DF'))

# Get Latitude of Postode
# print(game_connect.get_post_json_lat('BR53DF'))
#
#





