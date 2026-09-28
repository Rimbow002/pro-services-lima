import re

def reorder_and_fix(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    # Define markers
    markers = {
        'p1': '<!-- Proyecto 1: Congreso -->',
        'p2': '<!-- Proyecto 2: Luren -->',
        'p3': '<!-- Proyecto 3: Gasfitería -->', # Wait, the powershell output showed Gasfitera. Let's use regex or partial string.
    }
    
    # Actually, we can use regex to split
    # Let's find the start of each project.
    
    def get_block(start_marker, end_marker):
        start = html.find(start_marker)
        if start == -1: return ""
        if end_marker:
            end = html.find(end_marker, start)
            if end == -1:
                return html[start:]
            return html[start:end]
        return html[start:]

    # Since I don't know the exact spelling due to encoding, let's match with re
    p1_match = re.search(r'<!-- Proyecto 1: Congreso -->', html)
    p2_match = re.search(r'<!-- Proyecto 2: Luren -->', html)
    p3_match = re.search(r'<!-- Proyecto 3: Gasfiter.*?a -->', html)
    p4_match = re.search(r'<!-- Proyecto 4: Muebles -->', html)
    p5_match = re.search(r'<!-- Proyecto 5: Pintura Estuco -->', html)
    p6_match = re.search(r'<!-- Proyecto 6: Drywall y Video -->', html)
    p7_match = re.search(r'<!-- Proyecto 7: Techos de Cristal -->', html)
    footer_match = re.search(r'<!-- Call to Action / Footer -->', html)
    
    # Extract blocks
    head_to_p1 = html[:p1_match.start()]
    b1 = html[p1_match.start():p2_match.start()]
    b2 = html[p2_match.start():p3_match.start()]
    b3 = html[p3_match.start():p4_match.start()]
    b4 = html[p4_match.start():p5_match.start()]
    b5 = html[p5_match.start():p6_match.start()]
    b6 = html[p6_match.start():p7_match.start()]
    b7 = html[p7_match.start():footer_match.start() - 15] # Back off to not cut off closing tags of section, wait actually I should just find the last </div></section>
    
    # Safest way to find end of b7 is to look for closing </section> before Footer.
    end_of_b7 = html.find('</section>', p7_match.start()) + 10
    b7 = html[p7_match.start():end_of_b7]
    rest_of_html = html[end_of_b7:]
    
    # Modify b6 (Drywall)
    # Current grid: <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
    # Change to: <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
    b6 = b6.replace('lg:grid-cols-4', '')
    
    # Currently b6 has: 2 images and 1 video (with lg:col-span-2). 
    # Remove lg:col-span-2 from video
    b6 = b6.replace('lg:col-span-2', '')
    
    # The end of the video div looks like:
    # <video src="TRABAJOS/GENERAL/drywall/video1.mp4" autoplay loop muted playsinline class="w-full h-full object-cover opacity-90"></video>
    # </div>
    
    # Append the second video div right after the first video div
    vid1_str = '<video src="TRABAJOS/GENERAL/drywall/video1.mp4" autoplay loop muted playsinline class="w-full h-full object-cover opacity-90"></video>\n                    </div>'
    
    vid2_div = '\n                    <div class="relative rounded-lg overflow-hidden group aspect-[4/3] bg-brand-dark">\n                        <video src="TRABAJOS/GENERAL/drywall/video2.mp4" autoplay loop muted playsinline class="w-full h-full object-cover opacity-90"></video>\n                    </div>'
    
    b6 = b6.replace(vid1_str, vid1_str + vid2_div)
    
    # Reassemble in new order: 1, 2, 6, 7, 3, 4, 5
    new_html = head_to_p1 + b1 + b2 + b6 + b7 + b3 + b4 + b5 + rest_of_html
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(new_html)

reorder_and_fix('index.html')
reorder_and_fix('pro-services-dossier.html')
print("Reordered and modified successfully!")
