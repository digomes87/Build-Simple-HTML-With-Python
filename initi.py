import sys

script_tag = ""

filename = ""

name = len(sys.argv) > 1 and sys.argv[1] or None

x = len(sys.argv) > 2

if x:
 filename = sys.argv[2]
else:
 filename = 'index.html'

if name:
   script_tag = '<script type="text/javascript" src="%s"></script><script type="text/javascript">(function(){ alert("Ready to Go") })();</script>' % name

template = """<!DOCTYPE html">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html;charset=UTF-8" />
<title>PYTHON</title>
<style type="text/css">
.form-style-5{
    max-width: 800px;
    padding: 10px 20px;
    background: #f4f7f8;
    margin: 10px auto;
    padding: 20px;
    background: #f4f7f8;
    border-radius: 8px;
    font-family: Georgia, "Times New Roman", Times, serif;
}
.form-style-5 fieldset{
    border: none;
}
.form-style-5 legend {
    font-size: 1.4em;
    margin-bottom: 10px;
}
.form-style-5 label {
    display: block;
    margin-bottom: 8px;
}
.form-style-5 input[type="text"],
.form-style-5 input[type="date"],
.form-style-5 input[type="datetime"],
.form-style-5 input[type="email"],
.form-style-5 input[type="number"],
.form-style-5 input[type="search"],
.form-style-5 input[type="time"],
.form-style-5 input[type="url"],
.form-style-5 textarea,
.form-style-5 select {
    font-family: Georgia, "Times New Roman", Times, serif;
    background: rgba(255,255,255,.1);
    border: none;
    border-radius: 4px;
    font-size: 16px;
    margin: 0;
    outline: 0;
    padding: 7px;
    width: 100%;
    box-sizing: border-box;
    -webkit-box-sizing: border-box;
    -moz-box-sizing: border-box;
    background-color: #e8eeef;
    color:#8a97a0;
    -webkit-box-shadow: 0 1px 0 rgba(0,0,0,0.03) inset;
    box-shadow: 0 1px 0 rgba(0,0,0,0.03) inset;
    margin-bottom: 30px;

}
.form-style-5 input[type="text"]:focus,
.form-style-5 input[type="date"]:focus,
.form-style-5 input[type="datetime"]:focus,
.form-style-5 input[type="email"]:focus,
.form-style-5 input[type="number"]:focus,
.form-style-5 input[type="search"]:focus,
.form-style-5 input[type="time"]:focus,
.form-style-5 input[type="url"]:focus,
.form-style-5 textarea:focus,
.form-style-5 select:focus{
    background: #d2d9dd;
}
.form-style-5 select{
    -webkit-appearance: menulist-button;
    height:35px;
}
.form-style-5 .number {
    background: #1abc9c;
    color: #fff;
    height: 30px;
    width: 30px;
    display: inline-block;
    font-size: 0.8em;
    margin-right: 4px;
    line-height: 30px;
    text-align: center;
    text-shadow: 0 1px 0 rgba(255,255,255,0.2);
    border-radius: 15px 15px 15px 0px;
}

.form-style-5 input[type="submit"],
.form-style-5 input[type="button"]
{
    position: relative;
    display: block;
    padding: 19px 39px 18px 39px;
    color: #FFF;
    margin: 0 auto;
    background: #1abc9c;
    font-size: 18px;
    text-align: center;
    font-style: normal;
    width: 100%;
    border: 1px solid #16a085;
    border-width: 1px 1px 3px;
    margin-bottom: 10px;
}
.form-style-5 input[type="submit"]:hover,
.form-style-5 input[type="button"]:hover
{
    background: #109177;
}
</style>
</style>
%s
</head>
<body>
<div class="form-style-5">
<p>
	   	<h1>Pag Build With Python</h1>
	</p>
	<h3>
		<p>
			Python is the future !
		</p>
	</h>
		<div>
			<p>
				<h2>
					Here text about anyway,only a text about nothin speak about nothin.
					Sorry my criativite today stay in house sleep.
				</h2>
			</p>
			<p>
				Sera que chove hoje.
				Era uma vez dois gatinhos pretos que gostavam de chuva,um  se chama naue e o outra e o naua.
				Quando eles brigando eu falo Paranue !! Paranaua.

				<i>Piada boa !!!</i>
			</p>
		</div>

		<div>
			<p>
				<h1>
					<p>
						Here you have a form for send for administrator your opinion for this app in python.
						You Like this work ?
					</p>
				</h1>
			</p>
		</div>


            <form>
            <fieldset>
            <legend><span class="number">1</span> Candidate Info</legend>
            <input type="text" name="field1" placeholder="Your Name *">
            <input type="email" name="field2" placeholder="Your Email *">
            <textarea name="field3" placeholder="About yourself"></textarea>

            <legend><span class="number">2</span> Additional Info</legend>
            <textarea name="field3" placeholder="About Your School"></textarea>
            </fieldset>
            <input type="submit" value="Apply" />
            </form>
        </div>
</body>
</html>
""" % script_tag

#open the handler file
f = open(filename,'w')

#write to file
f.write(template)

#clone handle file
f.close()

#print screen
print template