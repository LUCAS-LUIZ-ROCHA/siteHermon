from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    """
    Rota única para SPA - todas URLs servem index.html
    Perfeito para Vercel serverless + navegação suave
    """
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
