from flask import Flask,render_template,request
import sqlite3
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/contact', methods = ["GET","POST"])
def contactus():
    if request.method == "POST":
        fname = request.form.get("fullname")
        pno = request.form.get("phone")
        email = request.form.get("email")
        addr = request.form.get("address")
        msg = request.form.get("message")
        # print(fname,pno,email,addr,msg)
        conn = sqlite3.connect("ytdatabase.db")
        cur = conn.cursor()
        cur.execute(f'''
                    INSERT INTO CONTACT VALUES("{fname}","{pno}","{email}","{addr}","{msg}")    
                ''')
        conn.commit()
        return render_template('successfull.html')
    else:
        return render_template('contactus.html')
    # pass

@app.route('/likepredict')
def likepredict():
    return render_template('likepredict.html')

if __name__ == '__main__':
    app.run(port=1010)