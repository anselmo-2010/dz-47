from flask import Flask, render_template, request
from openpyxl import Workbook
from openpyxl import load_workbook


app = Flask(__name__)

@app.route('/')
def homepage():
    excels = load_workbook('inventar.xlsx')
    page = excels["Sheet"]
    lst = []
    i = 1
    while page["A"+str(i)].value != None:
        txt = page["A" + str(i)].value 
        lst.append(txt)
        i+=1                                           

    return render_template('index.html', goods = lst)




