from flask import Flask, request, jsonify
from database import BugTracker
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
db = BugTracker()

@app.route('/bugs', methods=['GET'])
def get_bugs():
    bugs = db.listar_bugs()
    return jsonify([{
        'id': bug[0],
        'titulo': bug[1],
        'descricao': bug[2],
        'passos_reproduzir': bug[3],
        'prioridade': bug[4],
        'status': bug[5],
        'data_criacao': bug[6]
    } for bug in bugs])

@app.route('/bugs', methods=['POST'])
def add_bug():
    data = request.json
    bug_id = db.adicionar_bug(
        titulo=data['titulo'],
        descricao=data['descricao'],
        passos_reproduzir=data['passos_reproduzir'],
        prioridade=data['prioridade']
    )
    return jsonify({'id': bug_id}), 201

@app.route('/funcionalidades', methods=['GET'])
def get_funcionalidades():
    funcs = db.listar_funcionalidades()
    return jsonify([{
        'id': func[0],
        'titulo': func[1],
        'comportamento_esperado': func[2],
        'situacao_atual': func[3],
        'prioridade': func[4],
        'data_criacao': func[5]
    } for func in funcs])

@app.route('/funcionalidades', methods=['POST'])
def add_funcionalidade():
    data = request.json
    func_id = db.adicionar_funcionalidade(
        titulo=data['titulo'],
        comportamento_esperado=data['comportamento_esperado'],
        situacao_atual=data.get('situacao_atual', 'Não implementado'),
        prioridade=data['prioridade']
    )
    return jsonify({'id': func_id}), 201

if __name__ == '__main__':
    app.run(debug=True, port=5000)