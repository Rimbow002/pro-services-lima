import os

def make_b2c_friendly(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    # Replacements
    replacements = [
        ("para su Empresa.", 
         "para su Empresa y Hogar."),
        ("Centralizamos todas sus necesidades de mantenimiento corporativo, reparación e infraestructura en un proveedor de confianza.", 
         "Centralizamos todas sus necesidades de mantenimiento corporativo y residencial. Reparación, remodelación e infraestructura con un proveedor de confianza."),
        ("Un Aliado Estratégico a su Medida", 
         "El Aliado Ideal para su Empresa y Hogar"),
        ("mantenimiento óptimo de sus instalaciones no es solo un gasto, sino una inversión directa en la productividad y la imagen de su corporación.", 
         "mantenimiento óptimo de sus espacios no es solo un gasto, sino una inversión directa en la productividad de su empresa y el confort de su hogar."),
        ("Nos diferenciamos por ofrecer un servicio integral. Ya no necesita coordinar con múltiples proveedores", 
         "Tanto para grandes proyectos comerciales como para remodelaciones residenciales, nos diferenciamos por ofrecer un servicio 100% integral. Ya no necesita coordinar con múltiples proveedores"),
        ("Optimice hoy el mantenimiento de su empresa", 
         "Renueve su hogar u optimice su empresa hoy"),
        ("Contacte con nuestro equipo técnico para una visita de evaluación o solicite nuestra presentación comercial.", 
         "Contacte con nuestro equipo técnico para una visita de evaluación, cotización de remodelación o agendar una cita.")
    ]

    for old, new in replacements:
        html = html.replace(old, new)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)

make_b2c_friendly('index.html')
make_b2c_friendly('pro-services-dossier.html')
print("Text updated to include B2C")
