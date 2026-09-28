def update_drywall_height(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    # Extract the drywall block
    start_idx = html.find('<!-- Proyecto 6: Drywall y Video -->')
    end_idx = html.find('<!-- Proyecto 7: Techos de Cristal -->')

    if start_idx != -1 and end_idx != -1:
        drywall_block = html[start_idx:end_idx]
        # Replace height in drywall block
        new_drywall_block = drywall_block.replace('h-64 md:h-80', 'aspect-[4/5] md:aspect-square')
        
        # Or let's use fixed heights so it matches the aesthetic but is taller
        new_drywall_block = drywall_block.replace('h-64 md:h-80', 'h-96 md:h-[36rem]')

        html = html[:start_idx] + new_drywall_block + html[end_idx:]

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)

update_drywall_height('index.html')
update_drywall_height('pro-services-dossier.html')
print("Drywall height updated")
