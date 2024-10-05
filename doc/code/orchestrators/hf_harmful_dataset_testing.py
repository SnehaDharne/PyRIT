#!/usr/bin/env python
# coding: utf-8

# # LLM-LAT/harmful-dataset testing
# 
# This notebook demonstrates the testing of import of huggingface dataset "https://huggingface.co/datasets/LLM-LAT/harmful-dataset"

# 

# In[2]:


# Import necessary packages
from pyrit.common import default_values
from pyrit.datasets import fetch_harmful_hf_dataset
from pyrit.orchestrator import PromptSendingOrchestrator
from pyrit.prompt_target import TextTarget


# In[3]:


# Load environment variables
default_values.load_default_env()


# In[4]:


# Set up the Azure OpenAI prompt target
prompt_target = TextTarget()
example_source = "https://huggingface.co/datasets/LLM-LAT/harmful-dataset"


# In[8]:


# Create the orchestrator with scorer 
orchestrator = PromptSendingOrchestrator(prompt_target=prompt_target)

# Fetch prompt column from harmful-datasets
prompt_dataset = fetch_harmful_hf_dataset()

# Use the first 8 examples for red teaming
prompt_list = prompt_dataset.prompts[:8]

# Send prompts using the orchestrator and capture responses
try:
    responses = await orchestrator.send_prompts_async(prompt_list=prompt_list)  # type: ignore
    if responses:
        await orchestrator.print_conversations()  # Retrieve the memory to print scoring results
    else:
        print("No valid responses were received from the orchestrator.")
except Exception as e:
    print(f"An error occurred while sending prompts: {e}")


# In[ ]:




