from obsidian_to_hugo import ObsidianToHugo

def process_file(file_contents: str) -> str:
    modified_contents = file_contents.replace("/imgs/", "https://wasabi.essi.upc.edu/llmprimer/IMGS/")
    modified_contents = modified_contents.replace("/IMGS/", "https://wasabi.essi.upc.edu/llmprimer/IMGS/")
    return modified_contents


obsidian_to_hugo = ObsidianToHugo(
    obsidian_vault_dir="/Users/ludo/Code/LLMPrimerWeb/LLMPrimerWeb-obsidian",
    hugo_content_dir="/Users/ludo/Code/LLMPrimerWeb/LLMPrimerWeb-hugo/content",
    processors=[process_file],
)

obsidian_to_hugo.run()
