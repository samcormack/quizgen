import random
import operator

class Quiz:
    extra_params = []
    def __init__(self, input=None):
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
        self.params.extend(self.extra_params)
        if input is not None:
            self.bind(input)

    def bind(self, input):
        """ bind values for input parameters to quiz """
        self.values = {
            param['name']: int(input[param['name']])
            for param in self.params
        }

    def generate(self):
        return list()

    def pairs(self, filter_func):
        possibles = [
            (x, y)
            for x in range(1, self.values['max1']+1)
            for y in range(1,self.values['max2']+1)
            if filter_func(x,y)
        ]
        if len(possibles) < self.values['n_questions']:
            self.values['n_questions'] = len(possibles)
        return random.sample(possibles, self.values['n_questions'])

    @classmethod
    def get(cls, quizname):
        """ return class for quiz with name quizname """
        for sub in cls.__subclasses__():
            if sub.name == quizname:
                return sub
        else:
            raise ValueError('Quiz not found')

    @classmethod
    def types(cls):
        """ return names of all the quizzes"""
        return [sub.name for sub in cls.__subclasses__()]

class AdditionQuiz(Quiz):
    name = 'Addition'
    extra_params = [
        {
            'name': 'maxsum',
            'label': 'Maximum of sum:',
            'default': 10,
            'max': 30,
            'min': 2,
        }
    ]

    def generate(self):
        """ return list of strings with quiz questions """
        pairs = self.pairs(lambda x,y: x+y <= self.values['maxsum'])
        return ["{}) {} + {} = ".format(n+1, first, second) for (n,(first,second)) in enumerate(pairs)]


class SubtractionQuiz(Quiz):
    name = 'Subtraction'
    extra_params = []

    def generate(self):
        pairs = self.pairs(operator.gt)
        return ["{}) {} - {} = ".format(n+1, first, second) for (n,(first,second)) in enumerate(pairs)]

class BlanksMixin:
    @staticmethod
    def qstring(n, x, y, template):
        blankpos = random.randrange(3)
        if blankpos == 0:
            return template.format(n, '_', y, x-y)
        elif blankpos == 1:
            return template.format(n, x, '_', x-y)
        elif blankpos == 2:
            return template.format(n, x, y, '_')

class AdditionBlanksQuiz(Quiz, BlanksMixin):
    name = 'Addition with blanks'
    extra_params = [
        {
            'name': 'maxsum',
            'label': 'Maximum of sum:',
            'default': 10,
            'max': 30,
            'min': 2,
        }
    ]

    def generate(self):
        """ return list of strings with quiz questions """
        pairs = self.pairs(lambda x,y: x+y <= self.values['maxsum'])
        return [
            self.qstring(n+1, first, second, "{}) {} + {} = {}")
            for (n,(first,second)) in enumerate(pairs)
        ]

class SubtractionBlanksQuiz(Quiz, BlanksMixin):
    name = 'Subtraction with blanks'
    extra_params = []

    def generate(self):
        pairs = self.pairs(operator.gt)
        return [
            self.qstring(n+1, first, second, "{}) {} - {} = {}")
            for (n,(first,second)) in enumerate(pairs)
        ]
