def fix_video(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    html = html.replace('src="TRABAJOS/GENERAL/drywall/video1.mp4"', 'src="TRABAJOS/GENERAL/drywall/video1.mp4#t=15"')

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)

fix_video('index.html')
fix_video('pro-services-dossier.html')
print("Video fixed")
