from flask import Flask, render_template

app = Flask(__name__)
vm_list = []


@app.route('/')
def index():
    vms = vm_list
    return render_template('vms.html', vms=vms)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)