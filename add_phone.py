import re

def add_phone_number(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Add number text
    old_text = '<p class="text-xl font-bold text-white">+51 997 360 521</p>'
    new_text = '<p class="text-xl font-bold text-white">+51 997 360 521</p>\n                                  <p class="text-xl font-bold text-white">+51 907 532 812</p>'
    
    html = html.replace(old_text, new_text)

    # 2. Add second WhatsApp button
    new_button_block = '''<div class="flex flex-col space-y-4 w-full">
                            <a href="https://wa.me/51997360521?text=Hola%20Pro%20Service,%20me%20gustaría%20solicitar%20información%20sobre%20sus%20servicios." target="_blank" class="block w-full py-3 px-6 bg-green-500 hover:bg-green-600 text-white text-center text-lg font-bold rounded-lg shadow-lg hover:shadow-green-500/50 transition-all duration-300 transform hover:-translate-y-1">
                                WhatsApp (Línea 1)
                            </a>
                            <a href="https://wa.me/51907532812?text=Hola%20Pro%20Service,%20me%20gustaría%20solicitar%20información%20sobre%20sus%20servicios." target="_blank" class="block w-full py-3 px-6 bg-green-500 hover:bg-green-600 text-white text-center text-lg font-bold rounded-lg shadow-lg hover:shadow-green-500/50 transition-all duration-300 transform hover:-translate-y-1">
                                WhatsApp (Línea 2)
                            </a>
                        </div>'''

    html = re.sub(r'<a href="https://wa\.me/51997360521.*?Contactar por WhatsApp\s*</a>', new_button_block, html, flags=re.DOTALL)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)

add_phone_number('index.html')
add_phone_number('pro-services-dossier.html')
print("Phone number added cleanly")
