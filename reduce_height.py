def reduce_video_height(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    # Replace the massive height in the drywall block with a more reasonable one
    html = html.replace('h-96 md:h-[36rem]', 'h-72 md:h-96')

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)

reduce_video_height('index.html')
reduce_video_height('pro-services-dossier.html')
print("Height reduced")
