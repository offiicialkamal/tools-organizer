import re
import sys
from settings import GERNAL_SETTINGS

def p_name_by_link(link):
    try:
        if link.endswith("com", "git"):
            link = link.split(".")[-2].split("/")[-1]
        else:
            link = link.split("/")[-2]
        return link
    except Exceptions as e:
        if GERNAL_SETTINGS.get('IS_DEVELOPEMENT_MODE'):
            print("error on p_name_by_link ", e)
        sys.exi()  
        
        