from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')  # default URL
def student():
   return render_template('input_info.html')

@app.route('/result', methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = dict()
      result['Name'] = request.form.get('Name')
      result['Student Number'] = request.form.get('Student Number')
      result['Gender'] = request.form.get('Gender')
      return render_template("result.html",result = result)

# if __name__ == '__main__':
#   app.run()

if __name__ == '__main__':
   app.run(debug=True, host='0.0.0.0', port=5000)