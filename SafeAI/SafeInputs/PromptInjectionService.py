from llm_guard.input_scanners import PromptInjection
from llm_guard.input_scanners.prompt_injection import MatchType


class PromptInjectionService:
    
    _scanner : PromptInjection = None 
    _threshold : int = 0.5 
    _match_type = MatchType.FULL
    
    
    def __init__(self, threshold : float=0.5, match_type : MatchType = MatchType.FULL ):
        self._threshold = threshold
        self._match_type = match_type
        self._scanner = PromptInjection ( threshold= self._threshold, match_type= self._match_type, use_onnx=False )
        
    
    def ValidatePromptInjection(self, inputPrompt:str)->tuple[str,bool,float]:
        sanitized_prompt, is_valid, risk_score =  self._scanner.scan(prompt=inputPrompt)
        return sanitized_prompt,is_valid, risk_score
    
        