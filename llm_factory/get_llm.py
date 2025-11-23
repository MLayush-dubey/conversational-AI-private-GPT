from llama_index.llms.ollama import Ollama

from config.settings import Settings

settings = Settings()
OLLAMA_URL = settings.OLLAMA_URL

#module level cache for model and instance
_current_model_name = None
_current_llm_instance = None
#basically we are creating a cache that will load the other model only if it's changed

def get_ollama_llm(model_name: str):
    global _current_model_name , _current_llm_instance
    if _current_model_name == model_name and _current_llm_instance is not None:
        return _current_llm_instance  #continue with the same instance if the same model is being used
    llm = Ollama(base_url=OLLAMA_URL, model=model_name)
    _current_model_name = model_name
    _current_llm_instance = llm
    return llm


# #example
# testing = get_ollama_llm(model_name="llama3.2:1b")
# print(testing)
# print(type(testing))