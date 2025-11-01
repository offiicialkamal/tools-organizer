import os
import re
import sys
import time
import requests
import manager as MNJR
from settings import IS_DEVELOPEMENT_MODE, LOGO_PATH, OWENER_INFO, INSTALLED_APPS, COLORS
c_print=("all required modules has been installed sucessfully")

class main:
    def __init__(self, logo_path, apps):
        self.__apps = apps
        self.__all_apps = dict()
        self.__LOGO_PATH = logo_path
        self.__home_path = re.sub(r'/[^/]+$', repl="", string=os.getcwd())

    def start(self):
        # print(len(self.__apps))
        avilable_app_count = len(self.__apps)
        if avilable_app_count == 0: 
            MNJR.c_print("NO APPS ARE AVILABLE PLEASE Add SOME APPS TO THE SETTINGS.PY")
            sys.exit()
        
        for i in range(avilable_app_count):
            # print(f"{i} element printed ")
            p_data = self.__apps[i]
            p_name,p_key = p_data[0], p_data[1]
            self.__all_apps[p_name] = p_key
            print(f"{'0'+str(i+1) if i<=10 else i+1} {self.extract_dir(link=p_name)} ")
        ch = self.get_choice()
        self.handle_choice(ch) # now we have to check the scripts exists and run if really exists

    def extract_dir(self, ch=None, link=None):
        """ this function takes the link and returns the app dir from the provided link """
        def extract_from_link(link):
            if not link.endswith('.git'):
                path = link.split(".")[-2].split("/")[-1]
            else:
                path = link.split("/")[-1]
            return path
                
        if not link:
            link = list(self.__all_apps.keys())[ch - 1]
            path = extract_from_link(link)
            return path
        else:
            path = extract_from_link(link)
            return path
            
        
    def is_installed(self, p_name):
        """checks that the given name/folder is avilable on the same place or not returns the true or false"""
        if os.path.exists(self.__home_path + p_name):
            MNJR.c_print('Found That Directory')
            return True
        else:
            MNJR.c_print("Directory not found")
            return False
        
    def get_choice(self):
        try:
            choice = int(input(f"Enter Your Choice : {COLORS['reset']}"))
            if choice and choice <= len(self.__all_apps):
                return choice-1
            else:
                print(f"{COLORS['red']}Invalid choice  {COLORS['reset']}")
                # time.sleep(3)
                for i in range(-1, -8, -1):
                    print(f"{COLORS['yellow']} please try again in {i}: {COLORS['reset']}", end=" ")
                    time.sleep(1)
                    print("\033[A","\033[K")
                print("\n")
                self.get_choice()
                
        except Exception as e:
            MNJR.c_print(e)
            print(f"{COLORS['red']} invalid option choosen  {COLORS['reset']} ")
            time.sleep(1)
            print(f"{COLORS['yellow']}please try again  {COLORS['reset']}")
            time.sleep(2)
            return self.get_choice()

    def handle_choice(self, ch):
        """based on the output it runs/installs the specified path"""
        try:
            if ch <= len(self.__all_apps):
                app_directory = self.extract_dir(ch)
                if self.is_installed(app_directory):
                    # os.chdir(self.__home_path + app_directory)
                    # os.system(f'python main.py {self.__apps.get(app_directory)}')
                    # from .app_directory import main
                    __import__(f"{app_directory}.main", fromlist=['main'])
                else:
                    os.system(f'git clone {list(self.__all_apps.keys())[ch]}')
                    print(f"{COLORS['green']}perfect now app has been installed")
                    self.handle_choice(ch)
            else:
                MNJR.c_print('invalid choice')
        except Exception as e:
            print("error while processing your request : ", e)
    
    def show_logo(self):
        logo = None
        try:
            if os.path.exists(self.__LOGO_PATH):
                with open(self.__LOGO_PATH, "w") as f_obj:
                    logo = f_obj.read()
                    print(logo)
        except Exception as e:
            MNJR.c_print("error while reading the logo file ", e)
            sys.exit()
            

a = main(LOGO_PATH, INSTALLED_APPS)
a.start()
