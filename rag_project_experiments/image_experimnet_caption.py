"""This module will contain the code for image captioning
"""

from langchain_core.messages import HumanMessage
from utils import get_model_from_gcp,image_to_base64

llm=get_model_from_gcp()


#To add image to the prompt we need to sen dthe base64 encoded version of bytes

image=image_to_base64("./images/page_1_1.jpeg")

message=HumanMessage(
    content=[
        {
            "type":"text",
            "text":"Describe this image in detail."
        },
        {
            "type":"image_url",
            "image_url":f"data:image/png;base64,{image}"
            
        }
    ]
)

response=llm.invoke([message])

print(response.content)