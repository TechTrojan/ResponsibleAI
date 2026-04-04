import requests    


class ResponsibleAIModel:
    url = "http://localhost:11434/api/generate"

    
     
    
    def init_model(self):
        pass 
    
    def invoke(self,system_prompt:str, user_prompt:str)-> str :
        payload = {
                "model": "tinyllama",
                "system" : system_prompt,
                "prompt": user_prompt, 
                "stream": False
            }
        
        result = None 
        try:            

            response = requests.post(self.url, json=payload)
            result = response.json()['response']
        except Exception as e:
            result="Error from LLM : " + str(e)
            
            print(str(e))
        
        return result
            


    
    
    
    
