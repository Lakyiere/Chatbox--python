#!/usr/bin/env python
# coding: utf-8

# # CHATBOX

# In[1]:


name=str(input())
print("What should i call you my friend:", name)


# USER TEMPLATES

# In[2]:


bot_template = "BOT : {0}"
user_template = name + " : {0}"


# CHATBOX RESPONSES

# In[3]:


name = "Alice the Programmer" 
weather = "Rainy" 
mood = "Happy"

responses = { 
"what's your name?": [ 
"They call me {0}".format(name), 
"I usually go by {0}".format(name), 
"My name is the {0}".format(name) ],
    
"what's today's weather?": [ 
"The weather is {0}".format(weather), 
"It's {0} today".format(weather), 
"Let me check, it looks {0} today".format(weather) ],
    
"Are you a robot?": [ 
"What do you think?", 
"Maybe yes, maybe no!", 
"Yes, I am a robot with human feelings.", ],
    
"how are you?": [ 
"I am feeling {0}".format(mood), 
"{0}! How about you?".format(mood), 
"I am {0}! How about yourself?".format(mood), ],
"": [ 
"Hey! Are you there?", 
"What do you mean by saying nothing?", 
"Sometimes saying nothing tells a lot :)", ],
"default": [
"this is a default message"] }


# In[4]:


import random


# RESPONSE FUNCTION

# In[5]:


def respond(message):
    if message in responses: 
        bot_message = random.choice(responses[message])
    else: 
        bot_message = random.choice(responses["default"])
    return bot_message    


# RELATION FUNCTION

# In[6]:


def related(x_text): 
    if "name" in x_text: 
        y_text = "what's your name?"
    elif "weather" in x_text: 
        y_text = "what's today's weather?"
    elif "robot" in x_text: 
        y_text = "are you a robot?"
    elif "how are" in x_text: 
        y_text = "how are you?"
    else: 
        y_text = ""
    return y_text


# SEND MESSAGE FUNCTION 

# In[7]:


def send_message(message): 
    print(user_template.format(message)) 
    response = respond(message) 
    print(bot_template.format(response))


# TESTING THE CHATBOX

# In[ ]:


while 1: 
    my_input = input() 
    my_input = my_input.lower() 
    related_text = related(my_input) 
    send_message(related_text)
    if my_input == "exit" or my_input == "stop": 
        break


# In[ ]:





# In[ ]:




