import webbrowser

f = open('Beray.html', 'w')

#ol is for ordered lists
#ul is for unordered lists
#br is for line breaks(like new line)
#img src is for image that you want to open in web page
#alt is for name to photo, width is for width xd, heigth is for height xd, 

message = """<!DOCTYPE html>
<html lang = "en">
<head>
<title>This Is My Second Title</title>
</head>
<body>
<img src = "issizlikgecesi.png" alt = "Image of Us" style="width:25%"/>
<ol>
  <li>Item One</li>
  <li>Item Two</li>
  
</ol>   
<br>
<ul>
    <li>Item One</li>
    <li>Item Two</li>
</ul>   
</body>
</html>    

"""

f.write(message)
f.close()
webbrowser.open_new_tab('Beray.html')
