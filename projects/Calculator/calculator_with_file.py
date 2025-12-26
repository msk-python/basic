import os
os.system('cls')

class History:

    def __init__(self, filename="history.txt"):
        self.filename = filename

        # Create file if not exists
        if not os.path.exists(self.filename):
            open(self.filename, 'w').close()

    def show(self):
        with open(self.filename, 'r') as file:
            data = file.read()
            if data:
                print(data)
            else:
                print("No history found.")

    def clear(self):
        open(self.filename, 'w').close()
        print("History cleared.")

    def update(self, result):
        with open(self.filename, 'a') as file:
            file.write(result + '\n')

h = History()

while True:
    value = input('Enter a Value: ')

    if value.lower() == 'q':
        print('Thanks for using!.')
        break

    elif value.lower() == 'sh':
        h.show()
    
    elif value.lower() == 'ch':
        h.clear()

    else:
        try:
            result = eval(value)
            record = f"{value} = {result}"
            h.update(record)
            print(record)
        except Exception:
            print("Invalid Expression")
