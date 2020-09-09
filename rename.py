import os,sys,imghdr,time

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


folder_name = input("enter folder name ===> ")
list = sorted(os.listdir(folder_name))

os.chdir(folder_name)


def rename_files():
    num = 1
    for file in list:
        old_name = file
        if num < 10 :
            new_name = f"Episode_00{num}.mp4"
        elif num < 100:
            new_name = f"Episode_0{num}.mp4"
        else:
            new_name = f"Episode_{num}.mp4"
        try:
            os.rename(old_name, new_name)
            print(f"{bcolors.OKGREEN}done renaming ==> {old_name} ==> into ==> {new_name}{bcolors.ENDC}")
        except Exception as e:
            print(bcolors.FAIL + imghdr.what(file) + {bcolors.ENDC})


        num += 1


def show_files():
    num = 1
    for i in list:
    #    print(i)
        old_name = i
        if num < 10 :
            new_name = f"Episode_00{num}.mp4"
        elif num < 100:
            new_name = f"Episode_0{num}.mp4"
        else:
            new_name = f"Episode_{num}.mp4"
        print(f"{bcolors.WARNING}will rename ==> {old_name} ==> into ==> {new_name}{bcolors.ENDC}")

        num += 1

    print(f"""{bcolors.OKBLUE}
        _____________________________________________
        _                                           _
        _   The files will be renamed as above ...  _
        _                                           _
        _   Do you want to continue?                _
        _   {bcolors.OKGREEN}1) continue   {bcolors.OKBLUE}                          _
        _   {bcolors.FAIL}2) quit  {bcolors.OKBLUE}                               _
        _____________________________________________
          {bcolors.ENDC}""")
    choise = input("        >>> ")

    if choise == '1':
        rename_files()
    elif choise == '2':
        os.system('clear')
        print(f"""
        {bcolors.FAIL}
        ________________________________
        _                              _
        _          Quiting .../        _
        ________________________________
        {bcolors.ENDC}""")
        time.sleep(2)
        sys.exit()

    else:
        os.system('clear')
        print(f"""
        {bcolors.WARNING}
        ________________________________
        _                              _
        _ please choose a valid option _
        ________________________________
        {bcolors.ENDC}""")
        time.sleep(2)
        show_files()


show_files()
