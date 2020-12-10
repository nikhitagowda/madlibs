  
from sample_madlibs import harrypotter, code, zombie, hungergames, zoo
import random

if __name__ == "__main__":
    m = random.choice([harrypotter, code, zombie, hungergames, zoo])
    m.madlib()
