

from game_class import  *

from db_class import  *

input_1 = input("Welcome to BreezyGames can I help you?: ").strip()

while input_1 != 'no':
    input_2 = input("Ok, what can I do for you?: ").strip().lower()

    if  ("please" not in input_2) and ("thanks" not in input_2)  :
        print("Woah there, looks like you're missing a very special word ")

    elif "all games" in input_2:
        print(game_connect.print_all_games())

    elif "search" in input_2:
        input1 = input("\n Insert game name please: ").strip()
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
        game_gone = input("What is the GameID of the game you want to destroy?: ")
        game_connect.destroy_game(game_gone)

    elif "write to" in input_2:
        write_to = str(game_connect.return_all_games())

        game_connect.write_to_file('games.txt', write_to )




        receptionist_input2 = input("Can i do anything else for you today?")
        if ('thanks' not in receptionist_input2) or ('please' not in receptionist_input2):
            print("wow, again? Please go and learn some manners")

        else:
            print("Ok, well have an amazing day")
            break

    elif 'nothing' in input_2:
        break

    else:
        break

else:
    print("Ok, have an amazing day")
