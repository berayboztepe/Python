import webbrowser

f = open('index.html', 'w')


message = """
<!DOCTYPE html>
<html lang = "en">
<head>
    <meta charset = "UTF-8">
    <title>My First Page!</title>
</head>
<body>
    <main><p>This Is My Main Code!</p></main>
    <footer><p>Think of a more interesting footer</p></footer>     
</body>
</html>

"""

f.write(message)
f.close()
webbrowser.open_new_tab('index.html')