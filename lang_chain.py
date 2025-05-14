"""
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

llm = OpenAI(temperature=0.7)

prompt = PromptTemplate(
    input_variables=["topic"],
    template="Explain {topic} in simple terms."
)

chain = LLMChain(llm=llm, prompt=prompt)

response = chain.run("quantum computing")
print(response)
"""

from transformers import pipeline

# Use a pre-trained model for text generation
generator = pipeline("text-generation", model="gpt2")

# Generate a response
response = generator("Explain quantum computing in simple terms.", max_length=50, num_return_sequences=1)
print(response[0]["generated_text"])