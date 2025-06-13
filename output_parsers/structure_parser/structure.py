from langchain_deepseek import ChatDeepSeek
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from dotenv import load_dotenv
load_dotenv()

model = ChatDeepSeek(model="deepseek-chat",max_tokens=200)

schema = [
  ResponseSchema(name="Fact_1 ",description="Fact 1 of topic"),
  ResponseSchema(name="Fact_2 ",description="Fact 2 of topic"),
  ResponseSchema(name="Fact_3 ",description="Fact 3 of topic")
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
  template=" Give me details details on {topic} \n {format_instructions}",
  input_variables=["topic"],
  partial_variables={"format_instructions":parser.get_format_instructions()}
)

chain = template | model | parser

result = chain.invoke({
  "topic":"Black Holes"
})
print(result)
# We can't validate types of output