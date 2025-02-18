from flask import Flask, render_template, request, redirect
import sqlite3
from member_operations import query_members  # Import the query_members function
from member_operations import get_member_by_id

app = Flask(__name__)

# Home page - Display members with search and filter
@app.route('/')
def index():
    search_term = request.args.get('search', None)
    filter_by = request.args.get('filter_by', None)
    filter_value = request.args.get('filter_value', None)

    # Fetch members based on search or filter
    members = query_members(search_term=search_term, filter_by=filter_by, filter_value=filter_value)
    return render_template('index.html', members=members)

# Add member page
@app.route('/add', methods=['GET', 'POST'])
def add_member():
    if request.method == 'POST':
        name = request.form['name']
        date_of_birth = request.form['date_of_birth']
        email = request.form['email']
        membership_type = request.form['membership_type']
        start_date = request.form['start_date']
        status = request.form['status']
        
        conn = sqlite3.connect('members.db')
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO members (name, date_of_birth, email, membership_type, start_date, status)
        VALUES (?, ?, ?, ?, ?, ?)
        ''', (name, date_of_birth, email, membership_type, start_date, status))
        conn.commit()
        conn.close()
        return redirect('/')
    return render_template('add_edit.html')


@app.route('/edit/<int:member_id>', methods=['GET', 'POST'])
def edit_member(member_id):
    if request.method == 'POST':
        # Handle form submission to update the member
        name = request.form['name']
        date_of_birth = request.form['date_of_birth']
        email = request.form['email']
        membership_type = request.form['membership_type']
        start_date = request.form['start_date']
        status = request.form['status']
        
        conn = sqlite3.connect('members.db')
        cursor = conn.cursor()
        cursor.execute('''
        UPDATE members
        SET name = ?, date_of_birth = ?, email = ?, membership_type = ?, start_date = ?, status = ?
        WHERE id = ?
        ''', (name, date_of_birth, email, membership_type, start_date, status, member_id))
        conn.commit()
        conn.close()
        return redirect('/')
    
    # Fetch the member's data and render the edit form
    member = get_member_by_id(member_id)
    return render_template('add_edit.html', member=member)

# Delete member
@app.route('/delete/<int:member_id>')
def delete_member(member_id):
    conn = sqlite3.connect('members.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM members WHERE id = ?', (member_id,))
    conn.commit()
    conn.close()
    return redirect('/')

# Run the app
if __name__ == '__main__':
    app.run(debug=True)