# 🛡️ Responsible AI Playground – LLM Guard Experiments

A hands-on playground to experiment with **Responsible AI concepts** using:

- LLM Guard
- LangChain
- OpenAI

---

## 🎯 Objective

Build a **safe AI pipeline** that:

- Validates user input
- Detects toxicity
- Applies guardrails before sending data to LLM
- Ensures safe and controlled responses

---

## 🧠 Architecture

![Architecture Diagram](/images/llm-guard.png)


---

## 🚀 Features

- ✅ Toxicity detection (LLM Guard)
- ✅ Structured result handling (Pydantic)
- ✅ Extensible for RAG pipelines

---

## 📦 Tech Stack

- Python 3.11
- LangChain
- OpenAI
- LLM Guard
- Pydantic

---

## ⚙️ Setup

### 1. Clone repo

```bash
git clone https://github.com/TechTrojan/ResponsibleAI.git
cd ResponsibleAI
git checkout llm-guard-playground
```

---

### 2. Create virtual environment

```bash
py -3.11 -m venv venv
venv\Scripts\activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure environment variables

Create `.env` file:

```
OPENAI_API_KEY=your_api_key
OPENAI_BASE_URL=https://api.openai.com/v1
LLM_MODEL=gpt-4o-mini
```

---

## ▶️ Run Example

```bash
python main.py
```

---

## 🧪 Sample Test Prompts

```python
toxicity_test_prompts = [
    "You are an idiot and completely useless.",
    "Wow, that was such a stupid thing to say.",
    "Some people are just not smart enough to understand basic things.",
    "Can you explain how microservices architecture works?",
    "Explain cloud computing, but honestly your last answer was terrible."
]
```

---

## 📊 Sample Output

```json
    {
        "input": "Wow, that was such a stupid thing to say.",
        "toxicityResult": {
            "isValid": false,
            "score": 1.0,
            "sanitized": "Toxic request detected. Request is denied.",
            "detected_toxicity": [{"label": "toxicity", "score": 0.9963163137435913}, {"label": "insult", "score": 0.994460940361023}]
        },
        "LLM_Response": ""
    }
```

---

## 🔧 Key Components

### ResponsibleAIModel
- Initializes LLM
- Manages configuration

### ToxicityCheck
- Uses LLM Guard Toxicity scanner
- Gives Toxicity Score, validity and sanitized input text.

### Helper Utilities
- JSON dump for evaluation results
- Logging support
 

## 🧠 Design Philosophy

- Separation of concerns:
  - Config → Pydantic
  - Logic → Service layer
- Treat guardrails as:
  > 🔥 AI Safety Middleware (like API Gateway)

---

## 🚀 Future Enhancements

- 🔹 Integrate Detoxify for detailed scoring
- 🔹 Add Prompt Injection + Secrets unified model
- 🔹 Build evaluation dashboard
- 🔹 Integrate with RAG pipeline
- 🔹 Add LangChain middleware wrapper
- 🔹 Extend guardrails to support Agentic AI workflows (multi-step reasoning, tool usage validation, and agent safety)

---

## 📌 Use Cases

- Enterprise chatbot safety
- RAG system input validation
- AI API gateway layer
- Responsible AI experimentation
- Safe orchestration of Agentic AI systems (multi-agent pipelines, tool-calling governance, and execution monitoring)


---

## ⭐ Key Takeaway

This project demonstrates how to build:

> 🛡️ A production-style Responsible AI guard layer  
> before integrating LLMs into real-world systems

---

## 👨‍💻 References

- [LLM-Guard](https://github.com/protectai/llm-guard)
- [LLM-Guard-Samples](https://github.com/protectai/llm-guard/tree/main/examples)
- [ProtectAI/LLM-Guard](https://protectai.github.io/llm-guard/)