import sys


version = "1.0"
print("_" * 40)
print(f"Command Line TODO: VERSION: {version}")
print("type 'help' for help")
print("_" * 40)
loop = True


def data_list():
    with open("list", "r") as f:
        lines = f.readlines()
        print("|ID|____|TODO|____|CHECKD|")
        for line in enumerate(lines):
            inf = line[1].split(",")
            print(f"{line[0]}|{inf[0]}|{inf[1]}")
            

def check_user_input(user_input):
    # no input 
    if user_input == "":
        print("input, please")
    
    # show help page 
    elif user_input == "help":
        print("_" * 40)
        print("Help Page:")
        print("--Command--|--Usage--")
        print("   quit    |close programm")
        print("   reset   |reset todo list")
        print("   list    |show todo list")
        print(" add,this  |add 'this' to todo list")
        print("!! id is provided by list: do list first. !!")
        print(" chk,id    |check 'id' on todo list")
        print(" del,id    |delete 'id from todo list")

    elif user_input == "quit":
        print("exiting")
        sys.exit()
    
    # clear list 
    elif user_input == "clear":
        y_n = input("reset?")   
        if y_n == "y" or y_n == "yes":
            with open("list", "w") as f:
                f.write("")
                print("list cleared")
        
        elif y_n == "n" or y_n == "no":
            print("aborted")
        
        else:
            print("aborted")


    elif user_input == "list":
        # show all entrys 
        data_list()

    else:
        arguments = user_input.split(',')
        # catch single arg
        if len(arguments) == 1:
            print("you need to provide an argument : 1")
     
        # catch double arg
        elif len(arguments) == 2:
             # caller // add del chn chk
            if arguments[0] == "add":
            # example add,text -> add entry
                text = arguments[1]
                with open("list", "r") as f:
                    lines = f.readlines()
                    lines.append(f"{text},[]\n")
                    with open("list", "w") as f:
                        f.writelines(lines)
                        print("added")
        
            if arguments[0] == "del":
            # example del,do homework -> delete entry
                delete = arguments[1]
                with open("list", "r") as f:
                    lines = f.readlines()
                    lines.pop(int(delete))
                    with open("list", "w") as f:
                        f.writelines(lines)
                        print("ID: {delete} deleted.")

            
            if arguments[0] == "chk":
                # example chk,do homework -> checked / done
                entry = arguments[1]
                with open("list", "r") as f:
                    lines = f.readlines()
                    wl = lines[int(entry)].split(",")
                    new = f"{wl[0]},[x]\n"
                    lines.pop(int(entry))
                    lines.append(new)
                    with open("list", "w") as f:
                        f.writelines(lines)
                        print("checked")

        
while loop:
    user_input = input(">:")
    check_user_input(user_input)