#  Customer Support Copilot

## 📸 Application Screenshot

![Customer Support Copilot application](./Customer%20Support%20Copilot.png)

An AI-powered customer support assistant built with Python, Streamlit, local Large Language Models (LLMs), and Retrieval-Augmented Generation (RAG).

The application helps customers find answers to payment-related questions using a fictional finance company's knowledge base. It can retrieve relevant policy information, generate answers, display policy sources, and support the creation of customer support tickets.

##  Features

- **AI-powered conversations:** Ask questions about payments, failed transactions, and refunds.
- **Retrieval-Augmented Generation (RAG):** Retrieve relevant information from a payment policy before generating an answer.
- **Semantic search:** Use vector embeddings to find policy sections that are relevant to a question.
- **Source references:** Display the policy sections used to answer questions.
- **Support-ticket creation:** Create tickets for issues that may require human assistance.
- **Conversation history:** Maintain context during a chat session.
- **Local AI models:** Run the language model and embedding model locally using Ollama, without requiring a paid LLM API key.
- **Interactive interface:** Chat with the assistant through a Streamlit web application.

##  Technologies

- Python
- Streamlit
- Ollama
- Llama 3.2 (3B)
- ChromaDB
- Nomic Embed Text
- Retrieval-Augmented Generation (RAG)
- Vector embeddings and semantic search
- JSON-based ticket storage

##  How It Works

1. A customer submits a question through the Streamlit interface.
2. The application converts the question into an embedding.
3. ChromaDB retrieves relevant sections from the payment policy.
4. The retrieved information is provided to the local language model as context.
5. The model generates a response based on the available policy information.
6. Relevant policy sources are displayed to the customer.
7. For issues that may need human assistance, the application can offer a support-ticket form.

##  Project Structure

```text
customer-support-copilot/
├── app.py
├── agent_assistant.py
├── semantic_rag.py
├── support_tools.py
├── requirements.txt
├── .gitignore
├── README.md
└── knowledge_base/
    └── payment_policy.txt
```

##  Setup and Installation

### Prerequisites

- Python 3.10 or newer
- [Ollama](https://ollama.com/)
- Git (optional if downloading the repository as a ZIP file)

### 1. Clone the repository

```bash
git clone https://github.com/nourmahmoud5587/customer-support-copilot.git
cd customer-support-copilot
```

Alternatively, download the repository as a ZIP file from GitHub and extract it.

### 2. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Download the Ollama models

```bash
ollama pull llama3.2:3b
ollama pull nomic-embed-text
```

Make sure Ollama is running before starting the application.

### 5. Build the local policy index

```bash
python semantic_rag.py
```

This prepares the policy's vector embeddings and stores them in the local ChromaDB database.

### 6. Launch the application

```bash
streamlit run app.py
```

Open the local URL displayed in the terminal, usually `http://localhost:8501`.

##  Example Questions

- How long should I wait before retrying a failed payment?
- I was charged twice. Can I get a refund?
- What should I do if a payment failed but money was deducted?
- How can I report an unauthorized transaction?

##  Privacy and Limitations

- This project is an educational portfolio demonstration using a fictional finance-company policy.
- The language model runs locally through Ollama.
- Never enter real customer information, passwords, PINs, or full payment card numbers.
- Ticket records are stored locally in a JSON file.
- Generated answers may be inaccurate; important financial issues should be reviewed by human support.
- This project is not connected to a real financial institution or payment system.

##  Future Improvements

- Automated tests for retrieval, responses, and ticket creation.
- Evaluation of answer relevance and retrieval quality.
- Improved input validation and sensitive-data protection.
- A database for support tickets.
- Deployment and continuous integration.

##  Author

**Nour Mahmoud**

Computer Science graduate specializing in Artificial Intelligence.

email: [nourmahmoud5587@gmail.com]
