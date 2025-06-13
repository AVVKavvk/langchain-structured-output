from langchain_deepseek import ChatDeepSeek
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()

model = ChatDeepSeek(model="deepseek-chat",max_tokens=100)

parser = JsonOutputParser()

template = PromptTemplate(
  template="Give me a random person name, age and gender \n {format_instructions}",
  input_variables=[],
  partial_variables={"format_instructions":parser.get_format_instructions},
)

chain = template | model | parser

# prompt = template.invoke({})
# result = model.invoke(prompt)
# final = parser.parse(result.content)

result = chain.invoke({})

print(result)

# Issue with json parser is that we can't enforce for schema validation