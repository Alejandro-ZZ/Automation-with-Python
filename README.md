# Automation-with-Python

This repository shows examples of how to automate different actions with python. Each project was developed based in some exercises seen in the professional certificate of google: [Google IT Automation with Python](https://www.coursera.org/professional-certificates/google-it-automation)

## Examples

* **[send-email](https://github.com/Alejandro-ZZ/Automation-with-Python/tree/master/send-email)**, script that describes how to send an email message with an attachment from Python using libraries like `email.message`, `smtplib` and others.

* **[regex_examples](https://github.com/Alejandro-ZZ/Automation-with-Python/tree/master/regex_examples)**, basic and advanced examples applying regular expressions with the `re` module and three of its methods: `re.search()`, `re.findall()`, `re.sub()`

* **[generate-PDF](https://github.com/Alejandro-ZZ/Automation-with-Python/tree/master/generate-PDF)**, this code shows a way that let you generate PDFs with the content that you want in Python using the `ReportLab module`.

## Requirements

All of these examples were probed in `Python 3.7.8` and they might work with other version. Not build-in module versions are shown in the **requirements.txt** file.
To install all modules needed run the following line in your terminal.

      python -m pip install -r requirements.txt

If you have already installed Python in your computer you can see its version by running one of the below lines in the terminal.

      python --version
      python -V
      python -VV

If you have one of the not build-in module already installed, you can see the version of all modules installed by running the following line

    pip freeze

To individually find the version number of a `module_name` you can grep on this output (for NIX machines):

    pip freeze | grep module_name

On windows, you can use findstr instead of grep

    pip freeze | findstr module_name
