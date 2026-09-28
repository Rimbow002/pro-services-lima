def update_logo(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    old = 'font-size="10.5" fill="#64748b" letter-spacing="3.5">MANTENIMIENTO INTEGRAL</text>'
    new = 'font-size="8.5" fill="#64748b" letter-spacing="1">MANTENIMIENTO Y SERVICIOS GENERALES</text>'

    html = html.replace(old, new)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)

update_logo('index.html')
update_logo('pro-services-dossier.html')
print("Updated logo")
