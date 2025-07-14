import json
import os
import importlib.util
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../agents')))
from ai.agents.utils import load_agent_config, generate_prompt, get_provider_config

# Load tool registry
REGISTRY_PATH = os.path.join(os.path.dirname(__file__), '../config/registry.json')
with open(REGISTRY_PATH, encoding='utf-8') as f:
    TOOL_REGISTRY = json.load(f)

# Provider loader
PROVIDERS_BASE = os.path.join(os.path.dirname(__file__), '../config/providers')

def load_provider_module(provider_id):
    provider_dir = os.path.join(PROVIDERS_BASE, provider_id)
    provider_py = os.path.join(provider_dir, 'provider.py')
    if not os.path.exists(provider_py):
        raise ImportError(f"Provider module not found: {provider_py}")
    spec = importlib.util.spec_from_file_location(f"provider_{provider_id}", provider_py)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def run_tool_with_fallback(tool_name, input_text):
    providers = TOOL_REGISTRY.get(tool_name, [])
    for provider_id in providers:
        try:
            provider = load_provider_module(provider_id)
            return provider.run(input_text)
        except Exception as e:
            print(f"[Fallback Warning] {provider_id} failed: {e}")
    return {"error": f"❌ সব fallback provider ব্যর্থ হয়েছে: {tool_name}"}

def run_agent(agent_name, input_text, context=""):
    agent_cfg = load_agent_config(agent_name)
    allowed = agent_cfg.get("allowed_providers", [])

    # Dynamic prompt তৈরি
    prompt = generate_prompt(agent_name, input_text, context)

    # Load providers.yaml
    import yaml
    with open("ai/config/providers.yaml", "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)

    for provider_name in config["fallback_priority"]:
        if provider_name not in allowed:
            continue  # Skip if not allowed for this agent
        provider = get_provider_config(provider_name, config)
        if not provider:
            continue
        try:
            print(f"[{agent_name}] Trying {provider_name} with prompt:")
            print(prompt)
            # এখানে API কল বা local মডেল inference পাঠাবে
            # Example response return করা হচ্ছে
            return {"result": f"Response from {provider_name} for prompt:\n{prompt}"}
        except Exception as e:
            print(f"[{provider_name}] failed: {e}")
    return {"error": f"No working provider found for agent {agent_name}"}

# Example usage (for test)
if __name__ == "__main__":
    print(run_tool_with_fallback("chat", "হ্যালো!"))
    agent = "instruct"
    user_question = "Laravel এ middleware কিভাবে ব্যবহার করব?"
    context_history = "আগে আমরা middleware এর গুরুত্ব নিয়ে আলোচনা করেছিলাম।"
    response = run_agent(agent, user_question, context_history)
    print(response["result"]) 