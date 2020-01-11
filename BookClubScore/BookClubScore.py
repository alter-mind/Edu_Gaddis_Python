books = int(input('Enter nuber of books: '))
if books in range(2,4):
    score = 5
elif books in range(0,2):
    score = 0
elif books in range(4,6):
    score = 15
elif books in range(6,8):
    score = 30
elif books >= 8:
    score = 60
else:
    score = -1
    print('You can not bye negative number of books')
if score >= 0:
    print('You score:', score)