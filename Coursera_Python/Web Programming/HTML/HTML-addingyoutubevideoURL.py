import webbrowser

f = open('../index1.html', 'w')

message = """
<!DOCTYPE html>
<html lang = "en">
<head>
    <meta charset = "UTF-8">
    <title>Let's Try Smt.</title>
</head>
<body>
    <h1>VIDEO!</h1>
    <iframe  width = "400" src = "https://www.youtube.com/watch?v=AnUTAG15_4Q&list=RDAnUTAG15_4Q&start_radio=1">
    </iframe>
    <br>
</body>
</html>

"""

f.write(message)
f.close()
webbrowser.open_new_tab('index1.html')