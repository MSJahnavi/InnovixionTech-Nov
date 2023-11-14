# app.py
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data - in-memory storage
contacts = [
    {'id': 1, 'name': 'John Doe', 'phone': '1234567890'},
    {'id': 2, 'name': 'Jane Smith', 'phone': '9876543210'},
]

@app.route('/')
def index():
    return render_template('index.html', contacts=contacts)

@app.route('/add_contact', methods=['POST'])
def add_contact():
    name = request.form['name']
    phone = request.form['phone']

    new_contact = {
        'id': len(contacts) + 1,
        'name': name,
        'phone': phone,
    }

    contacts.append(new_contact)

    return redirect(url_for('index'))

@app.route('/edit_contact/<int:contact_id>')
def edit_contact(contact_id):
    contact = next((c for c in contacts if c['id'] == contact_id), None)
    if contact:
        return render_template('edit_contact.html', contact=contact)
    else:
        return redirect(url_for('index'))

@app.route('/update_contact/<int:contact_id>', methods=['POST'])
def update_contact(contact_id):
    contact = next((c for c in contacts if c['id'] == contact_id), None)
    if contact:
        contact['name'] = request.form['name']
        contact['phone'] = request.form['phone']
        return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))

@app.route('/delete_contact/<int:contact_id>')
def delete_contact(contact_id):
    global contacts
    contacts = [c for c in contacts if c['id'] != contact_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
