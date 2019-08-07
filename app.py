from flask import Flask, render_template

app = Flask(__name__)
vm_list = []


@app.route('/')
def index():
    return render_vm_list()


@app.route('/', methods=['POST'])
def new_vm():
    return render_vm_list()


def render_vm_list():
    vms = vm_list
    return render_template('vms.html', vms=vms)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)