# Send an email with Python

The [Send_Email_Example.py](https://github.com/Alejandro-ZZ/Automation-with-Python/blob/master/send-email/Send_Email_Example.py) code is divide in three sections: 

* [EMAIL LIBRARY](#email-library)
* [ADDING ATTACHMENTS](#adding-attachments)
* [SENDING EMAIL THROUGH SMTP SERVER](#sending-email-through-smtp-server) 

Running the script will show you (in the console) what action is being performed with a `print` function.

## EMAIL LIBRARY

In this section the [email.message.EmailMessage](https://docs.python.org/3/library/email.message.html#email.message.EmailMessage) class is used to create the text 
structures for the email we will send. There'll print a message on the screen every time a field of the email structure is modified, ex: 
when adding **`From`**, **`To`**, **`Subject`** and other fields. 

Note that the list of recipients includes the sender email address, so if everything goes well at the end of the code, you'll receive a copy of the email sent. On the
other hand, after setting a body to the email, the **`set_content()`** method also automatically added **`Content-Type`** and **`Content-Transfer-Encoding`** headers. 
Those are used to tell email clients and servers how to interpret the bytes in this email message into a string.

## ADDING ATTACHMENTS

This section attachs a png file (named *example.png*) to the email structure. This action is taken with the **`add_attachment()`** wich also takes as a parameter the 
**maintype** and **subtype** of the file; that is needed because whatever type the attachment happens to be, it'll be encoded as some form of text. So the **Multipurpose 
Internet Mail Extensions (MIME)** standard is used to encode all sorts of files as text strings that can be sent via email. 

In case that you know the correct type and subtype of the files you’ll be sending, you can use those values directly in the **`add_attachment()`** methof. But, if you 
don't know, you can use the Python **mimetypes** module to make a guess. That's why the **maintype** and **subtype** parameters are taken from the 
**`mimetypes.guess_type()`** method. In this example the **maintype** of the file is *image* and the **subtype** is *png*.

## SENDING EMAIL THROUGH SMTP SERVER

In this section the [smtplib](https://docs.python.org/3/library/smtplib.html) module is used to create the **Simple Mail Transfer Protocol (SMTP)** to send the email.
Firts, the code tries to connect to your *localhost* server; however it'll raise an error because the conection won't be succesfully (unless you have a local SMTP 
server configured). 

If the before connection wasn't successfully, the code will try to connect to a Gmail SMTP server. When doing that, program will wait you to enter wether you want to 
enable or not the debug option of the **`smtplib`** library. Then, the **`getpass`** module is imported to ask for the password without showing it in the screen. 


 **Note:** 
 
 * if you run the program in a python IDLE, when asking for your password it wil trough a warnning because the **`getpass`** module wasn't meant to excecute in a IDLE. 
   And so, you'll see your password on the shell.
 
 * When trying to authenticate, it might raise a fail connection (like the one shown below) even tough your password is OK. This might be because you have the 
   **Allow less secure apps access** option disable on your Gmail account settings. 
 ~~~
        smtplib.SMTPAuthenticationError: (535, b'5.7.8 Username and Password not accepted. Learn more at
        5.7.8  https://support.google.com/mail/?p=BadCredentials 11sm1527779vkz.42 - gsmtp')
 ~~~
