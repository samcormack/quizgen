import random

# def generator(max1, max2, maxsum, n_questions):
#     """ return list of strings with quiz questions """
#     possibles = [(x, y) for x in range(1,max1+1) for y in range(2,max2+1) if x+y<=maxsum]
#     if len(possibles) < n_questions:
#         n_questions = len(possibles)
#     pairs = random.sample(possibles, n_questions)
#     return ["{}) {} + {} = ".format(n+1, first, second) for (n,(first,second)) in enumerate(pairs)]


class Quiz:
    def __init__(self):
        self.params = [
            {
                'name': 'n_questions',
                'label': 'Number of questions:',
                'default': 20,
                'max': 100,
                'min': 1,
            },
            {
                'name': 'max1',
                'label': 'Maximum for first number:',
                'default': 10,
                'max': 30,
                'min': 1,
            },
            {
                'name': 'max2',
                'label': 'Maximum for second number:',
                'default': 10,
                'max': 30,
                'min': 1,
            },
        ]

    def bind(self, input):
        self.values = {
            param['name']: int(input[param['name']])
            for param in self.params
        }

    def generate(self):
        return list()

    @classmethod
    def get(cls, quizname):
        qs = {sub.name: sub for sub in cls.__subclasses__()}
        return qs[quizname]

    @classmethod
    def types(cls):
        return [sub.name for sub in cls.__subclasses__()]

class AdditionQuiz(Quiz):
    name = 'add'
    extra_params = [
        {
            'name': 'maxsum',
            'label': 'Maximum of sum:',
            'default': 10,
            'max': 30,
            'min': 2,
        }
    ]
    def __init__(self, input=None):
        super().__init__()
        self.params.extend(self.extra_params)
        if input is not None:
            super().bind(input)

    def generate(self):
        """ return list of strings with quiz questions """
        possibles = [
            (x, y)
            for x in range(1,self.values['max1']+1)
            for y in range(1,self.values['max2']+1)
            if x+y <= self.values['maxsum']
        ]
        if len(possibles) < self.values['n_questions']:
            self.values['n_questions'] = len(possibles)
        pairs = random.sample(possibles, self.values['n_questions'])
        return ["{}) {} + {} = ".format(n+1, first, second) for (n,(first,second)) in enumerate(pairs)]


class SubtractionQuiz(Quiz):
    name = 'subtract'
    extra_params = []

    def __init__(self, input=None):
        super().__init__()
        self.params.extend(self.extra_params)
        if input is not None:
            super().bind(input)

    def generate(self):
        possibles = [
            (x, y)
            for x in range(1,self.values['max1']+1)
            for y in range(1,self.values['max2']+1)
            if x - y > 0
        ]
        if len(possibles) < self.values['n_questions']:
            self.values['n_questions'] = len(possibles)
        pairs = random.sample(possibles, self.values['n_questions'])
        return ["{}) {} - {} = ".format(n+1, first, second) for (n,(first,second)) in enumerate(pairs)]
