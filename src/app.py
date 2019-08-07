from flask import Flask, render_template

from manager.activity import Activity

app = Flask(__name__)
activity = Activity(logger=app.logger)

class VMs(object):
    list = []

@app.route('/')
def index():
    return render_vm_list()


@app.route('/', methods=['POST'])
def new_vm():
    bot_ip = activity.start_vm()
    VMs.list += [bot_ip]
    return render_vm_list()


def render_vm_list():
    vms = VMs.list
    return render_template('vms.html', vms=vms)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)