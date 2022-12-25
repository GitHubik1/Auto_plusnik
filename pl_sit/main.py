from flask import Flask, render_template, request
import os
import klasses
from klasses import CLASS_ID

app = Flask(__name__)
@app.route("/", methods=['GET','POST'])
def index():
    message = ''
    if request.method =='POST':
        form = request.args.get('class')
        if form == 'update':
            class_ = request.form.get('class_select')
            if (class_id := klasses.find_klass(class_)) != None:
                os.system(f'cd ..; python3 run.py runonce {CLASS_ID[class_id].id_} {CLASS_ID[class_id].worksheet}')
        elif form[:3] == 'del':
            klass = klasses.find_klass(form[4:])
            CLASS_ID.pop(klass)
        elif form == 'new':
            CLASS_ID.append(klasses.klass('NaN', 'undifined', 'null'))
            klasses.save_db()
        elif form[:3] == 'upd':
            klass = klasses.find_klass(form[4:])
            CLASS_ID[klass].name = request.form.get('class_update_name')
            CLASS_ID[klass].id_ = request.form.get('class_update_id')
            CLASS_ID[klass].worksheet = request.form.get('class_update_worksheet')
            klasses.save_db()
        else:
            print('Что за шиза?')
    return render_template('index.html', message=message, variants=klasses.get_names(), klasses=klasses.CLASS_ID)

if __name__ == '__main__':
    klasses.read_db()
    app.run(host='0.0.0.0', port=3000, debug=True)
