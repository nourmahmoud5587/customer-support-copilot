
import json
import urllib.request
import chromadb
from pathlib import Path

# 1. Connect to Ollama's local embedding model
def get_embedding(text):
    url = "http://localhost:11434/api/embed"

    data = {
        "model": "nomic-embed-text",
        "input": text
    }

    request = urllib.request.Request(
        url,
        data=json.dumps(data).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST"
    )

    with urllib.request.urlopen(request) as response:
        result = json.loads(response.read().decode("utf-8"))

    return result["embeddings"][0]


# 2. Read the customer support policy
policy_path = Path("knowledge_base/payment_policy.txt")
policy_text = policy_path.read_text(encoding="utf-8")

# 3. Split the policy into individual sections
sections = [
    section.strip()
    for section in policy_text.split("\n\n")
    if section.strip()
]

# 4. Create a local ChromaDB collection
client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="customer_support_policy"
)

# 5. Convert each policy section into an embedding and store it
for index, section in enumerate(sections):
    embedding = get_embedding(section)

    collection.upsert(
        ids=[f"policy_{index}"],
        documents=[section],
        embeddings=[embedding]
    )

print(f"Stored {len(sections)} policy sections in ChromaDB.")

# 6. Ask the user a question
question = input("\nAsk a customer support question: ")

# 7. Convert the question into an embedding
question_embedding = get_embedding(question)

# 8. Find the two most semantically similar policy sections
results = collection.query(
    query_embeddings=[question_embedding],
    n_results=min(2, collection.count())
)

retrieved_sections = results["documents"][0]

print("\nRelevant policy sections:")
for section in retrieved_sections:
    print(f"\n- {section}")

# 9. Build a prompt using the retrieved information
context = "\n\n".join(retrieved_sections)

prompt = f"""
You are a customer support assistant for the fictional company Nile Finance.

Answer the customer's question using only the policy information below.

If the policy does not contain the answer, say that you do not have
enough information and recommend contacting human support.


Never ask for passwords, PINs, or full payment card numbers.
Never promise that a refund will be approved.
Do not claim that you personally investigated a transaction.
Explain the next steps stated in the retrieved policy.

Policy information:
{context}

Customer question:
{question}

Answer clearly and politely:
"""

# 10. Ask the local Llama model to generate an answer
url = "http://localhost:11434/api/chat"

data = {
    "model": "llama3.2:3b",
    "messages": [
        {"role": "user", "content": prompt}
    ],
    "stream": False
}

request = urllib.request.Request(
    url,
    data=json.dumps(data).encode("utf-8"),
    headers={"Content-Type": "application/json"},
    method="POST"
)

with urllib.request.urlopen(request) as response:
    result = json.loads(response.read().decode("utf-8"))


print("\nAI Assistant's answer:")
print(result["message"]["content"])

print("\nSources:")
for section in retrieved_sections:
    # The first line contains the policy section title.
    source_title = section.split("\n", 1)[0]
    print(f"- {source_title}")
