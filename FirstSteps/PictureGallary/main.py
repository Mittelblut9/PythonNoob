import os

filnames = []

for (root,dirs,files) in os.walk('./FirstSteps/PictureGallary/images', topdown=True):
        filnames = files

print(filnames)


html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Picture Gallary</title>
    </head>
    <body>
        <h1>Picture Gallary</h1>
        """
for f in filnames:
    html += f"""
        <img src="images/{f}" alt="{f}" style="width: 300px">
    """

html += """
        
    </body>
"""

try:
    os.remove('./FirstSteps/PictureGallary/index.html')
finally:
    with open('./FirstSteps/PictureGallary/index.html', 'w') as f:
        f.write(html)