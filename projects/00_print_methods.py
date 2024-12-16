import time

print('Hello', end=' ')
print('World!')                         # Output: Hello World!

print('first sentence', end=', ')
print('second sentence.')               # Output: first sentence., second sentence.

print('Loading', end='')
print('...')                            # Output: Loading...

print('Good Morning', end=' - ')
print('Have a great day!')              # Output: Good Morning - Have a great day!

print('Line 1', end='\n---\n')
print('Line 2')                         # Output: Line 1
                                        #         ---
                                        #         Line 2

for i in range(5):
    print(i, end=' | ')                 # Output: 0 | 1 | 2 | 3 | 4 |
    
print('\n')

for i in range(6):
    print(f'Progress: {i*20}%', end='\r')  # Overwrites the line
    time.sleep(1)

print('\n')
