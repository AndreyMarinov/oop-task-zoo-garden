'''OOP Zoo Garden Task by Misho'''

class Animal:
    '''Defining the main class as Animal'''


    def __init__(self, name):
        self.name = name


class Dog(Animal):
    '''Defining class as Dog and inherits name from the class animal'''

    _spieces = 'Dog'
    _sound = 'Bark'

    def __init__(self, name):
        super().__init__(name)


    def spieces(self):
        '''Returning the spiece of the dog'''
        return self._spieces

    def sound(self):
        '''Returning the sound of the dog'''
        return self._sound

    def run(self):
        '''Returning True cuz the dog can run'''
        return True

    def swim(self):
        '''Returning True cuz the dog can swim'''
        return True

    def is_mammal(self):
        '''Returning True cuz the Dog is mammal'''
        return True

class Cat(Animal):
    '''Defining class as Cat and inherits name from the class animal'''

    _spieces = 'Cat'
    _sound = 'Meow'

    def __init__(self, name):
        super().__init__(name)

    def spieces(self):
        '''Returning the spiece of the cat'''
        return self._spieces

    def sound(self):
        '''Returning the sound of the cat'''
        return self._sound

    def is_mammal(self):
        '''Returning True cuz the cat is mammal'''
        return True

    def run(self):
        '''Returning True cuz the cat can run'''
        return True

    def swim(self):
        '''Returning True cuz the cat can swim'''
        return True

class Snake(Animal):
    '''Defining class as Snake and inherits name from the animal class'''

    _spieces = 'Snake'
    _sound = 'sssssssss'

    def __init__(self, name):
        super().__init__(name)


    def spieces(self):
        '''Returning the spiece of the snake'''
        return self._spieces

    def sound(self):
        '''Returning the sound of the snake'''
        return self._sound

    def is_mammal(self):
        '''Returning False cuz the Snake is not mammal'''
        return False

    def swim(self):
        '''Returning True cuz the snake can swim'''
        return True


class Fish(Animal):
    '''Defining class as Fish and inherits name from the animal class'''

    _spieces = 'Fish'
    _sound = 'brbrbrbrbr'

    def __init__(self, name):
        super().__init__(name)


    def is_mammal(self):
        '''Returning False cuz the fish is not mammal'''
        return False

    def spieces(self):
        '''Returning the spiece of the fish'''
        return self._spieces

    def sound(self):
        '''Returning the sound of the fish'''
        return self._sound

    def running(self):
        '''Returning False cuz the fish cant run'''
        return False

    def swim(self):
        '''Returning True cuz the fish can swim'''
        return True


dog = Dog('Jorge')
print(dog.run())
print(dog.swim())
print(dog.spieces())
print(dog.sound())
print(dog.is_mammal())
