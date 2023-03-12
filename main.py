import openai
import os
import time
import sys


openai.api_key_path = ".env"

prompt = input("Choose words at random and I'll do my best to tell you a tale: ")
print('Wait, your story is being created... \n')
response = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    messages =[{'role': 'system', 'content': 'You tell stories for children. The stories you tell must have a message.'},
               {'role': 'system', 'content': 'Remember: this stories are for children so they must have fantasy, adventure and they must teach about aspects of life'},
               {'role': 'user', 'content': prompt}])

for c in response.choices[0].message.content:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.05)

cost = f'That wonderfull tale just costed you: '+str(int(response.usage.total_tokens)*0.002/1000)+' US dollars'
for c in cost:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.05)


print(response.choices[0].message.content)
print(f'\nThat wonderfull tale just costed you: '+str(round(int(response.usage.total_tokens)*0.002/1000,5))+' US dollars')