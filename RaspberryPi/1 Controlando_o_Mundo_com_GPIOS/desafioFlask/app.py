from flask import Flask, render_template, request
from automate import inicializaBoard, define_pino_como_saida, escreve_para_porta, resetar

app = Flask(__name__)

@app.route("/", methods=["GET",])
def index():
    return render_template("index.html")  

@app.route("/", methods=["POST",])
def submit():
    estado = False
    porta= False
    
    if(request.form["comando"]):
            comando = request.form["comando"]
            if(comando == "R"):
                mensagem = "PORTAS RESETADAS"
                resetar()
            else:
                mensagem = str(comando)
                if(comando[:2].isnumeric()):
                    porta= comando[:2]
                    pos =3
                else:
                    porta=comando[0]
                    pos =2
                print(len(comando))
                if(comando[pos -1 :] == "ON"):
                    estado = "1"
                else:
                    estado = "0"
                print(comando[pos - 1:])
                print(porta)
                escreve_para_porta(int(porta), int(estado))
            return render_template("index.html", porta=int(porta), estado=estado, mensagem=mensagem)
    else:
        return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
