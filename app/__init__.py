from flask import Flask, jsonify, request


def create_app():
    app = Flask(__name__)
    todos = []
    next_id = 1

    @app.get('/health')
    def health():
        return jsonify(status='ok'), 200

    @app.get('/todos')
    def list_todos():
        return jsonify(todos), 200

    @app.post('/todos')
    def create_todo():
        nonlocal next_id
        payload = request.get_json(silent=True) or {}
        title = payload.get('title')
        if not isinstance(title, str) or not title.strip():
            return jsonify(error="'title' is required and must be a non-empty string"), 400
        todo = {'id': next_id, 'title': title.strip(), 'completed': False}
        next_id += 1
        todos.append(todo)
        return jsonify(todo), 201

    return app
