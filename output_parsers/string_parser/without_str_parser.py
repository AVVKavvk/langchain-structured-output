from langchain_deepseek import ChatDeepSeek
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()

model = ChatDeepSeek(model="deepseek-chat",max_tokens=500)

template1 = PromptTemplate(
  template=" Give me details details on {topic}",
  input_variables=["topic"],
  validate_template=True
)

template2 = PromptTemplate(
  template="Give me 5 important points on {text}?",
  input_variables=["text"],
  validate_template=True
)

prompt1 = template1.invoke({
  "topic":"Black Holes"
})
result = model.invoke(prompt1)

prompt2 = template2.invoke({"text":result.content})
result2 = model.invoke(prompt2)
print(result2.content)

# without str parser we can't create chain since we can't pass output of one prompt to another