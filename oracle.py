print('I am the Oracle of Python Wisdom. Ask your question...')
question = input('What topic do you want to know about? (functions, loops, variables, arrays...)? ')

match question:
  case 'function' | 'functions':
    print('Functions are reusable blocks of code that perform specific tasks.')
  case 'loops':
    print('Loops are control structures that allow you to execute a block of code repeatedly. They are essential for automating repetitive tasks and processing collections of data efficiently. Use for or while.')
  case 'variables':
    print('Variables are containers that store data values. pergunta = "Qual sua idade?" ')
  case 'arrays':
    print('Lists store multiple values. From: fruits = ["apple","banana"]')
  case _:
    print('This question is beyond my current knowledge.')