import re

def fix_html(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Update experience
    html = html.replace('>10+</h4>', '>+15</h4>')

    # 2. Add tools text
    # Current text in about us:
    # "Tanto para grandes proyectos comerciales como para remodelaciones residenciales, nos diferenciamos por ofrecer un servicio 100% integral. Ya no necesita coordinar con múltiples proveedores"
    old_about = 'Ya no necesita coordinar con múltiples proveedores</p>'
    new_about = 'Ya no necesita coordinar con múltiples proveedores. Contamos con todas las herramientas, equipos y maquinaria disponibles para cualquier tipo de trabajo en todo Lima.</p>'
    html = html.replace(old_about, new_about)

    # 3. Fix missing margin on Gasfitería
    old_gasf = '<!-- Proyecto 3: Gasfitería -->\n            <div>\n                <div class="flex items-center mb-6">'
    new_gasf = '<!-- Proyecto 3: Gasfitería -->\n            <div class="mb-20">\n                <div class="flex items-center mb-6">'
    # Fallback if encoding is weird
    html = re.sub(r'<!-- Proyecto 3: Gasfiter.*?-->\s*<div>', '<!-- Proyecto 3: Gasfitería -->\n            <div class="mb-20">', html)

    # 4. Fix "exploded" heights by replacing aspect-[4/3] with a fixed height responsive class
    # aspect-[4/3] scales dynamically, which makes 2-col grids massive and 4-col grids tiny.
    # By using h-64 md:h-72, they all lock to the same height.
    html = html.replace('aspect-[4/3]', 'h-64 md:h-80')

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)

fix_html('index.html')
fix_html('pro-services-dossier.html')
print("Fixed layout, text, and margins")
