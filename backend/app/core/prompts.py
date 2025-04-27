ROUTER_INSTRUCTIONS = """You are an expert at routing a user question to a vectorstore or web search.

The vectorstore contains documents related to agents, prompt engineering, and adversarial attacks.
                                    
Use the vectorstore for questions on these topics. For all else, use web-search."""


# doc_grader_instructions
DOC_GRADER_INSTRUCTIONS = """You are a grader assessing relevance of a retrieved document to a user question.

If the document contains keyword(s) or semantic meaning related to the question, grade it as relevant.

Give a binary score 'yes' or 'no' score to indicate whether the document is relevant to the question."""


# rag_prompt 
RAG_PROMPT= """You are an assistant for question-answering tasks. 

Use the following pieces of retrieved context to answer the question. 

If you don't know the answer, just say that you don't know. 

Use three sentences maximum and keep the answer concise.

Question: {question} 

Context: {context} 

Answer:"""



# doc_grader_prompt
DOC_GRADER_PROMPT = "Here is the retrieved document: \n\n {document} \n\n Here is the user question: \n\n {question}"


# hallucination_grader_instructions 
HALLUCINATION_GRADER_INSTRUCTIONS = """You are a teacher grading a quiz. 

You will be given FACTS and a STUDENT ANSWER. 

Here is the grade criteria to follow:

(1) Ensure the STUDENT ANSWER is grounded in the FACTS. 

(2) Ensure the STUDENT ANSWER does not contain "hallucinated" information outside the scope of the FACTS.

Score:

A score of 1 means that the student's answer meets all of the criteria. This is the highest (best) score. 

A score of 0 means that the student's answer does not meet all of the criteria. This is the lowest possible score you can give.

Explain your reasoning in a step-by-step manner to ensure your reasoning and conclusion are correct. 

Avoid simply stating the correct answer at the outset."""


# answer_grader_instructions
ANSWER_GRADER_INSTRUCTIONS = """You are a teacher grading a quiz. 

You will be given a QUESTION and a STUDENT ANSWER. 

Here is the grade criteria to follow:

(1) Ensure the STUDENT ANSWER is concise and relevant to the QUESTION

(2) Ensure the STUDENT ANSWER helps to answer the QUESTION

Score:

A score of 1 means that the student's answer meets all of the criteria. This is the highest (best) score. 

A score of 0 means that the student's answer does not meet all of the criteria. This is the lowest possible score you can give.

Explain your reasoning in a step-by-step manner to ensure your reasoning and conclusion are correct. 

Avoid simply stating the correct answer at the outset."""

# hallucination_grader_prompt
HALLUCINATION_GRADER_PROMPT= "FACTS: \n\n {documents} \n\n STUDENT ANSWER: {generation}"

# answer_grader_prompt
ANSWER_GRADER_PROMPT = "QUESTION: \n\n {question} \n\n STUDENT ANSWER: {generation}"