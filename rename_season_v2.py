# renameing episodes like > SxxExxx.xxx
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

def main():
    print(os.getcwd())
    print(os.getcwd())
    global start_number,list,season_number
    folder_name = input("Enter folder name ===> ")
    print('_____________________________________________________\n')
    season_number = int(input("Enter the season number ==> "))
    print('_____________________________________________________\n')
    start_number = int(input("Enter the number from which the counter will start ==> "))
    print('_______________________________________________________________________\n')
    list = sorted(os.listdir(folder_name))

    os.chdir(folder_name)
    show_files()


def rename_files():
    num = start_number
    season = str(season_number).zfill(2)
    for file in list:
        old_name = file
        extention = file.split('.')
        extention = str(extention[-1])
        num = str(num).zfill(3)
        new_name = f"S{season}E{num}.{extention}"
        try:
            os.rename(old_name, new_name)
            print(f"{bcolors.OKGREEN}done renaming ==> {old_name} ==> into ==> {new_name}{bcolors.ENDC}")
        except Exception as e:
            print(bcolors.FAIL + imghdr.what(file) + {bcolors.ENDC})

        num = int(num)
        num += 1

    print(f"""{bcolors.OKBLUE}
        _____________________________________________
        _                                           _
        _                                           _
        _   Do you want to rename a new season?     _
        _   {bcolors.OKGREEN}1) rename     {bcolors.OKBLUE}                          _
        _   {bcolors.FAIL}2)any athor button to quit  {bcolors.OKBLUE}             _
        _____________________________________________
          {bcolors.ENDC}""")
    choise = input("        >>> ")


    if choise == '1':
        os.system('clear')
        os.chdir('../')
        main()
    else:
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




def show_files():
    num = start_number
    season = str(season_number).zfill(2)

    for i in list:

        extention = i.split('.')
        extention = str(extention[-1])

        old_name = i
        num = str(num).zfill(3)
        new_name = f"S{season}E{num}.{extention}"
        print(f"{bcolors.WARNING}will rename ==> {old_name} ==> into ==> {new_name}{bcolors.ENDC}")
        num = int(num)
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


if __name__ == '__main__':
    main()
