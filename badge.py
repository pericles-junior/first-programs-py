import os
os.system('cls')

msgWel = 'Welcome to the Dev Badge'
print('-' * len(msgWel))
print(msgWel)
print('-' * len(msgWel))
name = input('Type your name: ')
age = input('Type your age: ')
language = input('Type your favorite programming language: ')
emoji = input('Type an emoji that represents you: ')

os.system('cls') 
print('-' * 15)
os.system('echo.')
print('👨‍💻 Dev Bage ')
print(f'Name: {name}')
print(f'Age: {age}')
print(f'Favorite language: {language}')
print(f'Emoji: {emoji}')
os.system('echo.')
print('-' * 15)