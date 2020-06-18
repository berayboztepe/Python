import webbrowser

f = open('Helloworld.html', 'w')

#h1 is the first prg
#h2 is the second prg
#a href is for URLs
#blink is for blinking the things that is written there
#marquee is for scrolling the font
#center is for centering the fonts

message = """<html lang = "en">
<head></head>
<meta charset = "UTF-8">
<body>
<center>
<h1>This is My First Paragraph</h1>
<h2>This is My Second Paragraph</h2>
<blink>Click This--></blink>
<a href = "http://www.google.com">Wanna go there?</a>
<marquee>OR YOU AFRAID OF CLICKING LOL!</marquee>
</center>
</body>
</html>"""

f.write(message)
f.close()
webbrowser.open_new_tab('Helloworld.html')
