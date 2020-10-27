import smtplib
from email.message import EmailMessage

#===========================================================
#||                                                       ||
#||                 EMAIL LIBRARY                         ||
#||                                                       ||
#===========================================================
def create_email_structure():
    
    message = EmailMessage()

    print("Creating EmailMessage object...")
    #Should shows nothing
    print("Printing message object...\n")
    print(message)
    print("---------------------------------------" + "\n")

    print("Creating the From and To fields...")

    sender = SENDER_ADDRESS
    recipients =  RECIPIENT_ADDRESSES
    #Add the sender and recipient to the From and To fields
    message['From'] = sender
    message['To'] = ", ".join(recipients)

    print("Printing message object...\n")
    print(message)
    print("--------------------------------------------------------" + "\n")


    print("Creating a subject...")

    message['Subject'] = 'Greetings from {} to {}!'.format(sender, recipients)

    print("Printing message object...\n")
    print(message)
    print("--------------------------------------------------------" + "\n")


    print("Creating a body...")

    body = """Hey there!

    I'm learning to send emails using Python!"""
    message.set_content(body)


    print("Printing message object...\n")
    print(message)
    print("--------------------------------------------------------" + "\n")
    return message

#===========================================================
#||                                                       ||
#||                 ADDING ATTACHMENTS                    ||
#||                                                       ||
#===========================================================
def attach_file(message):
    #The label MIME type and subtype are used to know what type of
    #attachment are we sending. If you don't know the correct types, you
    #can use the module mimetypes to help.
    print("Guessing the type of an example file to attach...")

    import os

    attachment_path = os.path.join(os.getcwd(),"example.png")
    print("Looking for file in path: " + attachment_path +"...")

    attachment_filename = os.path.basename(attachment_path)
    print("File name: " + attachment_filename)

    import mimetypes
    mime_types, _ = mimetypes.guess_type(attachment_path)
    print("Printing the mime type and subtype guessed...")
    mime_type, mime_subtype = mime_types.split('/', 1)
    print("MIME type: " + mime_type)
    print("MIME subtype: " + mime_subtype + "\n")
    print("--------------------------------------------------------" + "\n")

    print("Attaching the example file...")
    with open(attachment_path, 'rb') as ap:
        message.add_attachment( ap.read(),
                                maintype=mime_type,
                                subtype=mime_subtype,
                                filename=os.path.basename(attachment_path)
                              )

    print("Printing message object...\n")
    print(message)
    print("--------------------------------------------------------" + "\n")

    return message
#===========================================================
#||                                                       ||
#||         SENDING EMAIL THROUGH SMTP SERVER             ||
#||                                                       ||
#===========================================================

def local_SMTP_connection(message):
    #To connect to a SMTP server we can use two classes of smtplib:
    #       The SMTP class will make a direct SMTP connection
    #       The SMTP_SSL class will make a SMTP connection over SSL/TLS.

    print("Trying to make direct SMTP connection to the local machine...")

    try:
        #You could get an error and that might be because there's no local
        #SMTP server configured
        mail_server = smtplib.SMTP('localhost')
        
        #emails_not_sent is a dictionary of any recipients that weren’t
        #able to receive the message.
        emails_not_sent = mail_server.send_message(message)
                
        print("The following emails weren’t able to receive the message: ")
        print(emails_not_sent)

        print("Closing the connection to the mail server...")
        mail_server.quit()

        return True
        
    except Exception as e:
        print("Oops! Something was wrong...\n")
        print("Exception: ")
        print(e,"\n")

        return False

    print("--------------------------------------------------------" + "\n")

def gmail_SMPT_connection(message, sender, recipients):
    
    #Let's connect to the SMTP server for your personal email address
    #in this case we are using Gmail account.

    print("Connecting over SSL/TLS to SMTP Gmail server...")
    mail_server = smtplib.SMTP_SSL('smtp.gmail.com')

    #To see the SMTP messages that are being sent back and forth by the smtplib
    #module behind the scenes, you can use set_debuglevel(1).
    debug = input('Would you like to enable debug messages from smtlib? [Y/n]')

    if debug.lower() == 'y':
        print("Activating debug options to SMTP lib...")
        mail_server.set_debuglevel(1)
        print("--------------------------------------------------------" + "\n")

    print("Asking for the password of email: " + sender)
    import getpass
    mail_pass = getpass.getpass('Password: ')

    #===========================================================
    #|| IMPORTANT NOTE FOR SMTP GMAIL SERVERS:                ||
    #||                                                       ||
    #||     If there's an error while authenticating (and you ||
    #||     are sure your password is ok) you have to go to   ||
    #||     "Less secure app access" and set "Allow less      ||
    #||     secure apps access" to YES                        ||
    #===========================================================

    print("Authenticating to the email server...")

    try:
        mail_server.login(sender, mail_pass)

        print("Sending message to ", recipients,"...")
        
        #emails_not_sent is a dictionary of any recipients that weren’t
        #able to receive the message.
        emails_not_sent = mail_server.send_message(message)
        
        print("The following emails weren’t able to receive the message: ")
        print(emails_not_sent)

    except Exception as e:
        print("Oops! Something was wrong...\n")
        print("Exception: ")
        print(e, "\n")

    print("Closing the connection to the mail server...")
    mail_server.quit()

def main():

    message = create_email_structure()
    message = attach_file(message)
    
    success = local_SMTP_connection(message)

    if not success:
        gmail_SMPT_connection(message, SENDER_ADDRESS, RECIPIENT_ADDRESSES)

    
#===========================================================
#||                                                       ||
#||                      EXECUTING CODE                  ||
#||                                                       ||
#===========================================================
SENDER_ADDRESS = "my@gmail.com"
RECIPIENT_ADDRESSES =  ['person_1@example.com', 'person_2@example.com', SENDER_ADDRESS]
main()
