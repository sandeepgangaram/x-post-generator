import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

def generate_x_post(topic:str)->str:

    prompt = f'''
        You are an expert social media manager, and you excel at crafting viral and highly engaging posts for the platform X (formerly twitter).

        Your task is to generate a post that is concise, and tailored to the topic provided by the user.
        Avoid using hashtags and lots of emojis (a few emojis are okay, but not too many).

        Keep the post short and focused, structure it in a clean, readable way, using line breaks and empty lines to enhance readability.

        Here's the topic provided by the user for which you need to generate a post:
        <topic>
        {topic}
        </topic>    
        
        Here are some examples of topics and generated posts:
        <examples>
            <example-1>
                <topic>
                 Rose
                </topic>

                <generated-post>
                    A rose is a rose is a rose.
                </generated-post>
            </example-1>

            <example-2>
                <topic>
                    Rain
                </topic>

                <generated-post>
                    When in pain all you need is rain.
                </generated-post>
            </example-2>
        </examples>

        Use the same tone, language, structure and style of the examples provided above to generate a post that is engaging and relevant
        to the topic provided by the user. Don't use content from the examples!
        '''

    response = client.responses.create(
    model="gpt-4o-mini",
    input=prompt
)

    return response.output_text
    

def main():
    user_input = input("What you want the post to be about? ")
    x_post = generate_x_post(user_input)
    print(x_post)


if __name__ == "__main__":
    main()
