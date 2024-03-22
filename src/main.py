from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("EleutherAI/gpt-neo-125M")
model = AutoModelForCausalLM.from_pretrained("EleutherAI/gpt-neo-125M")

# Your prompt goes here. This is an example of a simple Python function prompt.
prompt = "Write a Python function to add two numbers"

# Encode the prompt text to tensor
input_ids = tokenizer.encode(prompt, return_tensors="pt")

# Generate a response to the prompt
outputs = model.generate(input_ids, max_length=512, num_return_sequences=1)

# Decode the generated text
generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

print(generated_text)
