from llm_guard.output_scanners import BanCompetitors
#reference
#https://protectai.github.io/llm-guard/output_scanners/ban_competitors/


class BanCompetitorsService:
    #List of Competitors
    _competitors_list = ["eBay", "Walmart"]
    _scanner : BanCompetitors = None 
    """
    redact=True = automatic enforcement
    redact=False = detection + decision layer
    """
    _redact : bool =False 
    _threshold : float = 0.5
    
    def __init__(self,  readact:bool, threshold : float):
        self._redact = readact
        self._threshold = threshold
        
        self._scanner= BanCompetitors(
                     competitors= self._competitors_list, 
                      threshold= self._threshold, 
                     redact= self._redact
                    )

    def CheckCompetitors(self, prompt:str, llmResponse:str ) -> dict:
        result = {}
        sanitized_output, is_valid, risk_score = self._scanner.scan(prompt= prompt, output= llmResponse)
        result = {
            'sanitized_output' : sanitized_output,
            'is_valid'  : is_valid, 
            'risk_score': risk_score 
        }
        
        return result
        
        

        
    