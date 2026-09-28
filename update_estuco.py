import re

def update_estuco(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    # The block might be inside grid-cols-2 because of our rebuild.
    # We will find <!-- Proyecto 5: Pintura Estuco --> and replace its grid.

    new_block = '''<div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                    <div class="relative rounded-lg overflow-hidden group h-64 md:h-80 bg-brand-dark">
                        <img src="TRABAJOS/GENERAL/estuco/estuco1.jpg" alt="Pintura Estuco 1" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105 opacity-90 group-hover:opacity-100">
                    </div>
                    <div class="relative rounded-lg overflow-hidden group h-64 md:h-80 bg-brand-dark">
                        <img src="TRABAJOS/GENERAL/estuco/estuco2.jpg" alt="Pintura Estuco 2" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105 opacity-90 group-hover:opacity-100">
                    </div>
                    <div class="relative rounded-lg overflow-hidden group h-64 md:h-80 bg-brand-dark">
                        <img src="TRABAJOS/GENERAL/estuco/estuco3.jpg" alt="Pintura Estuco 3" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105 opacity-90 group-hover:opacity-100">
                    </div>
                </div>'''

    html = re.sub(r'<div class="grid grid-cols-1 md:grid-cols-2 gap-6">.*?estuco.*?</div>\s*</div>', new_block, html, flags=re.DOTALL)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)

update_estuco('index.html')
update_estuco('pro-services-dossier.html')
print("Estuco updated")
