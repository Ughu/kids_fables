import openai
import os
import time
import sys


openai.api_key_path = ".env"

prompt = input("Choose words at random and I'll do my best to tell you a tale: ")

print('Wait, your story is being created... \n')

story = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    messages=[{'role': 'system', 'content': 'You tell stories for children.\
                The stories you tell must have a message.'},
              {'role': 'system', 'content': 'Remember: this stories are for \
                children so they must have fantasy, adventure and they must \
                teach about aspects of life'},
              {'role': 'user', 'content': prompt}])

title = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    messages=[{'role': 'system', 'content': 'Create a title \
                for a childs book from a story'},
              {'role': 'system', 'content': 'Remember: \
                this title must be short and visual'},
              {'role': 'user', 'content': prompt+"\n"+story.choices[0].message.content}])

image_prompt = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    messages=[{'role': 'system', 'content':'You are a illustrator using Dall-e for inspirational purposes.'},
              {'role': 'user', 'content':  f'Create a DALL-E prompt with this story title: {title.choices[0].message.content}'}]

)


for c in title.choices[0].message.content:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.05)

print("\n")
print("="*75)
print("\n")

for c in story.choices[0].message.content:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.05)

background = openai.Image.create(
  prompt=image_prompt.choices[0].message.content,
  n=1,
  size="512x512"
)
image_url = background['data'][0]['url']

print(f'\nThis is the image we made for your tale:\n \
      {image_url}\nClick the link to see this amazing cover for your book.')

# cost = f'That wonderfull tale just costed you: '+str(int(story.usage.total_tokens)*0.002/1000)+' US dollars'
# for c in cost:
#     sys.stdout.write(c)
#     sys.stdout.flush()
#     time.sleep(0.05)


# print(response.choices[0].message.content)
# print(f'\nThat wonderfull tale just costed you: '+str(round(int(response.usage.total_tokens)*0.002/1000,5))+' US dollars')