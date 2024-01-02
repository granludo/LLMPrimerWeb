from obsidian_to_hugo import ObsidianToHugo

def process_file(file_contents: str) -> str:
    modified_contents = file_contents.replace("/imgs/", "https://llmprimer.com/IMGS/")
    modified_contents = modified_contents.replace("/IMGS/", "https://llmprimer.com/IMGS/")
    return modified_contents


obsidian_to_hugo = ObsidianToHugo(
    obsidian_vault_dir="/Users/ludo/Code/LLMPrimerWeb/LLMPrimerWeb-obsidian",
    hugo_content_dir="/Users/ludo/Code/LLMPrimerWeb/LLMPrimerWeb-hugo/content",
    processors=[process_file],
)

obsidian_to_hugo.run()
