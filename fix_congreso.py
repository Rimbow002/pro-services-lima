import re

def fix_congreso(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    new_block = '''<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
                    <div class="relative rounded-lg overflow-hidden group h-64 md:h-80 bg-brand-dark">
                        <img src="TRABAJOS/Destacados/congreso/DIPUTADO_1.jpg" alt="Congreso Foto 1" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105 opacity-90 group-hover:opacity-100">
                    </div>
                    <div class="relative rounded-lg overflow-hidden group h-64 md:h-80 bg-brand-dark">
                        <img src="TRABAJOS/Destacados/congreso/DIPUTADO_2.jpg" alt="Congreso Foto 2" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105 opacity-90 group-hover:opacity-100">
                    </div>
                    <div class="relative rounded-lg overflow-hidden group h-64 md:h-80 bg-brand-dark">
                        <img src="TRABAJOS/Destacados/congreso/congreso1.jpg" alt="Congreso Foto 3" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105 opacity-90 group-hover:opacity-100">
                    </div>
                    <div class="relative rounded-lg overflow-hidden group h-64 md:h-80 bg-brand-dark">
                        <img src="TRABAJOS/Destacados/congreso/congreso2.jpg" alt="Congreso Foto 4" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105 opacity-90 group-hover:opacity-100">
                    </div>
                </div>'''

    html = re.sub(r'<div class="grid grid-cols-1 md:grid-cols-3 gap-6">.*?DIPUTADO_3\.jpg.*?</div>\s*</div>', new_block, html, flags=re.DOTALL)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)

fix_congreso('index.html')
fix_congreso('pro-services-dossier.html')
print('Fixed!')
