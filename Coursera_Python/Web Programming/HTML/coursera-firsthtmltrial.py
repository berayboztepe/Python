import webbrowser

f = open('Helloworld.html', 'w')

#h1 is the first prg
#h2 is the second prg
#a href is for URLs
#blink is for blinking the things that is written there
#marquee is for scrolling the writing
#center is for centering the writing

message = """<!DOCTYPE html>
<html lang = "tr">

<head> 
    <title>This Is My Very First Time</title>
    <meta charset = "UTF-8">
</head>
<body>
    <div style="text-align: center;">
    <h1>This is My First Paragraph</h1>
    <h2>This is My Second Paragraph</h2>
    <a href = "http://www.google.com">Wanna go there?</a>
    </div>   
</body>

</html>"""

f.write(message)
f.close()
webbrowser.open_new_tab('Helloworld.html')
