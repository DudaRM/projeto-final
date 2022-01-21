#Importar o que foi feito no init.py para iniciar a aplicação e rodar a mesma
from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True) #toda vez que fizer uma mudança, atualiza de forma automática
    #para rodar o site de forma controlada, apenas quando eu quiser
    