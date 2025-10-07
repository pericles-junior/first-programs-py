questions = [
    ['How much is 2 + 2?','4'],
    ['How many fingers does a hand have?','5'],
    ['How many legs does a horse have?','4'],
    ['Who is the greatest football player in history?','Cristiano Ronaldo']
  ]

hits = 0

for question in questions:
  answer = input(f'{question[0]}  ')
  if answer.lower() == question[1].lower():
    hits += 1
  
print (f'You hit {hits} of {len(questions)} questions!')