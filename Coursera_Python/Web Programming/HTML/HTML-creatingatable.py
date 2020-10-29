import webbrowser

f = open('index1.html', 'w')
#tr for rows
#th is for heading of rows
#border is for borders of table
#rowspan means = 2(or more, or less. u choose) rows of space
message = """
<!DOCTYPE html>
<html lang = "en">
<head>
    <meta charset = "UTF-8">
    <title>This Is My Table</title>
</head>
<body>
    <table>
        <tr><th>First</th><th>Second</th><th>Third</th></tr>
        <tr><td>One</td><td>Two</td><td>Three</td></tr>
        <tr><td>Four</td><td>Five</td><td>Six</td></tr>
        <tr><td>Seven</td><td>Eight</td><td>Nine</td></tr>
    </table>
    <center>
        <table border = "20">
            <tr>
                <th>Child's Name: </th><th>Parent's Name: </th>
            </tr>
            <tr>
                <td rowspan="2">Catherine</td><td>Michael Mccartney</td>
            </tr>
            <tr>
                <td>Barbara Mccartney</td>
            </tr>
            <tr>
                <td>Maggie</td><td>Sheila Brolia</td>
            </tr>
            <tr>
                <td rowspan="2">Edward</td><td>Jeff Thalindo</td>
            </tr>
            <tr>
                <td>Kristie Thalindo</td>
            </tr>
        </table>
    </center>
</body>
</html>

"""

f.write(message)
f.close()
webbrowser.open_new_tab('index1.html')