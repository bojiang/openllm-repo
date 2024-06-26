
CONSTANT_YAML = '''
alias:
- 7b-4bit
chat_template: gemma-it
engine_config:
  max_model_len: 2048
  model: casperhansen/gemma-7b-it-awq
  quantization: awq
project: vllm-chat
service_config:
  name: gemma
  resources:
    gpu: 1
    gpu_type: nvidia-rtx-3060
  traffic:
    timeout: 300

'''
