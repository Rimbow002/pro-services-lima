import os

def insert_cocina(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    marker = '<!-- Proyecto 3: Gasfiter'
    
    new_block = '''<!-- Proyecto 8: Cocina -->
            <div class="mb-20">
                <div class="flex items-center mb-6">
                    <div class="w-12 h-12 rounded-full bg-brand-gold flex items-center justify-center mr-4">
                        <i class="fas fa-sink text-white text-xl"></i>
                    </div>
                    <div>
                        <h3 class="text-2xl font-bold">Trabajos Técnicos Generales</h3>
                        <p class="text-brand-gold text-sm font-semibold uppercase tracking-wide">Remodelación Completa de Cocina</p>
                    </div>
                </div>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div class="relative rounded-lg overflow-hidden group aspect-[4/3] bg-brand-dark">
                        <img src="TRABAJOS/GENERAL/cocina/cocina1.jpg" alt="Cocina 1" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105 opacity-90 group-hover:opacity-100">
                    </div>
                    <div class="relative rounded-lg overflow-hidden group aspect-[4/3] bg-brand-dark">
                        <img src="TRABAJOS/GENERAL/cocina/cocina2.jpg" alt="Cocina 2" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105 opacity-90 group-hover:opacity-100">
                    </div>
                    <div class="relative rounded-lg overflow-hidden group aspect-[4/3] bg-brand-dark">
                        <img src="TRABAJOS/GENERAL/cocina/cocina3.jpg" alt="Cocina 3" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105 opacity-90 group-hover:opacity-100">
                    </div>
                    <div class="relative rounded-lg overflow-hidden group aspect-[4/3] bg-brand-dark">
                        <img src="TRABAJOS/GENERAL/cocina/cocina_final.jpg" alt="Cocina Final" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105 opacity-90 group-hover:opacity-100">
                    </div>
                </div>
            </div>

            '''
    
    if 'Proyecto 8: Cocina' not in html:
        idx = html.find(marker)
        if idx != -1:
            html = html[:idx] + new_block + html[idx:]
        else:
            print(f"Marker not found in {filename}")

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)

insert_cocina('index.html')
insert_cocina('pro-services-dossier.html')
print("Cocina injected")
