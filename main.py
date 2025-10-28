import os
import time
import requests
from . import manager as MNJR
from .settings import IS_DEVELOPEMENT_MODE, LOGO_PATH, OWENER_INFO, INSTALLED_APPS
c_print=("all required modules has been installed sucessfully")

class main:
    @staticmethod
    def get_choice():
        try:
            choice = int(input("Enter Your Choice : "))
            if choice and choice <= len(INSTALLED_APPS):
                return choice
            else:
                print("Invalid choice")
                time.sleep(1)
                print("please try again")
                time.sleep(2)
                main.get_choice()
                
        except Exception as e:
            print(" invalid option choosen ")
            time.sleep(1)
            print("please try again")
            time.sleep(2)
            return main.get_choice()

    def handle_choice(ch):
        try:
            if ch == 1:
                pass  # tommarow ill start writting from this same position 
        except Exception as e:
            print("error while processing your request : ", e)
                
            
    @staticmethod
    def start():
        installation_status = None
        for i in range(len(INSTALLED_APPS)):
            p_data = INSTALLED_APPS[i]
            p_name,p_key = p_data[o], p_data[1]
            print(f"{i+1} {MNJR.p_name_by_link([o])}")
        ch = main.get_choice()
        main.handle_choice(ch) # now we have to check the scripts exists and run if really exists
        
    @staticmethod
    def show_logo(file_path):
        logo = None
        try:
            if os.path.exists(file_path):
                with open(f"{file_path}", "w") as f_obj:
                    logo = f_obj.read()
        except Exception as e:
            MNJR.c_print("error while reading the logo file ", e)
            sys.exit()
            

main.start()
