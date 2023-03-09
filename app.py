from flask import Flask


app=Flask(__name__)


@app.route("/") #localhost:port_number/ome
##localhost:port_number/resultpage


def home():
    return "Junaid loves sameera"


if __name__=="__main__":
    app.run(debug=True) #port_number,option,host

