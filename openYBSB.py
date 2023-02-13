import os
import openai

def ai_it():
  #Remember to update the text file with you API key    
  openai.api_key_path="apikey.txt"

  f = open('history.txt', 'r')
  memory = []

  #You can change this variable to adjust the number of previous messages that will be sent to openai (Remember you're probably paying for it kek)
  memorySize = 4

  #Here you can adjust the AI personality and atributes, this is sent everytime with the history to the API
  description = "<Insert personality description here>, you're in a discord chat, every message has the name of who said it like name:message, your handle is <AI Handle here>"

  for line in f:
    memory.append(line)

  #Very very very dumb way of doing it, but I ran out of energy drinks here
  for i in range(len(memory) - memorySize):
    memory.pop(0)

  input = description+"\n"
  for mem in memory:
    input = input + mem
  print(input)

  #If you know what you're doing you can adjust the API call
  #A good ideia would be to use something else as the model, since "text-davinci-003" is the most expencive model
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=input+"\n",
    temperature=0.8,
    max_tokens=50,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )

  output = "\n"+response.choices[0].text 

  fw = open('history.txt', 'a+')
  fw.write(output)
  fw.close()

  return output.partition(' ')[2]

#print(response.choices[0].text)

