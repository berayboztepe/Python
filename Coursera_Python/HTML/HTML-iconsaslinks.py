import webbrowser

f = open('../index.html', 'w')

#i tag is for icon
#link tag is for icon link, the link has a special key for everyone 
#fa-5x is for x5 the size of the icon!
message = """
<!DOCTYPE html>
<html lang = "en">
<head>
    <meta charset = "UTF-8">
    <title>Font Awesome!</title>
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.10.0/css/all.css" 
    integrity="sha384-AYmEC3Yw5cVb3ZcuHtOA93w35dYTsvhLPVnYs9eStHfGJvOvKxVfELGroGkvsg+p" crossorigin="anonymous"/>
</head>
<body>
    <a href = "https://www.google.com/"><i class="fab fa-google fa-5x"></i></a>
</body>
</html>

"""

f.write(message)
f.close()
webbrowser.open_new_tab('index.html')