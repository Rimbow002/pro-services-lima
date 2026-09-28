def fix_name(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    html = html.replace('Pro Services', 'Pro Service')

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)

fix_name('index.html')
fix_name('pro-services-dossier.html')
print('Name fixed')
