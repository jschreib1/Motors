#!/usr/bin/cgipython1

import cgi
import cgitb
cgitb.enable()

form = cgi.FieldStorage()
letter = form.getvalue("option")

with open('index.txt', 'w') as f:
 f.write(str(letter))


print('Content-type:text/html\n\n')

print('''
<html>
<style>
body {
background-image: url("https://www.kinsa.com/wp-content/uploads/2013/10/In-the-Driver-Seat.jpg");
background-repeat: no-repeat;
background-attachment: fixed;
background-size: cover;
}

input {
text-align:center;
border-radius:10px;
margin-left:40px;
}
</style>

<body>
<h1 style="text-align:center;">Remote Control Car Webpage</h1><br><br>


<h2 style="margin-left:30px;"> <b>Direction</b></h2>

<form action="/cgi-bin/index.py" method="POST">
<input type="radio" name="option" value="F"> Forward<br>
<input type="radio" name="option" value="L"> Left<br>
<input type="radio" name="option" value="R"> Right<br><br>
<input type="submit" value="Submit"> <br><br>
</form>

</body>
</html>

''')