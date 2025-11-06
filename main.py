import os
import re
import sys
import time
import manager as MNJR
from settings import GERNAL_SETTINGS, LOGO_SETTINGS, OWENER_INFO, INSTALLED_APPS, COLORS
c_print=("all required modules has been installed sucessfully")

class main:
    def __init__(self, LOGO_SETTINGS, APPS, COLORS):
        self.__apps = APPS
        self.__colors = COLORS
        self.__all_apps = dict()
        self.__logo_settings = LOGO_SETTINGS
        # self.__home_path = re.sub(r'/[^/]+$', repl="", string=os.getcwd() + "/")
        self.__home_path = os.getcwd() + "/"

    def start(self):
        # print(len(self.__apps))
        avilable_app_count = len(self.__apps)
        self.show_logo()
        if avilable_app_count == 0: 
            MNJR.c_print("NO APPS ARE AVILABLE PLEASE Add SOME APPS TO THE SETTINGS.PY")
            sys.exit()
        
        for i in range(avilable_app_count):
            # print(f"{i} element printed ")
            p_data = self.__apps[i]
            p_name,p_key = p_data[0], p_data[1]
            self.__all_apps[p_name] = p_key
            dname = self.extract_dir(link=p_name)
            print(f"{'0'+str(i+1) if i<=10 else i+1} {dname} {'' if self.is_installed(dname) else '( install )'}")
        ch = self.get_choice()
        self.handle_choice(ch) # now we have to check the scripts exists and run if really exists

    def extract_dir(self, ch="", link=""):
        """ this function takes the link and returns the app dir from the provided link """
        def extract_from_link(link):
            if link.endswith('.git'):
                path = link.split(".")[-2].split("/")[-1]
            else:
                path = link.split("/")[-1]
            return path
                
        if str(ch):
            try:
                link = list(self.__all_apps.keys())[int(ch)]
                path = extract_from_link(link)
                return path
            except Exception as e:
                MNJR.c_print(" ERROR ON extract_dir() : ===>>>> ", e)
        else:
            path = extract_from_link(link)
            return path
            
        
    def is_installed(self, p_name):
        """checks that the given name/folder is avilable on the same place or not returns the true or false"""
        if os.path.exists(self.__home_path + p_name):
            MNJR.c_print('Found That Directory')
            return True
        else:
            MNJR.c_print(f"Directory ''' {self.__home_path + p_name} ''' not found")
            return False
        
    def get_choice(self):
        try:
            choice = int(input(f"Enter Your Choice : {COLORS['reset']}"))
            if choice and choice <= len(self.__all_apps):
                return choice-1
            else:
                print(f"{COLORS['red']} Invalid choice  {COLORS['reset']}")
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
                    print(f"{COLORS['green']} perfect now app has been installed")
                    self.handle_choice(ch)
            else:
                MNJR.c_print('invalid choice')
        except Exception as e:
            print("error while processing your request : ", e)
    
    def show_logo(self):
        logo = "random"
        try:
            if not GERNAL_SETTINGS.get("logo_color") or not self.__logo_settings.get("logo_color") == "random":
                color = MNJR.get_random_color(self.__colors)
            else:
                color = self.__logo_settings.get("logo_color")    
            
            logo_text = self.__logo_settings.get('logo_text')
            logo_font = self.__logo_settings.get("logo_font") 
            logo = MNJR.generate_logo(logo_text, font=logo_font)

            if logo:
                print(f"{color} {logo} ")
            else:
                print("Unable to get the logo", logo)
                
        except Exception as e:
            MNJR.c_print("error while reading the logo file : ", e)
            sys.exit()
            

a = main(LOGO_SETTINGS, INSTALLED_APPS, COLORS)
a.start()
