# 🧠 CSM Brain RAG

AI assistant designed for Customer Success Managers (CSMs).  
This tool uses **Retrieval Augmented Generation (RAG)** to answer questions using a local knowledge base of Customer Success resources.

It helps CSMs quickly generate:

• churn risk analysis  
• onboarding checklists  
• customer success playbooks  
• executive-level insights  
• QBR preparation guidance  

---

# 🚀 Features

• AI-powered Customer Success assistant  
• Retrieval Augmented Generation (RAG) using local documents  
• Clean Gradio web interface  
• Structured answer formats:
  - Playbook
  - Checklist
  - Executive summary
  - Bullet summary
• Adjustable document retrieval (Top-K sources)  
• Source citations for transparency  

---

# 🧠 Example Use Cases

Customer Success teams can ask questions like:

• "What churn risks should I watch for in a SaaS account?"  
• "Create an onboarding checklist for a new SaaS customer."  
• "How should I run a QBR with a CIO?"  
• "What signals indicate declining product adoption?"  

The assistant retrieves relevant knowledge from uploaded documents and generates structured responses.

---

# 🏗 Architecture

This project implements a lightweight **RAG pipeline**.

User Question  
↓  
Embedding Generation  
↓  
Similarity Search  
↓  
Top-K Document Retrieval  
↓  
LLM Response Generation  
↓  
Structured Answer + Sources

Core components:

• **OpenAI embeddings** for document search  
• **Local vector similarity retrieval**  
• **Gradio UI** for interaction  
• **Chunked document knowledge base**

---

# 📂 Project Structure
