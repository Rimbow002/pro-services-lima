import os

def update_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update Infraestructura
    content = content.replace(
        '<span>Pintura premium (interiores/exteriores).</span>',
        '<span>Empaste y pintura de paredes y techos.</span></li>\n                        <li class="flex items-start"><i class="fas fa-check text-brand-gold mt-1 mr-3 text-sm"></i> <span>Instalación de techos bloques de vidrios.</span></li>\n                        <li class="flex items-start"><i class="fas fa-check text-brand-gold mt-1 mr-3 text-sm"></i> <span>Instalación de mesadas de piedra.</span>'
    )

    # 2. Update Tecnicas
    content = content.replace(
        '<span>Electricidad comercial e industrial.</span>',
        '<span>Electricidad comercial e industrial y cableado general.</span></li>\n                        <li class="flex items-start"><i class="fas fa-check text-brand-gold mt-1 mr-3 text-sm"></i> <span>Luminarias: Instalación/desinstalación, cambio de alambrillo, corrida y anclajes.</span>'
    )

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

update_file('index.html')
update_file('pro-services-dossier.html')
print("Done")
