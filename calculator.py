from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import math

app = Flask("__name__")


app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///calculator.sqlite3"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)


class data(db.Model):
    Sr_No = db.Column(db.Integer, primary_key = True, autoincrement = True)
    Input_1 = db.Column(db.String)
    Input_2 = db.Column(db.String)
    Operation = db.Column(db.String)
    Result = db.Column(db.String)




@app.route("/calculator", methods = ["GET", "POST"])

def calculator_main_eng():
    return render_template("cal_main_eng.html")

@app.route("/calculator/hindi", methods = ["GET", "POST"])
def calculator_main_hin():
    return render_template("cal_main_hin.html")

@app.route("/calculator_eng", methods = ["GET", "POST"])
def calculator_eng():
    if request.method == "GET":
        return render_template("calculator_eng.html")

    else:

        o1 = str(request.form["o1"])
        if o1 == "":
            o1 = 0
        else :
            o1 = float(o1)
        o2 = str(request.form["o2"])
        if o2 == "":
            o2 = 0
        else:
            o2 = float(o2)


        operation = str(request.form["operation"])




#---------------------------------------- Basic Arithmatic Operations ----------------------------------------




        if operation == "sum":

            result = o1 + o2

        elif operation == "sub":

            result = o1 - o2

        elif operation == "mul":

            result = o1 * o2

        elif operation == "div":

            if o2 == 0:
                result = "Division by Zero is not possible."

            else:
                result = o1 / o2

        elif operation == "quo":

            if o2 == 0:
                result = "Division by Zero is not possible."

            else:
                result = o1 // o2

        elif operation == "rem":

            if o2 == 0:
                result = "Division by Zero is not possible."

            else:
                result = o1 % o2




#---------------------------------------- Roots Operations ----------------------------------------""""




        elif operation == "s_root":
            if o1 == 0 and o2 != 0:
                a = o2

            elif o1 != 0 and o2 == 0:
                a = o1

            elif o1 == 0 and o2 == 0:
                a = 0

            else:
                a = o1

            result = round(math.sqrt(a), 15)

        elif operation == "c_root":
            if o1 == 0 and o2 != 0:
                a = o2

            elif o1 != 0 and o2 == 0:
                a = o1

            elif o1 == 0 and o2 == 0:
                a = 0

            else:
                a = o1

            result = round(math.cbrt(a), 15)





#---------------------------------------- Exponential Operations ----------------------------------------"""





        elif operation == "power":

            result = round(pow(o1, o2),15)

        elif operation == "c_log":

            if o1 == 0 and o2 != 0:
                a = o2

            elif o1 != 0 and o2 == 0:
                a = o1

            elif o1 == 0 and o2 == 0:
                a = 0

            else:
                a = o1

            result = round(math.log10(a), 15)

        elif operation == "n_log":

            if o1 == 0 and o2 != 0:
                a = o2

            elif o1 != 0 and o2 == 0:
                a = o1

            elif o1 == 0 and o2 == 0:
                a = 0

            else:
                a = o1

            result = round(math.log(a), 15)

        elif operation == "log_b":

            result = round(math.log(o2,o1), 15)

        elif operation == "exp":

            if o1 == 0 and o2 != 0:
                a = o2

            elif o1 != 0 and o2 == 0:
                a = o1

            elif o1 == 0 and o2 == 0:
                a = 0

            else:
                a = o1

            if a > 709.782:
                result = "Infinity"
            else:
                result = round(math.exp(a), 15)


#---------------------------------------- Angular Conversion Operations ----------------------------------------""""





        elif operation == "rad":

            if o1 == 0 and o2 != 0:
                a = o2

            elif o1 != 0 and o2 == 0:
                a = o1

            elif o1 == 0 and o2 == 0:
                a = 0

            else:
                a = o1

            result = str(round(math.radians(a), 15)) + " Radian"

        elif operation == "deg":

            if o1 == 0 and o2 != 0:
                a = o2

            elif o1 != 0 and o2 == 0:
                a = o1

            elif o1 == 0 and o2 == 0:
                a = 0

            else:
                a = o1

            result = str(round(math.degrees(a), 15)) + " Degree"






#---------------------------------------- Trigonometric Operations ----------------------------------------""""




        elif operation == "sin_d":

            if o1 == 0 and o2 != 0:
                a = o2

            elif o1 != 0 and o2 == 0:
                a = o1

            elif o1 == 0 and o2 == 0:
                a = 0

            else:
                a = o1

            a = math.radians(a)
            result = round(math.sin(a), 15)

        elif operation == "cos_d":

            if o1 == 0 and o2 != 0:
                a = o2

            elif o1 != 0 and o2 == 0:
                a = o1

            elif o1 == 0 and o2 == 0:
                a = 0

            else:
                a = o1

            a = math.radians(a)
            result = round(math.cos(a), 15)

        elif operation == "tan_d":

            if o1 == 0 and o2 != 0:
                a = o2

            elif o1 != 0 and o2 == 0:
                a = o1

            elif o1 == 0 and o2 == 0:
                a = 0

            else:
                a = o1

            a = math.radians(a)
            sin = round(math.sin(a), 15)
            cos = round(math.cos(a), 15)

            if cos != 0:
                result = sin/cos
            else:
                result = "Undefined"

        elif operation == "csc_d":

            if o1 == 0 and o2 != 0:
                a = o2

            elif o1 != 0 and o2 == 0:
                a = o1

            elif o1 == 0 and o2 == 0:
                a = 0

            else:
                a = o1

            a = math.radians(a)
            a = round(math.sin(a), 15)

            if a != 0:
                result = 1 / a
            else:
                result = "Undefined"

        elif operation == "sec_d":

            if o1 == 0 and o2 != 0:
                a = o2

            elif o1 != 0 and o2 == 0:
                a = o1

            elif o1 == 0 and o2 == 0:
                a = 0

            else:
                a = o1

            a = math.radians(a)
            a = round(math.cos(a), 15)

            if a != 0:
                result = 1 / a
            else:
                result = "Undefined"

        elif operation == "cot_d":

            if o1 == 0 and o2 != 0:
                a = o2

            elif o1 != 0 and o2 == 0:
                a = o1

            elif o1 == 0 and o2 == 0:
                a = 0

            else:
                a = o1

            a = math.radians(a)

            sin = round(math.sin(a), 15)
            cos = round(math.cos(a), 15)

            if sin != 0:
                result = cos / sin
            else:
                result = "Undefined"

        elif operation == "sin_r":

            if o1 == 0 and o2 != 0:
                a = o2

            elif o1 != 0 and o2 == 0:
                a = o1

            elif o1 == 0 and o2 == 0:
                a = 0

            else:
                a = o1

            result = round(math.sin(a), 15)

        elif operation == "cos_r":

            if o1 == 0 and o2 != 0:
                a = o2

            elif o1 != 0 and o2 == 0:
                a = o1

            elif o1 == 0 and o2 == 0:
                a = 0

            else:
                a = o1

            result = round(math.cos(a), 15)

        elif operation == "tan_r":

            if o1 == 0 and o2 != 0:
                a = o2

            elif o1 != 0 and o2 == 0:
                a = o1

            elif o1 == 0 and o2 == 0:
                a = 0

            else:
                a = o1

            sin = round(math.sin(a), 15)
            cos = round(math.cos(a), 15)

            if cos != 0:
                result = sin/cos
            else:
                result = "Undefined"

        elif operation == "csc_d":

            if o1 == 0 and o2 != 0:
                a = o2

            elif o1 != 0 and o2 == 0:
                a = o1

            elif o1 == 0 and o2 == 0:
                a = 0

            else:
                a = o1

            a = round(math.sin(a), 15)

            if a != 0:
                result = 1 / a
            else:
                result = "Undefined"

        elif operation == "sec_d":

            if o1 == 0 and o2 != 0:
                a = o2

            elif o1 != 0 and o2 == 0:
                a = o1

            elif o1 == 0 and o2 == 0:
                a = 0

            else:
                a = o1

            a = round(math.cos(a), 15)

            if a != 0:
                result = 1 / a
            else:
                result = "Undefined"

        elif operation == "cot_d":

            if o1 == 0 and o2 != 0:
                a = o2

            elif o1 != 0 and o2 == 0:
                a = o1

            elif o1 == 0 and o2 == 0:
                a = 0

            else:
                a = o1

            sin = round(math.sin(a), 15)
            cos = round(math.cos(a), 15)

            if sin != 0:
                result = cos / sin
            else:
                result = "Undefined"

        elif operation == "asin_d":

            if o1 == 0 and o2 != 0:
                a = o2

            elif o1 != 0 and o2 == 0:
                a = o1

            elif o1 == 0 and o2 == 0:
                a = 0

            else:
                a = o1

            a = round(math.asin(a), 15)
            result = str(math.degrees(a)) + " Degree"

        elif operation == "acos_d":

            if o1 == 0 and o2 != 0:
                a = o2

            elif o1 != 0 and o2 == 0:
                a = o1

            elif o1 == 0 and o2 == 0:
                a = 0

            else:
                a = o1

            a = round(math.acos(a), 15)
            result = str(math.degrees(a)) + " Degree"

        elif operation == "atan_d":

            if o1 == 0 and o2 != 0:
                a = o2

            elif o1 != 0 and o2 == 0:
                a = o1

            elif o1 == 0 and o2 == 0:
                a = 0

            else:
                a = o1

            sin = round(math.asin(a), 15)
            cos = round(math.acos(a), 15)

            a = round(math.atan(a), 15)
            result = str(math.degrees(a)) + " Degree"

        elif operation == "acsc_d":

            if o1 == 0 and o2 != 0:
                a = 1/o2

            elif o1 != 0 and o2 == 0:
                a = 1/o1

            elif o1 == 0 and o2 == 0:
                a = 0

            else:
                a = 1/o1

            a = round(math.asin(a), 15)
            result = str(math.degrees(a)) + " Degree"

        elif operation == "asec_d":

            if o1 == 0 and o2 != 0:
                x = 1 / o2

            elif o1 != 0 and o2 == 0:
                x = 1 / o1

            elif o1 == 0 and o2 == 0:
                x = 0

            else:
                x = 1 / o1

            a = round(math.acos(x), 15)
            result = str(math.degrees(a)) + " Degree"

        elif operation == "acot_d":

            if o1 == 0 and o2 != 0:
                a = 1/o2
                a = round(math.atan(a), 15)
                b = math.degrees(a)

            elif o1 != 0 and o2 == 0:
                a = 1/o1
                a = round(math.atan(a), 15)
                b = math.degrees(a)

            elif o1 == 0 and o2 == 0:
                a = 0
                b = 90.0

            else:
                a = 1/o1
                a = round(math.atan(a), 15)
                b = math.degrees(a)

            result = str(b) + " Degree"

        elif operation == "asin_r":

            if o1 == 0 and o2 != 0:
                a = o2

            elif o1 != 0 and o2 == 0:
                a = o1

            elif o1 == 0 and o2 == 0:
                a = 0

            else:
                a = o1

            result = str(round(math.asin(a), 15)) + " Radian"

        elif operation == "acos_r":

            if o1 == 0 and o2 != 0:
                a = o2

            elif o1 != 0 and o2 == 0:
                a = o1

            elif o1 == 0 and o2 == 0:
                a = 0

            else:
                a = o1

            result = str(round(math.acos(a), 15)) + " Radian"

        elif operation == "atan_r":

            if o1 == 0 and o2 != 0:
                a = o2

            elif o1 != 0 and o2 == 0:
                a = o1

            elif o1 == 0 and o2 == 0:
                a = 0

            else:
                a = o1

            result = str(round(math.atan(a), 15)) + " Radian"

        elif operation == "acsc_r":

            if o1 == 0 and o2 != 0:
                a = 1/o2

            elif o1 != 0 and o2 == 0:
                a = 1/o1

            elif o1 == 0 and o2 == 0:
                a = 0

            else:
                a = 1/o1

            result = str(round(math.asin(a), 15)) + " Radian"

        elif operation == "asec_r":

            if o1 == 0 and o2 != 0:
                a = 1/o2

            elif o1 != 0 and o2 == 0:
                a = 1/o1

            elif o1 == 0 and o2 == 0:
                a = 0

            else:
                a = 1/o1

            result = str(round(math.acos(a), 15)) + " Radian"

        elif operation == "acot_r":

            if o1 == 0 and o2 != 0:
                a = 1/o2

            elif o1 != 0 and o2 == 0:
                a = 1/o1

            elif o1 == 0 and o2 == 0:
                a = 0

            else:
                a = 1/o1

            result = str(round(math.atan(a), 15)) + " Radian"






#---------------------------------------- Hyperbolic Operations ----------------------------------------"""






        elif operation == "sinh_d":

            if o1 == 0 and o2 != 0:
                a = o2

            elif o1 != 0 and o2 == 0:
                a = o1

            elif o1 == 0 and o2 == 0:
                a = 0

            else:
                a = o1

            result = round(math.sinh(a), 15)

        elif operation == "cosh_d":

            if o1 == 0 and o2 != 0:
                a = o2

            elif o1 != 0 and o2 == 0:
                a = o1

            elif o1 == 0 and o2 == 0:
                a = 0

            else:
                a = o1

            a = math.radians(a)
            result = round(math.cosh(a), 15)

        elif operation == "tanh_d":

            if o1 == 0 and o2 != 0:
                a = o2

            elif o1 != 0 and o2 == 0:
                a = o1

            elif o1 == 0 and o2 == 0:
                a = 0

            else:
                a = o1

            a = math.radians(a)
            sin = round(math.sinh(a), 15)
            cos = round(math.cosh(a), 15)

            if cos != 0:
                result = sin / cos
            else:
                result = "Undefined"

        elif operation == "csch_d":

            if o1 == 0 and o2 != 0:
                a = o2

            elif o1 != 0 and o2 == 0:
                a = o1

            elif o1 == 0 and o2 == 0:
                a = 0

            else:
                a = o1

            a = math.radians(a)
            a = round(math.sin(a), 15)

            if a != 0:
                result = 1 / a
            else:
                result = "Undefined"

        elif operation == "sech_d":

            if o1 == 0 and o2 != 0:
                a = o2

            elif o1 != 0 and o2 == 0:
                a = o1

            elif o1 == 0 and o2 == 0:
                a = 0

            else:
                a = o1

            a = math.radians(a)
            a = round(math.cos(a), 15)

            if a != 0:
                result = 1 / a
            else:
                result = "Undefined"

        elif operation == "coth_d":

            if o1 == 0 and o2 != 0:
                a = o2

            elif o1 != 0 and o2 == 0:
                a = o1

            elif o1 == 0 and o2 == 0:
                a = 0

            else:
                a = o1

            a = math.radians(a)

            sin = round(math.sin(a), 15)
            cos = round(math.cos(a), 15)

            if sin != 0:
                result = cos / sin
            else:
                result = "Undefined"

        elif operation == "sinh_r":

            if o1 == 0 and o2 != 0:
                a = o2

            elif o1 != 0 and o2 == 0:
                a = o1

            elif o1 == 0 and o2 == 0:
                a = 0

            else:
                a = o1

            result = round(math.sin(a), 15)

        elif operation == "coshr":

            if o1 == 0 and o2 != 0:
                a = o2

            elif o1 != 0 and o2 == 0:
                a = o1

            elif o1 == 0 and o2 == 0:
                a = 0

            else:
                a = o1

            result = round(math.cos(a), 15)

        elif operation == "tanh_r":

            if o1 == 0 and o2 != 0:
                a = o2

            elif o1 != 0 and o2 == 0:
                a = o1

            elif o1 == 0 and o2 == 0:
                a = 0

            else:
                a = o1

            sin = round(math.sin(a), 15)
            cos = round(math.cos(a), 15)

            if cos != 0:
                result = sin / cos
            else:
                result = "Undefined"

        elif operation == "csch_r":

            if o1 == 0 and o2 != 0:
                a = o2

            elif o1 != 0 and o2 == 0:
                a = o1

            elif o1 == 0 and o2 == 0:
                a = 0

            else:
                a = o1

            a = round(math.sin(a), 15)

            if a != 0:
                result = 1 / a
            else:
                result = "Undefined"

        elif operation == "sech_r":

            if o1 == 0 and o2 != 0:
                a = o2

            elif o1 != 0 and o2 == 0:
                a = o1

            elif o1 == 0 and o2 == 0:
                a = 0

            else:
                a = o1

            a = round(math.cos(a), 15)

            if a != 0:
                result = 1 / a
            else:
                result = "Undefined"

        elif operation == "coth_r":

            if o1 == 0 and o2 != 0:
                a = o2

            elif o1 != 0 and o2 == 0:
                a = o1

            elif o1 == 0 and o2 == 0:
                a = 0

            else:
                a = o1

            sin = round(math.sin(a), 15)
            cos = round(math.cos(a), 15)

            if sin != 0:
                result = cos / sin
            else:
                result = "Undefined"

        elif operation == "asin_d":

            if o1 == 0 and o2 != 0:
                a = o2

            elif o1 != 0 and o2 == 0:
                a = o1

            elif o1 == 0 and o2 == 0:
                a = 0

            else:
                a = o1

            a = round(math.asin(a), 15)
            result = str(math.degrees(a)) + " Degree"

        elif operation == "acos_d":

            if o1 == 0 and o2 != 0:
                a = o2

            elif o1 != 0 and o2 == 0:
                a = o1

            elif o1 == 0 and o2 == 0:
                a = 0

            else:
                a = o1

            a = round(math.acos(a), 15)
            result = str(math.degrees(a)) + " Degree"

        elif operation == "atan_d":

            if o1 == 0 and o2 != 0:
                a = o2

            elif o1 != 0 and o2 == 0:
                a = o1

            elif o1 == 0 and o2 == 0:
                a = 0

            else:
                a = o1

            sin = round(math.asin(a), 15)
            cos = round(math.acos(a), 15)

            a = round(math.atan(a), 15)
            result = str(math.degrees(a)) + " Degree"

        elif operation == "acsc_d":

            if o1 == 0 and o2 != 0:
                a = 1 / o2

            elif o1 != 0 and o2 == 0:
                a = 1 / o1

            elif o1 == 0 and o2 == 0:
                a = 0

            else:
                a = 1 / o1

            a = round(math.asin(a), 15)
            result = str(math.degrees(a)) + " Degree"

        elif operation == "asec_d":

            if o1 == 0 and o2 != 0:
                x = 1 / o2

            elif o1 != 0 and o2 == 0:
                x = 1 / o1

            elif o1 == 0 and o2 == 0:
                x = 0

            else:
                x = 1 / o1

            a = round(math.acos(x), 15)
            result = str(math.degrees(a)) + " Degree"

        elif operation == "acot_d":

            if o1 == 0 and o2 != 0:
                a = 1 / o2
                a = round(math.atan(a), 15)
                b = math.degrees(a)

            elif o1 != 0 and o2 == 0:
                a = 1 / o1
                a = round(math.atan(a), 15)
                b = math.degrees(a)

            elif o1 == 0 and o2 == 0:
                a = 0
                b = 90.0

            else:
                a = 1 / o1
                a = round(math.atan(a), 15)
                b = math.degrees(a)

            result = str(b) + " Degree"

        elif operation == "asin_r":

            if o1 == 0 and o2 != 0:
                a = o2

            elif o1 != 0 and o2 == 0:
                a = o1

            elif o1 == 0 and o2 == 0:
                a = 0

            else:
                a = o1

            result = str(round(math.asin(a), 15)) + " Radian"

        elif operation == "acos_r":

            if o1 == 0 and o2 != 0:
                a = o2

            elif o1 != 0 and o2 == 0:
                a = o1

            elif o1 == 0 and o2 == 0:
                a = 0

            else:
                a = o1

            result = str(round(math.acos(a), 15)) + " Radian"

        elif operation == "atan_r":

            if o1 == 0 and o2 != 0:
                a = o2

            elif o1 != 0 and o2 == 0:
                a = o1

            elif o1 == 0 and o2 == 0:
                a = 0

            else:
                a = o1

            result = str(round(math.atan(a), 15)) + " Radian"

        elif operation == "acsc_r":

            if o1 == 0 and o2 != 0:
                a = 1 / o2

            elif o1 != 0 and o2 == 0:
                a = 1 / o1

            elif o1 == 0 and o2 == 0:
                a = 0

            else:
                a = 1 / o1

            result = str(round(math.asin(a), 15)) + " Radian"

        elif operation == "asec_r":

            if o1 == 0 and o2 != 0:
                a = 1 / o2

            elif o1 != 0 and o2 == 0:
                a = 1 / o1

            elif o1 == 0 and o2 == 0:
                a = 0

            else:
                a = 1 / o1

            result = str(round(math.acos(a), 15)) + " Radian"

        elif operation == "acot_r":

            if o1 == 0 and o2 != 0:
                a = 1 / o2

            elif o1 != 0 and o2 == 0:
                a = 1 / o1

            elif o1 == 0 and o2 == 0:
                a = 0

            else:
                a = 1 / o1

            result = str(round(math.atan(a), 15)) + " Radian"



        else:
            result = "Please select any one operation"

        entry = data(Input_1=str(o1), Input_2=str(o2), Operation=str(operation), Result=str(result))

        db.session.add(entry)
        db.session.commit()

        return render_template("calculator_eng.html", result = result)






# ---------------------------------------- CALCULATOR HINDI VERSION  ---------------------------------------- """
# ---------------------------------------- CALCULATOR HINDI VERSION  ---------------------------------------- """
# ---------------------------------------- CALCULATOR HINDI VERSION  ---------------------------------------- """






@app.route("/calculator_hin", methods = ["GET", "POST"])
def calculator_hin():

    if request.method == "GET":
        return render_template("calculator_hin.html")

    else:

        o1 = str(request.form["o1"])
        if o1 == "":
            o1 = 0
        else :
            o1 = float(o1)
        o2 = str(request.form["o2"])
        if o2 == "":
            o2 = 0
        else:
            o2 = float(o2)


        operation = str(request.form["operation"])

        if operation == "sum":
            result = o1 + o2

        elif operation == "sub":

            result = o1 - o2

        elif operation == "mul":

            result = o1 * o2

        elif operation == "div":

            if o2 == 0:
                result = "Division by Zero is not possible."

            else:
                result = o1 / o2

        elif operation == "quo" :
             if o2 == 0:
                 result = "Division by Zero is not possible."
             else:
                 result = o1 // o2

        elif operation == "rem":
             if o2 == 0:
                 result = "Division by Zero is not possible."

             else:
                 result = o1 % o2

        elif operation == "SIN":

            if o1 == 0 and o2 != 0:
                a = o2

            elif o1 != 0 and o2 == 0:
                a = o1

            elif o1 == 0 and o2 == 0:
                a = 0

            else:
                a = o1

            a = math.radians(a)
            result = round(math.sin(a), 15)

        elif operation == "COS":

            if o1 == 0 and o2 != 0:
                a = o2

            elif o1 != 0 and o2 == 0:
                a = o1

            elif o1 == 0 and o2 == 0:
                a = 0

            else:
                a = o1

            a = math.radians(a)
            result = round(math.cos(a), 15)

        elif operation == "TAN":

            if o1 == 0 and o2 != 0:
                a = o2

            elif o1 != 0 and o2 == 0:
                a = o1

            elif o1 == 0 and o2 == 0:
                a = 0

            else:
                a = o1

            a = math.radians(a)
            sin = round(math.sin(a), 15)
            cos = round(math.cos(a), 15)

            if cos != 0:
                result = sin/cos
            else:
                result = "अपरिभाषित "

        elif operation == "COSEC":

            if o1 == 0 and o2 != 0:
                a = o2

            elif o1 != 0 and o2 == 0:
                a = o1

            elif o1 == 0 and o2 == 0:
                a = 0

            else:
                a = o1

            a = math.radians(a)
            a = round(math.sin(a), 15)

            if a != 0:
                result = 1 / a
            else:
                result = "अपरिभाषित "

        elif operation == "SEC":

            if o1 == 0 and o2 != 0:
                a = o2

            elif o1 != 0 and o2 == 0:
                a = o1

            elif o1 == 0 and o2 == 0:
                a = 0

            else:
                a = o1

            a = math.radians(a)
            a = round(math.cos(a), 15)

            if a != 0:
                result = 1 / a
            else:
                result = "अपरिभाषित "

        elif operation == "COT":

            if o1 == 0 and o2 != 0:
                a = o2

            elif o1 != 0 and o2 == 0:
                a = o1

            elif o1 == 0 and o2 == 0:
                a = 0

            else:
                a = o1

            a = math.radians(a)

            sin = round(math.sin(a), 15)
            cos = round(math.cos(a), 15)

            if sin != 0:
                result = cos / sin
            else:
                result = "अपरिभाषित "

        elif operation == "":
            result = "Please select any one operation"

        entry = data(Input_1=str(o1), Input_2=str(o2), Operation=str(operation), Result=str(result))

        db.session.add(entry)
        db.session.commit()

        return render_template("calculator_hin.html", result = result)










if __name__ == "__main__":
    app.debug = True
    app.run()