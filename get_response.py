#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def get_response(text, topic):
    from openai import OpenAI
    my_key=""
    client = OpenAI(api_key=my_key)
    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=
        [
        {"role": "system", "content": "You are provided with a medical research article."},
        {"role": "user", "content": f"""Assess the following article.'''{text}'''.
        IF there is information related to {topic} in the article, 
        THEN provide a summary of the article. Be concise and keep only most important points;
        ELIF there is no Abstract,
        THEN return just the following statement <No abstract available>;
        ELIF information in the article does not relate to {topic} 
        THEN return just the following statement <This article does not pertain to {topic}>"""}
        ], 
    temperature = 0)
    return response.choices[0].message.content

