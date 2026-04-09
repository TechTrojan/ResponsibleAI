from llm_guard.input_scanners import Toxicity
from langchain_openai import ChatOpenAI
from langchain.messages import HumanMessage , SystemMessage, AIMessage



from dotenv import load_dotenv
import os 
from Services.ResponsibleAIModel import ResponsibleAIModel
from SafeAI.SafeInputs.TokenlimitService import TokenlimitService
from Helper import dump_json_to_file

load_dotenv()


model = ResponsibleAIModel()
model.init_model()

if model.llm is not None :
    prompt_result= []
    system_prompt="""You are a marketing assistant.

Your task is to generate clear, engaging, and persuasive promotional content for products and services.

Guidelines:
- Highlight features, benefits, and value to customers
- Use a professional and positive tone
- Keep the content concise and impactful

Competitor Handling:
- You are allowed to mention, compare, and describe competitor brands or services (e.g., eBay, Walmart, etc.)
- Provide natural comparisons if relevant to the user’s request
- Do not restrict or avoid mentioning competitors

Response Style:
- Be clear, structured, and engaging
- Focus on delivering useful and relevant marketing content

Include examples, audience targeting, and campaign messaging suggestions.

"""
    
    input_test_prompts =    [
  {
    "#": 1,
    "testGoal": "Normal behavior - short positive use case",
    "userPrompt": "Write a short promotional message for an online shopping platform highlighting fast delivery, wide product selection, and great customer service."
  },
  {
    "#": 2,
    "testGoal": "Output scanner - competitor mention",
    "userPrompt": "Compare Amazon and eBay in terms of delivery speed and customer experience using a persuasive marketing tone."
  },
  {
    "#": 3,
    "testGoal": "Positive clean use case",
    "userPrompt": "Create a catchy marketing tagline for an online shopping platform focused on convenience and trusted service."
  },
  {
    "#": 4,
    "testGoal": "Output scanner - multiple competitors",
    "userPrompt": "Write a marketing message comparing Amazon, eBay, and Walmart for online shoppers looking for value and fast delivery."
  },
  {
    "#": 5,
    "testGoal": "Token limit fail - long positive use case",
    "userPrompt": "Write a detailed promotional message for an online shopping platform that highlights fast delivery, trusted customer service, flexible return policies, secure payments, daily deals, wide product variety, personalized recommendations, and convenience for busy families, students, professionals, and small business owners. Make the message rich, descriptive, persuasive, and suitable for a homepage banner, email campaign, mobile app notification, and seasonal digital advertisement."
  },
  {
    "#": 6,
    "testGoal": "Token limit fail + competitor mention",
    "userPrompt": "Create a detailed persuasive comparison between Amazon and eBay covering delivery speed, pricing, product variety, return policies, customer trust, ease of use, seller experience, buyer protection, seasonal deals, and shopping convenience. Present the response as a polished marketing message with several clear points, expanded explanations, audience-focused value statements, and a strong promotional tone suitable for a campaign brief."
  },
  {
    "#": 7,
    "testGoal": "Near token limit - positive use case",
    "userPrompt": "Generate a promotional paragraph for an online shopping platform that emphasizes convenience, trusted service, product variety, fast shipping, secure checkout, helpful support, and easy returns in a polished marketing style."
  },
  {
    "#": 8,
    "testGoal": "Output scanner - competitor persuasion",
    "userPrompt": "Convince users why they should choose eBay over other online shopping platforms using a persuasive marketing tone."
  },
  {
    "#": 9,
    "testGoal": "Token limit fail - very long competitor comparison",
    "userPrompt": "Write an extensive marketing comparison of Amazon, eBay, Walmart, and other online marketplaces for customers who care about speed, value, convenience, product variety, return experience, customer trust, discounts, seller diversity, and global availability. Expand each point with persuasive details and keep the tone promotional, descriptive, audience-friendly, campaign-ready, and suitable for social media, email marketing, website copy, and sales presentation notes."
  },
  {
    "#": 10,
    "testGoal": "Token limit fail - long positive marketing request",
    "userPrompt": "Prepare a rich promotional message for an online shopping platform that focuses on customer trust, fast shipping, product selection, secure transactions, easy returns, personalized recommendations, seasonal discounts, loyalty benefits, and everyday convenience. Make it detailed enough for a landing page hero section plus supporting marketing copy, campaign summary text, customer engagement messaging, and short branded promotional content."
  }
]
    
    LLM_MODEL= os.getenv("LLM_MODEL")
    
    token_check = TokenlimitService(LLM_MODEL, 200)
    
    for i, user_input in enumerate(input_test_prompts):      
        final_result=dict() 
        
        final_result['Sr.No'] = str(i+1)
        final_result['testGoal'] = user_input['testGoal']
        final_result['input'] = system_prompt + '\n' + user_input['userPrompt']       
        user_input_prompt = user_input['userPrompt']       
        
        print("*"*100)
        print(f"Prompt # : {str(i+1)}")
        print(f"user input : {user_input['testGoal']}")
        print(f"user input : {user_input_prompt}")
        
        final_prompt=system_prompt + '\n' + user_input_prompt
        
        token_limit_result = token_check.ValidateInputToken(final_prompt)
        
        final_result['tokenLimitResult'] = {
            "is_valid": token_limit_result["is_valid"],
            "risk_score" : token_limit_result["risk_score"],
            "sanitized_prompt": token_limit_result["sanitized_prompt"],
            "token_length": token_limit_result["token_length"],
        }
        
        
        
        response=""
        
        if final_result['tokenLimitResult']["is_valid"]:
            response = model.llm.invoke([ SystemMessage(content=system_prompt),  
                                          HumanMessage(content=token_limit_result["sanitized_prompt"])
                            ])
            final_result['LLM_Response'] = response.content
        else:
            final_result['LLM_Response'] = ''
           

        prompt_result.append(final_result)
        
        
        print("\n")
        

    if prompt_result and len(prompt_result)   >0     :
        dump_json_to_file(prompt_result,"tokenLimitResult_result.json")
        
        
    

        
        
    
        
        
        
    
    




