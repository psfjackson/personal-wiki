name = ''
question = ''
answer = ''

import random
rad_num = random.randint(1, 9)
# print (rad_num)


# connecting number to answers
if rad_num == 1:
  answer += 'Yes - definitely'
elif rad_num == 2:
  answer += 'It is decidedly so'
elif rad_num == 3:
  answer += 'Without a doubt'
elif rad_num == 4:
  answer += 'Reply hazy, try again'
elif rad_num == 5:
  answer += 'Ask again later'
elif rad_num == 6:
  answer += 'Better not tell you now'
elif rad_num == 7:
  answer += 'My sources say no'
elif rad_num == 8:
  answer += 'Outlook not so good'
elif rad_num == 9:
  answer += 'Very doubtful'
else:
  answer += 'Error'

# name and question inputs
name += 'Joe'
question += 'Will Wales beat Ireland in the rugby?'

# printed statements
if question == '':
  print ('You must enter a question.') 
elif name == '':
  print ('Question: ' + question)
  print ('Magic 8-Balls answer: ' + answer) 
else:
   print (name + ' asks: ' + question)
   print ('Magic 8-Balls answer: ' + answer) 
   


  