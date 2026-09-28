def add_text(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    old_chunk = 'acabados de nivel premium.'
    new_chunk = 'acabados de nivel premium.\n                    </p>\n                    <p class="text-gray-600 text-lg leading-relaxed mb-8">\n                        Contamos con todas las herramientas, equipos y maquinaria disponibles para cualquier tipo de trabajo en todo Lima.'

    if 'herramientas' not in html:
        html = html.replace(old_chunk, new_chunk)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)

add_text('index.html')
add_text('pro-services-dossier.html')
print("Done")
