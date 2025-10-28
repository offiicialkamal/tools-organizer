import requests

from . import manager as MNJR

from .settings import IS_DEVELOPEMENT_MODE, LOGO_PATH, OWENER_INFO, INSTALLED_APPS

if IS_DEVELOPEMENT_MODE:
    print("all required modules has been installed sucessfully")
 

class main:
    @staticmethod
    def start():
        for i in range(len(INSTALLED_APPS)):
            p_data = INSTALLED_APPS[i]
            p_name,p_key = p_data[o], p_data[1]
            
            print(f"{i+1} {p_name_by_link([o])}")
