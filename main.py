import os
import json
import sys
import boto3

# Properly formatted prompt for Llama 3
prompt = """<|begin_of_text|><|start_header_id|>user<|end_header_id|>
You are a smart assistant, so please let me know what is machine learning in the smartest way?<|eot_id|><|start_header_id|>assistant<|end_header_id|>
"""

bedrock = boto3.client(service_name="bedrock-runtime")

# Payload structure for Llama 3
payload = {
    "prompt": prompt,
    "max_gen_len": 512,
    "temperature": 0.9,
    "top_p": 0.9
}

body = json.dumps(payload)
model_id = "meta.llama3-70b-instruct-v1:0"

# Fixed parameter names: modelId (not model_id), contentType (not content_type)
response = bedrock.invoke_model(
    body=body,
    modelId=model_id,          # Fixed: modelId (camelCase)
    accept="application/json",
    contentType="application/json"  # Fixed: contentType (camelCase)
)

response_body = json.loads(response.get("body").read())
response_text = response_body["generation"]

print(response_text)