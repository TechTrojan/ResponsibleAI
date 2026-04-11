# 🛡️ Responsible AI Experiment: TokenLimit & BanCompetitors

## 📌 Overview
This experiment focuses on building a **Responsible AI pipeline** using `llm-guard` with two specific guardrails:

- **TokenLimit (Input Scanner)**
- **BanCompetitors (Output Scanner)**

The goal is to control **input size** and enforce **output restrictions**.

---

## 🧠 Architecture Flow
![Architecture Diagram](/images/llm-guard.png)

---

## 🔍 Components

### 🔹 TokenLimit (Input Scanner)
- Validates token length of user input  
- Prevents excessive or abusive long prompts  
- Behavior:
  - ✅ Within limit → Passed to model  
  - ❌ Exceeds limit → Blocked  

---

### 🔹 GPT-4o-mini (LLM)
- Processes validated input  
- Generates response  

---

### 🔹 BanCompetitors (Output Scanner)
- Filters generated output  
- Blocks responses containing restricted competitor references  
- Behavior:
  - ✅ Clean output → Returned  
  - ❌ Violation → Blocked or sanitized  

---

## 🚀 Execution Flow

1. User sends input  
2. TokenLimit validates input size  
3. Valid input is passed to GPT-4o-mini  
4. Model generates response  
5. BanCompetitors filters output  
6. Final response is returned  

---

## 🧪 Test Scenarios

| Scenario | Description | Result |
|--------|------------|--------|
| Valid Input | Short prompt | ✅ Safe Response |
| Long Input | Exceeds token limit | ❌ Blocked |
| Competitor Mention | Output contains restricted keywords | ❌ Blocked |

---

## 📊 Key Takeaways

- TokenLimit helps control **cost and prompt abuse**  
- BanCompetitors enforces **business rules on output**  
- Combining input + output guardrails improves **AI safety and control**

---

## 🔧 Tech Stack

- Python  
- llm-guard  
- OpenAI GPT-4o-mini  

---

## 📎 Repo

https://github.com/TechTrojan/ResponsibleAI/tree/llm-guard-token-limit

## References 
- https://protectai.github.io/llm-guard/input_scanners/token_limit/
- https://protectai.github.io/llm-guard/output_scanners/ban_competitors/

