from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    # Substitua pelo seu nome de usuário exato do GitHub
    username = "Diiriibeiiro01" 
    
    url = f"https://api.github.com/users/{username}/repos"
    
    try:
        # Faz a requisição segura para a API do GitHub
        response = requests.get(url)
        if response.status_code == 200:
            repos = response.json()  # Transforma o resultado em uma lista de projetos
        else:
            repos = []
    except Exception as e:
        repos = []
        print(f"Erro ao conectar na API: {e}")

    # Passa a lista de repositórios dinamicamente para o HTML
    return render_template('index.html', projetos=repos)

if __name__ == '__main__':
    app.run(debug=True)