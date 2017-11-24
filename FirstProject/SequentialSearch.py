from flask import Flask as fl, render_template
import numpy as np
import datetime as d
import math
import Algorithms

app = fl(__name__)

@app.route('/')
def index():
    return 'Tran Anh'

@app.route('/dynamic/')
@app.route('/dynamic/<str_A>/<str_B>')
def dynamic(str_A=None, str_B=None):
    if str_A:
        A = np.fromstring(str_A, dtype='|S1')
        B = np.fromstring(str_B, dtype='|S1')
        ED1, ptrl, edInt = Algorithms.edit_distance(A, B)
        ED1 = ED1.tolist()
        ptrl = ptrl.tolist()
        arr_A = list(str_A)
        arr_B = list(str_B)
        return render_template("layout.html", EDI=ED1, PTR=ptrl, str_A=str_A, str_B=str_B, arr_A=arr_A, arr_B=arr_B, edInt=edInt)
    else:
        A = np.fromstring("", dtype='|S1')
        B = np.fromstring("", dtype='|S1')
        ED1, ptrl = Algorithms.edit_distance(A, B)
        ED1 = ED1.tolist()
        ptrl = ptrl.tolist()
        return render_template("layout.html", EDI=ED1, PTR=ptrl, str_A=str_A, str_B=str_B)


    #print("ED using basic method: \n", ED1, "\n Trace-back table: \n", ptr1)
    # toBePrinted = 'ED using basic method: \n\n'
    #
    # for x in ED1:
    #     toBePrinted += str(x)
    #     toBePrinted += '\n'
    #
    # toBePrinted += '\n'
    # toBePrinted += '\n Trace-back table: \n\n'
    #
    # for x in ptr1:
    #     toBePrinted += str(x)
    #     toBePrinted += '\n'

    return render_template("layout.html", toBePrinted=toBePrinted, str_A=str_A, str_B=str_B)

if __name__ == "__main__":
    app.run()

