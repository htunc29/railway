from flask import Flask, render_template, request, redirect, url_for, session
import os

app = Flask(__name__)
app.secret_key = 'gizli_anahtar'  # Session için gerekli

@app.route('/', methods=['GET', 'POST'])
def home():
    if 'todos' not in session:
        session['todos'] = []
    if request.method == 'POST':
        yeni_todo = request.form.get('todo')
        if yeni_todo:
            session['todos'].append(yeni_todo)
            session.modified = True
        return redirect(url_for('home'))
    return render_template('index.html', todos=session['todos'])

@app.route('/sil/<int:index>')
def sil(index):
    if 'todos' in session and 0 <= index < len(session['todos']):
        session['todos'].pop(index)
        session.modified = True
    return redirect(url_for('home'))

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)
