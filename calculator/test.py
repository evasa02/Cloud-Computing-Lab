import webapp2

html_form="""
<!DOCTYPE html>
<html>
<head>
    <title>Calculator</title>
</head>
<body>
    <h1>Calculator</h1>
    <form action="/" method="post" id="f1">
        <label>Number 1 :</label>
        <input type="number" id="num1" name="num1" required></br>
        <label>Number 2 :</label>
        <input type="number" id="num2" name="num2" required></br>
        <label>Operation :</label>
        <select id="op" name="op">
            <option value="add">+</option>
            <option value="sub">-</option>
            <option value="mul">*</option>
            <option value="div">/</option>
        </select></br>
    </form>
    <button type="submit" form="f1">Calculate</button>
</body>
</html>
"""

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.write(html_form)
    
    def post(self):
        try:    
            num1 = float(self.request.get('num1'))
            num2 = float(self.request.get('num2'))
            operation = self.request.get('op')

            if operation == "add":
                result = num1 + num2 
            elif operation == "sub":
                result = num1 - num2
            elif operation == "mul":
                result = num1 * num2
            elif operation =="div":
                if num2 != 0: 
                    result = num1 / num2
                else:
                    result = "Error! Division by zero error"
            else:
                result = "Invalid Input !!!"
            self.response.write(html_form)
            self.response.write("<h2>Result : {}</h2>".format(result))
        except ValueError:
            self.response.write(html_form)
            self.response.write("<h2>Invalid Input !!! </h2>")

app = webapp2.WSGIApplication([('/',MainPage)],debug=True)
