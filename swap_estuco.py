def swap_estuco(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    # We will just temporarily rename estuco1 to estuco_TEMP, estuco2 to estuco1, and estuco_TEMP to estuco2
    # But since it's only two specific occurrences in the whole file, we can do block replacement

    old_block = '''<div class="relative rounded-lg overflow-hidden group h-64 md:h-80 bg-brand-dark">
                        <img src="TRABAJOS/GENERAL/estuco/estuco1.jpg" alt="Pintura Estuco 1" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105 opacity-90 group-hover:opacity-100">
                    </div>
                    <div class="relative rounded-lg overflow-hidden group h-64 md:h-80 bg-brand-dark">
                        <img src="TRABAJOS/GENERAL/estuco/estuco2.jpg" alt="Pintura Estuco 2" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105 opacity-90 group-hover:opacity-100">
                    </div>'''

    new_block = '''<div class="relative rounded-lg overflow-hidden group h-64 md:h-80 bg-brand-dark">
                        <img src="TRABAJOS/GENERAL/estuco/estuco2.jpg" alt="Pintura Estuco 2" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105 opacity-90 group-hover:opacity-100">
                    </div>
                    <div class="relative rounded-lg overflow-hidden group h-64 md:h-80 bg-brand-dark">
                        <img src="TRABAJOS/GENERAL/estuco/estuco1.jpg" alt="Pintura Estuco 1" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105 opacity-90 group-hover:opacity-100">
                    </div>'''

    html = html.replace(old_block, new_block)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)

swap_estuco('index.html')
swap_estuco('pro-services-dossier.html')
print("Swapped estuco images")
