import requests

r = requests.get('https://lichess.org/api/user/MarcinK50')

rapid_games = r.json()['perfs']['rapid']['games']
rapid_rank = r.json()['perfs']['rapid']['rating']

a_file = open("README.md", "r")
list_of_lines = a_file.readlines()
for i, line in enumerate(list_of_lines):
    if line.__contains__('rated'):
        list_of_lines[i] = f"I'm rated test after {rapid_games} rapid games.\n"


a_file = open("README.md", "w")
a_file.writelines(list_of_lines)
a_file.close()
