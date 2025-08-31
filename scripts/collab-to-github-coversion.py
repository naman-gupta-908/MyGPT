import json
def clean_notebook(path):
    with open(path, "r", encoding="utf-8") as f:
        nb = json.load(f)
    
    # remove broken widget metadata
    if "widgets" in nb.get("metadata", {}):
        nb["metadata"].pop("widgets")
    
    with open(path, "w", encoding="utf-8") as f:
        json.dump(nb, f, indent=2)
    
# usage
clean_notebook("myGPT-v3.ipynb")