import os
from openai import OpenAI, AsyncOpenAI
from ragas.llms import llm_factory 
from ragas.embeddings.base import embedding_factory

client = OpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"), # 如何获取API Key：https://help.aliyun.com/zh/model-studio/developer-reference/get-api-key
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

aclient = AsyncOpenAI(
    api_key=os.getenv("DASHSCOPE_API_KEY"), # 如何获取API Key：https://help.aliyun.com/zh/model-studio/developer-reference/get-api-key
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

def invoke(user_message, model_name="qwen-plus"):
    completion = client.chat.completions.create(
        model=model_name, # 模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models
        messages=[{"role": "user", "content": user_message}]
    )
    # 生产环境建议考虑调用异常的处理
    return completion.choices[0].message.content

def invoke_with_stream_log(user_message, model_name="qwen-plus"):
    completion = client.chat.completions.create(
        model=model_name, # 模型列表：https://help.aliyun.com/zh/model-studio/getting-started/models
        messages=[{"role": "user", "content": user_message}],
        stream=True
    )
    result = ""
    for response in completion:
        result += response.choices[0].delta.content
        print(response.choices[0].delta.content, end="")
    # 生产环境建议考虑调用异常的处理
    return result

def ragas_llm(model_name="qwen-plus"):
    return llm_factory(
        model=model_name,
        client=aclient,
    )

def ragas_embedding(model_name="text-embedding-v3"):
    return embedding_factory(
        model=model_name,
        client=aclient,
    )
