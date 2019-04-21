import random

def generator(max1, max2, maxsum, n_questions):
    """ return list of strings with quiz questions """
    possibles = [(x, y) for x in range(1,max1+1) for y in range(2,max2+1) if x+y<=maxsum]
    if len(possibles) < n_questions:
        n_questions = len(possibles)
    pairs = random.sample(possibles, n_questions)
    return ["{}) {} + {} = ".format(n+1, first, second) for (n,(first,second)) in enumerate(pairs)]
    
