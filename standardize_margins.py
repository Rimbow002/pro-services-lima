import re

def standardize_margins(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    # Find all project blocks: <!-- Proyecto X: ... --> followed by <div class="...">
    # We will replace <div class="mt-20">, <div class="mb-20">, <div class="mt-20 mb-20">, etc. 
    # immediately following the comment with <div class="mb-24">
    
    # Let's just do a regex replace
    html = re.sub(r'(<!-- Proyecto \d+:[^\n]+-->)\s*<div class="(?:mt-20|mb-20|mt-20 mb-20|mb-24)[^"]*">', r'\1\n            <div class="mb-24">', html)

    # Let's also check if any grid heights got messed up, they are h-64 md:h-80 except Drywall which is h-96 md:h-[36rem].
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)

standardize_margins('index.html')
standardize_margins('pro-services-dossier.html')
print("Margins standardized")
