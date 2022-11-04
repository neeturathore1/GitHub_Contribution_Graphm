import os
from random import randint
def make_commit(days: int):
    if days <1:
        #Push
        return os.system('git push')
    else:
        dates = f'{days} days agp'

        with open('data.txt','a') as file:
            file.write(f'{dates}\n')
        
        #staging
        os.system('git add data.txt')

        #commit
        os.system('git commit --date="'+dates+'" -m "First Commit"')

        return days * make_commit(days-1)

make_commit(randint(1,365))