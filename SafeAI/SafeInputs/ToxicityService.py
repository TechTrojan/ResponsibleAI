from llm_guard.input_scanners import Toxicity


class ToxicityResult:    
    
    def __init__(self,sanitized, is_valid, score ):
        self.sanitized = sanitized
        self.is_valid = is_valid
        self.score= score
    
class ToxicityService:
    
    def __init__(self):    
        self.tc = Toxicity() 
    
    def validate_toxicity_check(self,user_input:str):
        
        sanitized,is_valid,score = self.tc.scan(user_input)
        #print(f"Toxicity Score: {score}, Valid: {is_valid}")
        
        if not is_valid:
            sanitized="Toxic request detected. Request is denied."

        return ToxicityResult(
            sanitized= sanitized,
            is_valid=is_valid,
            score=score
        )
        
