from flask import Flask,redirect,render_template,request

app=Flask(__name__)

#data=dict()
data_list=[]

@app.route('/',methods=['GET'])
def student():
    return render_template('input.html')

@app.route('/result', methods=['POST','GET'])
def result():
    if request.method =='POST':
        result=dict()
        result['Name']=request.form.get('name')
        result['Student Number']=request.form.get('StudentNumber')
        result['Gender']=request.form.get('gender')
        result['Major']=request.form.get('major')

        lst=['Python','Java','HTML','C++']

        lst2=[]

        for x in lst:
            if request.form.get(x):
                lst2.append(x)
        programming=','.join(lst2)
        result['Programming Languages']=programming

        return render_template('result.html', result=result)

# if __name__ =='__main__':
#    app.run(debug=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

# 만약?
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)