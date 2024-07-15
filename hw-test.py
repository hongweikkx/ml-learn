from transformers import pipeline

# 使用 transformers 库加载一个本地模型
qa_pipeline = pipeline("question-answering")

# 提出一个问题并生成答案
context = "Paris is the capital and most populous city of France."
question = "What is the capital of France?"
result = qa_pipeline(question=question, context=context)

print(f"Question: {question}")