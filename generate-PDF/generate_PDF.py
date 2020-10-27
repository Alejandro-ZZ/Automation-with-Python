from reportlab.platypus import SimpleDocTemplate
from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie

#Let us create a title, some text in paragraphs, and some charts and images
#Also known as Flowables
from reportlab.platypus import Paragraph, Spacer, Table, Image

#Let us tell reportlab what style we want each part of the document to have
from reportlab.lib.styles import getSampleStyleSheet

import os

def dict_to_list_of_lists(dict_data):
    '''
    Action: Converts a dictionary into a list-of-lists
    
    Inputs:
        dict_data -> Dictionary containing values to convert
    
    Output:
        table_data -> List of list data representing the dict_data info
    '''
    table_data = []
    for k, v in dict_data.items():
        table_data.append([k, v])

    return table_data


#Data where the PDF file will be based at
fruit = {
  "elderberries": 1,
  "figs": 1,
  "apples": 2,
  "durians": 3,
  "bananas": 5,
  "cherries": 8,
  "grapes": 13
}

#===========================================================
#||                                                       ||
#||                 GENERATING SIMPLE PDF                 ||
#||                                                       ||
#===========================================================

print("->Generating report object...")
#Generates a PDF by creating a 'report' object using the filename report.pdf
report = SimpleDocTemplate(os.path.join(os.getcwd(),"report.pdf"))

print("->Report object created in " + os.path.join(os.getcwd(),"report.pdf"))

# Creates a default style provided by the module
styles = getSampleStyleSheet()

print("->Generating a title...")
#Creates a title for the report file
report_title = Paragraph("A Complete Inventory of My Fruit", styles["h1"])

#Build the report PDF with the title created in 'report_title' 
#built() method takes a list of Flowable elements to generates the PDF.
report.build([report_title])

print("PDF built, check the file and press enter to continue...")
input('')
print("---------------------------------------" + "\n")

#===========================================================
#||                                                       ||
#||                     ADDING TABLE                      ||
#||                                                       ||
#===========================================================
#list-of-lists data to created a table
table_data = dict_to_list_of_lists(fruit)

print("->Generating table of fruits...")
#Creates a table to the report PDF
report_table = Table(data=table_data)

#Build the report PDF
report.build([report_title, report_table])

print("PDF built, check the file and press enter to continue...")
input('')
print("---------------------------------------" + "\n")

print("->Generating bordes to the table...")
#Creates a border around all of the cells in the table
table_style = [('GRID', (0,0), (-1,-1), 1, colors.black)]

print("->Creating table on the left...")
#Parameter hAling takes the values "LEFT" to move the table over to the left
report_table = Table(data=table_data, style=table_style, hAlign="LEFT")

#Build the report PDF
report.build([report_title, report_table])

print("PDF built, check the file and press enter to continue...")
input('')
print("---------------------------------------" + "\n")

#===========================================================
#||                                                       ||
#||                  ADDING GRAPGHIC                      ||
#||                                                       ||
#===========================================================

print("->Creating pie chart...")
#Creates a pie chart
report_pie = Pie(width=3*inch, height=3*inch)

print("->Adding data to the pie chart...")
#Adds data to the pie chart
report_pie.data = []
report_pie.labels = []
for fruit_name in sorted(fruit):
    report_pie.data.append(fruit[fruit_name])
    report_pie.labels.append(fruit_name)

#Place the pie chart into a Flowable Drawing.
report_chart = Drawing()
report_chart.add(report_pie)

#Build the report PDF
report.build([report_title, report_table, report_chart])

print("PDF built, check the file ...")
print("---------------------------------------" + "\n")
