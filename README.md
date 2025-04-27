# Agentic RAG Chatbot

This repository implements an `Agentic Retrieval-Augmented Generation (RAG)` chatbot using `LangChain`, `OpenAI`, `Mistral`, and `Chainlit`.  
The system routes user questions intelligently between a local vectorstore and web search, grades document relevance, detects hallucinations, and retries generation if necessary to ensure high-quality answers.

## Features

- `Query Routing`: Smartly routes a query to either the vectorstore (internal documents) or a web search.
- `Vectorstore Retrieval`: Retrieves documents from a SKLearn-based vectorstore if related.
- `Web Search Fallback`: Automatically falls back to Tavily web search when needed.
- `Document Grading`: Grades whether retrieved documents are relevant to the query.
- `Hallucination Detection`: Checks if generated answers are hallucinated.
- `Answer Grading`: Grades whether the generation sufficiently answers the user query.
- `Retry Mechanism`: Retries generation if hallucination is detected.
- `Chainlit Frontend`: Clean, live web app using Chainlit.

## Project Structure

```
├── chainlit.py          # Chainlit app frontend
├── graph.py             # Core graph logic for RAG workflow
├── prompts.py           # Prompt templates
├── schemas.py           # Pydantic models for structured output
├── utils.py             # Utility functions (e.g., format documents)
├── .env                 # Environment variables (API Keys)
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

## Architecture

### Agentic RAG Workflow

![image](https://github.com/user-attachments/assets/9e4c6172-53e5-4f20-a6ff-ab885fea0f56)


**Explanation:**

- **Routing**: When a question is asked, the system first decides if it relates to the internal document index or requires external web search.
- **Retrieve & Grade Documents**: If related to the index, the system retrieves documents and grades them for relevance.
- **Web Search Fallback**: If documents are irrelevant or if routing suggests, the system uses web search.
- **Generate Answer**: Based on retrieved information, the system generates an answer.
- **Hallucination Detection**: After generating, it checks whether the answer contains hallucinations (i.e., made-up information not grounded in facts).
- **Answer Grading**: Finally, it checks if the answer fully addresses the original question.
- **Retry Mechanism**: If hallucination is detected or the answer isn't good enough, the system retries generation with improved retrieval or searching.

This structured workflow ensures **high accuracy**, **factual correctness**, and **relevance** in every response.

## Installation

Clone the repository:

```
git clone https://github.com/ahmad-meda/agentic-rag-chatbot.git
cd agentic-rag-chatbot
```

Install the dependencies:

```
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the root directory and add the following:

```
OPENAI_API_KEY=your-openai-key
LANGCHAIN_API_KEY=your-langchain-key
MISTRAL_API_KEY=your-mistral-key
TAVILY_API_KEY=your-tavily-key
LANGCHAIN_TRACING_V2=true
LANGCHAIN_PROJECT=agentic-rag
TOKENIZERS_PARALLELISM=true
```

## Running the App

Start the Chainlit server:

```
chainlit run chainlit.py -w
```

Access the app at `http://localhost:8000`.

## License

This project is licensed under the MIT License.
![Uploading image.png…]()
