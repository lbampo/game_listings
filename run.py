import time

from game_class import  *

from db_class import  *

input_1 = input("Welcome to BreezyGames can I help you?: ").strip()

while input_1 != 'no':
    input_2 = input("Ok, what can I do for you?: ").strip().lower()

    if  ("please" not in input_2) and ("thanks" not in input_2)  :
        print("\nWoah there, looks like you're missing a very special word\n ")

    elif "all games" in input_2:
        print("\n Of course, here you go \n")
        print(game_connect.print_all_games())

    elif "search" in input_2:
        input1 = input("\n Course I can, what is the name of the game?: ").strip()
        print(game_connect.search_game_title(f"{input1}"))

    elif "add" in input_2:
        print("Sure you can \n")
        input_gname = input("Please input your game name: ")
        input_uname = input("Please input username: ")
        input_pnumber = input("Please input phone number: ")
        input_price = input("Please input game price: ")
        input_postcode = input("Please input postcode: ")

        game_connect.add_game(input_gname, input_uname, input_pnumber, input_price, input_postcode,
                              game_connect.get_post_json_long(input_postcode),
                              game_connect.get_post_json_lat(input_postcode))

    elif "destroy" in input_2:
        print("Ummm, hold on let me ask my manager if we allow that.. hold on a second")

        time.sleep(5)

        print("\nOh, we do... sorry for the wait")

        game_gone = input("\n What is the GameID of the game you want to destroy?: ")
        game_connect.destroy_game(game_gone)

    elif "write all games" in input_2:
        write_to = str(game_connect.return_all_games())

        game_connect.write_to_file('games.txt', write_to )


    elif "update" in input_2:
        print("\n Sure you can \n")
        input_update = input("What row you like to update: ")
        new_value = input("What would you like to update it with: ")

        condition_value = input("What GameID would you like to update: ")

        game_connect.update_game_in_table(input_update, new_value, 'GameID', condition_value)





    elif 'nothing' in input_2:
        print(" \n \n Ok, hope I've helped you today. Have an amazing day")
        break

    else:
        break

else:
    print("Ok, have an amazing day")
