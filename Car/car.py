class Car :
    sterringWheel=1
    def __init__(self,name,wheels):
        self.name=name
        self.wheels=wheels
    
    def drive(self):
        print(f'{self.name} is driving.')

    @classmethod
    def common(cls):
        print(f'all car has only {cls.sterringWheel} sterring wheel')

