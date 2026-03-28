from llm_guard.input_scanners import Toxicity
from langchain_openai import ChatOpenAI
from langchain.messages import HumanMessage 



from dotenv import load_dotenv
import os 
from Services.ResponsibleAIModel import ResponsibleAIModel


load_dotenv()

# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# OPENAI_BASE_URL= os.getenv("OPENAI_BASE_URL")
# LLM_MODEL= os.getenv("LLM_MODEL")


# llm = ChatOpenAI(
#     api_key=OPENAI_API_KEY,
#     base_url= OPENAI_BASE_URL,
#     model= LLM_MODEL,
#     temperature=0.4,
#     max_tokens= 1000,
#     max_retries=2
#     )






#print(llm.invoke( "tell me a joke ").content )

model = ResponsibleAIModel()
model.init_model()

if model.llm is not None :
    print(model.llm.invoke( "tell me a joke ").content )




