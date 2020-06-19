import webbrowser

f = open('Finalproject.html', 'w')

message = """
<!DOCTYPE html>
<html lang = "en">
<head>
    <meta charset = "UTF-8">
    <title>Here Is My Final Project!</title>
</head>
<body>
    <h1>Beray Boztepe</h1>
    <nav>
        <a href = "http://www.google.com">One</a> 
        <a href = "http://www.github.com">Two</a> 
        <a href = "http://www.facebook.com">Three</a> 
        <a href = "http://www.youtube.com">MyFavOne</a>
    </nav>
    <section>
    <h2>Favorite Foods</h2>
    <ul>
        <li>Pizza</li>
        <li>Hamburger</li>
        <li>Salad</li>
        <li>French Fries</li>
    </ul>
    </section>
    <section>
    <h2>Achievements</h2>
    <p>Progress in this course (100%) <progress max="100" value="100">100%</progress></p>
    <p>Progress in the Specialization capstone (20%) <progress max="100" value="20">20%</progress></p>
    <p>Progress in life goals (33%) <progress max="100" value="33">33%</progress></p>
    </section>
    <section>
    <h2>More About Me</h2>
    <details>
        <summary>My Childhood</summary>
        <p>I was born in Aydin, Turkey. My only wish was playing football with my friends.</p>
    </details>
    </section>
    <footer>
        <a href="http://www.intro-webdesign.com."> 
            <img src = "http://www.intro-webdesign.com/images/newlogo.png"
                alt = "Web Design For Everybody Logo"/></a>
                    This page was created by Beray Boztepe &amp; Colleen van Lent. To learn more about web design, please visit
                        <a href="http://www.intro-webdesign.com.">Intro to Web Design.</a>
    </footer>
</body>
</html>

"""

f.write(message)
f.close()
webbrowser.open_new_tab('Finalproject.html')