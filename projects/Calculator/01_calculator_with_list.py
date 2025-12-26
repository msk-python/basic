import os
os.system('cls')

class History:

    def __init__(self):
        self.data = []

    def show(self):
        print(self.data)

    def clear(self):
        self.data.clear()

    def update(self, result):
        self.data.append(result)

h = History()

while True:
    value = input('Enter a Value: ')
    if 'q' in value or "Q" in value:
        print('Thanks for using!.')
        break

    elif "sh" in value or "SH" in value:
        h.show()

    else:
        result = eval( value )
        h.update(f"{value} = {result}")
        print(h.data[-1])
        
