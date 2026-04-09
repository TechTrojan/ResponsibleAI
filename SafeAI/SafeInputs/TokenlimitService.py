
import tiktoken
from tiktoken import Encoding 
from llm_guard.input_scanners import TokenLimit



 

class TokenlimitService:
    VALID_MODELS = ["gpt-4o", "gpt-4o-mini"] 
    ENCODING_NAME = 'o200k_base'
    _encoding:Encoding = None 
    
    def __init__(self, llm_model:str = 'gpt-4o-mini', token_limit:int = 5000):
        
        if not llm_model.lower() in self.VALID_MODELS :
            raise ValueError('Token limit services supports only valid models ' , self.VALID_MODELS )
        
        
        self._llm_model = llm_model
        self._token_limit = token_limit        
        #encoding for model
        self._encoding = tiktoken.get_encoding(self.ENCODING_NAME)
        self._scanner = TokenLimit(limit= self._token_limit,encoding_name= self.ENCODING_NAME,model_name= self._llm_model)      
        
        
    def ValidateInputToken(self,inputPrompt:str)->dict:
        result = {} 
        sanitized_prompt, is_valid, risk_score = self._scanner.scan(inputPrompt)
        token_length = len(self._encoding.encode(inputPrompt))
        
        result = {
            'sanitized_prompt' : sanitized_prompt,
            'is_valid' : is_valid,
            'risk_score' : risk_score ,
            'token_length': token_length
        }
        
        return result 
        
        
                           
        
        
    
                 
    
