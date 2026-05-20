from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Esta será a página principal do seu PortfolioHUB
    return "<h1>PortfolioHUB - Em Desenvolvimento</h1><p>Integração com Git e GitHub ativa!</p>"

if __name__ == '__main__':
    app.run(debug=True)