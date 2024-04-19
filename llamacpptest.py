from llama_cpp import Llama

llm = Llama(
  model_path="/home/sujit/Downloads/text-generation-webui-main/models/TheBloke_openchat-3.5-0106-GGUF/openchat-3.5-0106.Q4_K_M.gguf",  
  n_ctx=1024,  n_threads=8, n_gpu_layers=10)

while True:
    prompt=input("\nUser: ")

    output = llm.create_chat_completion(
        messages=[{ "role": "user", "content": "You are a personal assistant." },
            { "role": "assistant","content": prompt}],
        stream=True
    )

    for chunk in output:
        delta = chunk['choices'][0]['delta']
        if 'role' in delta:
            print(delta['role'], end=': ')
        elif 'content' in delta:
            if delta['content'] !="":
                print(delta['content'], end='')
