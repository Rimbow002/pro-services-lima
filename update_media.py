import os

def update_html(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # 1. Add "planos" to Infraestructura
    old_planos = '<span>Diseño e instalación de Drywall.</span></li>'
    new_planos = '<span>Diseño e instalación de Drywall.</span></li>\n                        <li class="flex items-start"><i class="fas fa-check text-brand-gold mt-1 mr-3 text-sm"></i> <span>Elaboración y diseño de planos arquitectónicos.</span></li>'
    if new_planos not in html:
        html = html.replace(old_planos, new_planos)

    # 2. Add Drywall and Techo de cristal blocks
    # I'll find the last portfolio block: Pintura Estuco, and append after it.
    
    old_estuco = 'alt="Pintura Estuco 2" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105 opacity-90 group-hover:opacity-100">\n                    </div>\n                </div>\n            </div>'
    
    new_blocks = '''alt="Pintura Estuco 2" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105 opacity-90 group-hover:opacity-100">
                    </div>
                </div>
            </div>

            <!-- Proyecto 6: Drywall y Video -->
            <div class="mt-20">
                <div class="flex items-center mb-6">
                    <div class="w-12 h-12 rounded-full bg-brand-gold flex items-center justify-center mr-4">
                        <i class="fas fa-hammer text-white text-xl"></i>
                    </div>
                    <div>
                        <h3 class="text-2xl font-bold">Trabajos Técnicos Generales</h3>
                        <p class="text-brand-gold text-sm font-semibold uppercase tracking-wide">Estructuras y Acabados en Drywall</p>
                    </div>
                </div>
                <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
                    <div class="relative rounded-lg overflow-hidden group aspect-[4/3] bg-brand-dark">
                        <img src="TRABAJOS/GENERAL/drywall/drywall1.jpg" alt="Drywall 1" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105 opacity-90 group-hover:opacity-100">
                    </div>
                    <div class="relative rounded-lg overflow-hidden group aspect-[4/3] bg-brand-dark">
                        <img src="TRABAJOS/GENERAL/drywall/drywall2.jpg" alt="Drywall 2" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105 opacity-90 group-hover:opacity-100">
                    </div>
                    <div class="relative rounded-lg overflow-hidden group aspect-[4/3] bg-brand-dark lg:col-span-2">
                        <video src="TRABAJOS/GENERAL/drywall/video1.mp4" autoplay loop muted playsinline class="w-full h-full object-cover opacity-90"></video>
                    </div>
                </div>
            </div>

            <!-- Proyecto 7: Techos de Cristal -->
            <div class="mt-20">
                <div class="flex items-center mb-6">
                    <div class="w-12 h-12 rounded-full bg-brand-gold flex items-center justify-center mr-4">
                        <i class="fas fa-border-all text-white text-xl"></i>
                    </div>
                    <div>
                        <h3 class="text-2xl font-bold">Trabajos Técnicos Generales</h3>
                        <p class="text-brand-gold text-sm font-semibold uppercase tracking-wide">Instalación de Techos de Cristal / Vidrio</p>
                    </div>
                </div>
                <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                    <div class="relative rounded-lg overflow-hidden group aspect-[4/3] bg-brand-dark">
                        <img src="TRABAJOS/GENERAL/techo_cristal/techo1.jpg" alt="Techo Cristal 1" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105 opacity-90 group-hover:opacity-100">
                    </div>
                    <div class="relative rounded-lg overflow-hidden group aspect-[4/3] bg-brand-dark">
                        <img src="TRABAJOS/GENERAL/techo_cristal/techo2.jpg" alt="Techo Cristal 2" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105 opacity-90 group-hover:opacity-100">
                    </div>
                    <div class="relative rounded-lg overflow-hidden group aspect-[4/3] bg-brand-dark">
                        <img src="TRABAJOS/GENERAL/techo_cristal/techo3.jpg" alt="Techo Cristal 3" class="w-full h-full object-cover transition-transform duration-700 group-hover:scale-105 opacity-90 group-hover:opacity-100">
                    </div>
                </div>
            </div>'''
            
    if "Proyecto 6: Drywall" not in html:
        html = html.replace(old_estuco, new_blocks)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)

update_html('index.html')
update_html('pro-services-dossier.html')
print("Media injected")
