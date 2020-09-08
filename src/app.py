from flask import Flask, render_template, request

from manager.activity import Activity

app = Flask(__name__)
activity = Activity(logger=app.logger)

@app.route('/')
def index():
    return render_vm_list()


@app.route('/', methods=['POST'])
def new_vm():
    activity.start_vm(width=request.form['width'], height=request.form['height'])
    return render_vm_list()


def render_vm_list():
    vms = activity.get_running_ip_list()
    return render_template('vms.html', vms=vms)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)