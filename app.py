import os
from random import randint

for i in range(1,365):

    for j in range(0,randint(1,10),randint(5,10)):
        d = str(i) + 'days ago'
        with open('data.txt','a') as file:
            file.write(f'{dates}\n')
        os.system('git add data.txt')
        os.system('git commit --date="'+dates+'" -m "First Commit"')
os.system('git push -u origin main')