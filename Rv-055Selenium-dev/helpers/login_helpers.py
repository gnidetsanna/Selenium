"""helper module for profile_test.py"""
import json
import random
from string import ascii_lowercase
import datetime

def get_random_pass(pass_len=None):
    """function to generate random pass from alphabet"""

    def save_new_pass(new_pass):
        """save new password to file"""
        timestamp = datetime.datetime.now()
        try:
            file_obj = open('.password.json')
            data = json.load(file_obj)
            file_obj.close()
        except FileNotFoundError:
            data = dict()
        with open('.password.json', 'w', encoding='utf-8') as file_obj:
            data[timestamp.isoformat()] = new_pass
            json.dump(data, file_obj, ensure_ascii=False, indent=2)

    if pass_len is None:
        pass_len = 7
    char_list = random.sample(ascii_lowercase, pass_len)
    new_pass = ''.join(char_list)
    save_new_pass(new_pass)
    return new_pass

def read_new_pass():
    """read new pass from file"""
    with open('.password.json') as json_file:
        data = json.load(json_file)
    return data['password']
