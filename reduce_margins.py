def reduce_margins(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    # Replace mb-24 with mb-12 to reduce the gap between projects by half
    html = html.replace('class="mb-24"', 'class="mb-12"')

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)

reduce_margins('index.html')
reduce_margins('pro-services-dossier.html')
print("Margins reduced")
