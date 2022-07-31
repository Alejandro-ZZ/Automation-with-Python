# Generate a PDF file with Python

[generate_PDF.py](https://github.com/Alejandro-ZZ/Automation-with-Python/blob/master/generate-PDF/generate_PDF.py) is divide in three sections: 

- [GENERATING SIMPLE PDF](#generating-simple-pdf)
- [ADDING TABLE](#adding-table)
- [ADDING GRAPGHIC](#adding-grapghic)

Running the script will show you what action is being performed with a `print` function and wait until you hit the ENTER key so you can see the changes made to the PDF file, as shown below.

      -> Action taken...
      :
      :
      PDF built, check the file and press enter to continue...

After you press ENTER keyboard key, the program will executed the next action and will update the PDF so you can again see changes made and so on.

## GENERATING SIMPLE PDF

In this section the SimpleDocTemplate, from reportlab.platypus, class is used to create the object that will end up generating a PDF named "report.pdf" in the
current directory where the code is executed. 

Then a style for the PDF is generated, with a default included in the module. After this some other classes like: Paragraph, Spacer, Table, Image are taken from 
reportlab.platypus to, later, add some components (also known as Flowables) to the PDF.

## ADDING TABLE

As the name of this section says, the code will add a table to the PDF. However, to do this, data is needed to be in a ***list-of-lists*** (also called: 
***two-dimensional array***). To convert the data in the `fruit` dictionary into the right format, the function **`dict_to_list_of_lists`** is called; it takes a
parameter named `dict_data` wich is a dictionary. 

To add a black border to the table the colors class is used from reportlab.lib.

## ADDING GRAPGHIC

Finally a pie chart is added by using the Pie class from reportlab.graphics.charts.piecharts. This class lets us create a pie chart; however, due a pie isn't 
Flowable, to include it in the PDF this graphic is placed inside of a Flowable named **Drawing** (imported from reportlab.graphics.shapes).


**Note:** 
 
 * In this example code, the PDF is generated from information in a Python dictionary created in the same code. However, the information might be in another file
 like CSV, txt and others that can be read with different methods like `open`.
