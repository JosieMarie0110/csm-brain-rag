# CS Brain

**AI-powered strategy assistant for Customer Success Managers**

CS Brain is a lightweight AI tool designed to help Customer Success Managers generate **strategic responses, risk analysis, and executive-ready messaging** based on Customer Success best practices.

The tool acts as a **CSM knowledge assistant**, helping translate complex customer situations into structured insights and actionable communication.

This project was built as part of a **Customer Success AI toolkit** designed to support real-world CS workflows such as account strategy, incident communication, and customer risk evaluation.

---

## Why This Project Exists

Customer Success Managers often need to quickly:

- assess customer health signals  
- craft executive-ready messaging  
- respond to incidents  
- align product usage with business outcomes  
- prepare for QBR / EBR discussions  

However, most tools focus on **product analytics**, not **strategic thinking and communication**.

**CS Brain bridges that gap** by helping CSMs structure their thinking into **clear, strategic outputs**.

---

## Key Features

**Structured Strategic Responses**

Transforms open-ended questions into clear, structured guidance aligned with Customer Success best practices.

**Multiple Response Formats**

Users can choose how they want the output structured, including:

- Strategic guidance  
- Executive summaries  
- Customer messaging  
- Playbooks and action plans  

**Customer Success Knowledge Assistant**

The system uses a knowledge base of Customer Success concepts to help generate responses aligned with common CS frameworks.

**Fast Idea Generation**

CSMs can quickly brainstorm messaging or strategy when preparing for:

- customer calls  
- renewal discussions  
- internal strategy meetings  
- executive updates  

---



<img width="1502" height="1125" alt="image" src="https://github.com/user-attachments/assets/de9a2d9e-a9d6-4c12-b19c-925e01f462d4" />


<img width="1498" height="1129" alt="image" src="https://github.com/user-attachments/assets/4939f34f-c0a0-471e-9d7a-3e535cc940ac" />

<img width="1488" height="1278" alt="image" src="https://github.com/user-attachments/assets/7c47c43e-ad75-4a2a-8e60-b6f954bb4dd5" />



<img width="1001" height="1080" alt="image" src="https://github.com/user-attachments/assets/f1161a17-80bf-4591-b8e9-8da5593cd2fb" />



## Example Use Cases

### Account Risk Evaluation

**Input**

Customer adoption has declined and engagement with the platform has dropped over the past quarter.

**Output**

Structured analysis outlining potential risk signals, recommended actions, and communication strategies.

---

### Executive Communication

**Input**

Need to explain an incident impact to a customer executive.

**Output**

Clear executive-ready messaging summarizing the situation, impact, and next steps.

---

### Strategic Customer Planning

**Input**

Customer is expanding infrastructure and evaluating additional solutions.

**Output**

Strategic guidance on positioning value and aligning the platform with customer objectives.

---

## Tech Stack

- Python  
- Gradio (UI framework)  
- OpenAI API  
- PDF knowledge ingestion (RAG-style knowledge base)

---

## How It Works

1. The user enters a question or customer scenario.
2. CS Brain retrieves relevant context from the knowledge base.
3. The AI generates a **structured response based on the selected output format.**
4. The result helps the CSM quickly produce **clear, professional communication or strategy guidance.**

---

## Running the Project Locally

Clone the repository

```
git clone https://github.com/YOUR_USERNAME/csm-brain-clean.git
cd csm-brain-clean
```

Create a virtual environment

```
python3 -m venv venv
source venv/bin/activate
```

Install dependencies

```
pip install -r requirements.txt
```

Set your OpenAI API key

```
export OPENAI_API_KEY="your_api_key_here"
```

Run the app

```
python app_gradio.py
```

---

## Future Improvements

- improved response structuring  
- additional Customer Success frameworks  
- enhanced knowledge base ingestion  
- playbook expansion  
- integration with other CS AI tools  

---

## Part of a Larger Customer Success AI Toolkit

This project is part of a broader set of experimental tools exploring how AI can assist Customer Success teams.

Related projects include:

**Customer Signal Analyzer**  
Analyzes customer communication to detect risk, resistance, or alignment signals.

**Incident to Executive Translator**  
Converts technical incident descriptions into executive-ready communication.

**Business Outcome Translator (planned)**  
Maps product adoption signals to measurable business outcomes.

---

## Author

Built by a Customer Success professional with **15+ years of experience in SaaS, cybersecurity, and technical account management**, exploring how AI can support modern Customer Success workflows.
