from flask import Flask, render_template


app= Flask(__name__)


@app.route('/')
def indec():
    # return'<h3>Welcome to Mars. Updated</h3>'
    return render_template('index.html')

@app.route('/hemispheres')
def hemispheres():
    # return render_template('hemisphere.html')
    return render_template('hemispheres.html')

   
if __name__=='__main__':
    app.run(debug=True)