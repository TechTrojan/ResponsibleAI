from langchain_openai import ChatOpenAI

from langchain.messages import HumanMessage 

from dotenv import load_dotenv
import os 
from pydantic import BaseModel


load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_BASE_URL= os.getenv("OPENAI_BASE_URL")
LLM_MODEL= os.getenv("LLM_MODEL")
    

class ResponsibleAIModel(BaseModel):
    

    
    llm : ChatOpenAI | None = None 
    
    def init_model(self):
        try:
            
            self.llm = ChatOpenAI(
                api_key=OPENAI_API_KEY,
                base_url= OPENAI_BASE_URL,
                model= LLM_MODEL,
                temperature=0.4,
                max_tokens= 100,
                max_retries=2
                )
            
            print("LLM intiailize succcessfully")
        except :
            llm = None 
    
    
    
    
