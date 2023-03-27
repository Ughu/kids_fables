import openai
import os
import time
import sys


openai.api_key_path = ".env"

prompt = input("I tell stories.\nSo, please ask me for a story about anything: ")

print('Wait, your story is being created... \n')

story = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    messages=[{'role': 'system', 'content': 'You tell stories for children.\
                The stories you tell must have dialogues. Also the story should be soulful and very visual'},
              {'role': 'user', 'content': prompt}])

title = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    messages=[{'role': 'user', 'content': f'Create a title \
                for a childs book from a story. \
                This is the story: {story.choices[0].message.content}'}])

image_prompt = openai.ChatCompletion.create(
    model='gpt-3.5-turbo',
    messages=[{'role': 'user', 'content': f'Create a prompt for a text to image AI application from titles generated by chat gpt. \
                This is the title: {title.choices[0].message.content}. \
                The prompt must be very descriptive and it must paint a picture that summarizes the title story'}]
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
  prompt=f"{image_prompt['choices'][0]['message']['content']}; as a digital collorful illustration",
  n=1,
  size="512x512"
)

image_url = background['data'][0]['url']

print(f'\n\nThis is the image we made for your tale:\n \
      {image_url}\nClick the link to see this amazing cover for your book.')

# cost = f'That wonderfull tale just costed you: '+str(int(story.usage.total_tokens)*0.002/1000)+' US dollars'
# for c in cost:
#     sys.stdout.write(c)
#     sys.stdout.flush()
#     time.sleep(0.05)


# print(response.choices[0].message.content)
# print(f'\nThat wonderfull tale just costed you: '+str(round(int(response.usage.total_tokens)*0.002/1000,5))+' US dollars')