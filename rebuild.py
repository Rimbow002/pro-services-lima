import re

def rebuild_html(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    # Find the start of portafolio section
    start_sec = html.find('<section id="portafolio"')
    end_sec = html.find('<!-- Call to Action / Footer -->')

    if start_sec == -1 or end_sec == -1: return

    head = html[:start_sec]
    tail = html[end_sec:]

    # The portafolio header
    header = '''<section id="portafolio" class="py-24 bg-brand-blue text-white">
        <div class="container mx-auto px-6">
            <div class="flex flex-col md:flex-row justify-between items-end mb-16">
                <div>
                    <span class="text-brand-gold font-bold tracking-widest text-sm uppercase">Experiencia Comprobada</span>
                    <h2 class="text-3xl md:text-5xl font-extrabold mt-2">Casos de Éxito</h2>
                </div>
                <p class="text-gray-300 md:text-right mt-4 md:mt-0 max-w-sm">Nuestro nivel de detalle, documentado en nuestros proyectos más exigentes.</p>
            </div>'''

    # Extract inner content blocks using regex
    # Each block starts with <!-- Proyecto X: ... --> and ends right before the next <!-- Proyecto X: ... --> or the end of the section.
    
    # We will just parse the whole HTML for project blocks
    projects = {}
    patterns = [
        ('p1', r'<!-- Proyecto 1: Congreso -->'),
        ('p2', r'<!-- Proyecto 2: Luren -->'),
        ('p6', r'<!-- Proyecto 6: Drywall y Video -->'),
        ('p7', r'<!-- Proyecto 7: Techos de Cristal -->'),
        ('p8', r'<!-- Proyecto 8: Cocina -->'),
        ('p3', r'<!-- Proyecto 3: Gasfiter.*? -->'),
        ('p4', r'<!-- Proyecto 4: Muebles -->'),
        ('p5', r'<!-- Proyecto 5: Pintura Estuco -->')
    ]

    for key, pat in patterns:
        match = re.search(pat, html)
        if match:
            projects[key] = match.start()

    # Sort to find boundaries
    sorted_projects = sorted([(k, v) for k, v in projects.items()], key=lambda x: x[1])
    
    blocks = {}
    for i, (k, start_idx) in enumerate(sorted_projects):
        if i < len(sorted_projects) - 1:
            end_idx = sorted_projects[i+1][1]
        else:
            end_idx = end_sec
        
        block = html[start_idx:end_idx]
        
        # Clean up dangling divs and unclosed divs in the block.
        # It's safer to just extract the actual content.
        # But wait, fixing unbalanced divs via regex is hard.
        # Let's count divs and fix them!
        blocks[k] = block

    # Let's manually fix p1 which is broken.
    # We know p1 is Congreso.
    p1 = blocks['p1']
    # p1 is missing a closing </div> at the end because my regex swallowed it.
    if p1.count('<div') > p1.count('</div'):
        p1 += '\n</div>\n'
    blocks['p1'] = p1

    # p7 was right before the container closed early. It might have too many </div>.
    # Actually, the early close was because of `reorder.py` leaving `</div></section>` attached to p7.
    p7 = blocks['p7']
    p7 = re.sub(r'</section>', '', p7)
    p7 = re.sub(r'</div>\s*$', '</div>\n', p7) # Make sure it doesn't close the container
    blocks['p7'] = p7

    # Ensure all blocks are properly balanced
    for k in blocks:
        b = blocks[k]
        open_divs = len(re.findall(r'<div\b[^>]*>', b))
        close_divs = len(re.findall(r'</div>', b))
        if open_divs > close_divs:
            b += '\n</div>' * (open_divs - close_divs)
        elif close_divs > open_divs:
            # Too many closing divs! Remove them from the end.
            for _ in range(close_divs - open_divs):
                b = re.sub(r'</div>\s*$', '', b)
        blocks[k] = b

    # Assemble in correct order
    # order: p1, p2, p6, p7, p8, p3, p4, p5
    ordered_keys = ['p1', 'p2', 'p6', 'p7', 'p8', 'p3', 'p4', 'p5']
    assembled_projects = '\n\n'.join([blocks[k] for k in ordered_keys if k in blocks])

    final_html = head + header + '\n\n' + assembled_projects + '\n        </div>\n    </section>\n\n    ' + tail

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(final_html)

rebuild_html('index.html')
rebuild_html('pro-services-dossier.html')
print("Rebuilt structure")
