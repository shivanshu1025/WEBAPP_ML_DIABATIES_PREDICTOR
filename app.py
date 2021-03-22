from keras.models import load_model
from flask import Flask,render_template,request
app=Flask("FLASKAPP")

@app.route("/form")
def form():
  return render_template("myform.html")
@app.route("/result")
def model():
  x1=int(request.args.get("x1"))
  x2=int(request.args.get("x2"))
  x3=int(request.args.get("x3"))
  x4=int(request.args.get("x4"))
  x5=int(request.args.get("x5"))
  x6=float(request.args.get("x6"))
  x7=float(request.args.get("x7"))
  x8=int(request.args.get("x8"))
  model = load_model("dia_model.h5")
  output = model.predict([[x1,x2,x3,x4,x5,x6,x7,x8]])
  if round(output[0][0])== 1:
    return "YOU MAY HAVE DIABATIES ..... CONSULT THE DOCTOR"
  else:
   return "YOU MAY NOT HAVE DIABATIES ..... CONSULT THE DOCTOR"
