# Add a new member
import sqlite3

def add_member(name, date_of_birth, email, membership_type, start_date, status):
    conn = sqlite3.connect('members.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO members (name, date_of_birth, email, membership_type, start_date, status)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (name, date_of_birth, email, membership_type, start_date, status))
    conn.commit()
    conn.close()

# Edit member information
def edit_member(member_id, name, date_of_birth, email, membership_type, start_date, status):
    conn = sqlite3.connect('members.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE members
        SET name = ?, date_of_birth = ?, email = ?, membership_type = ?, start_date = ?, status = ?
        WHERE id = ?
    ''', (name, date_of_birth, email, membership_type, start_date, status, member_id))
    conn.commit()
    conn.close()

# Delete a member
def delete_member(member_id):
    conn = sqlite3.connect('members.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM members WHERE id = ?', (member_id,))
    conn.commit()
    conn.close()

# Query all members or search by criteria
def query_members(search_term=None, filter_by=None, filter_value=None):
    conn = sqlite3.connect('members.db')
    cursor = conn.cursor()

    if search_term:
        cursor.execute('SELECT * FROM members WHERE name LIKE ?', (f'%{search_term}%',))
    elif filter_by and filter_value:
        cursor.execute(f'SELECT * FROM members WHERE {filter_by} = ?', (filter_value,))
    else:
        cursor.execute('SELECT * FROM members')

    members = cursor.fetchall()
    conn.close()
    return members
def get_member_by_id(member_id):
    conn = sqlite3.connect('members.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM members WHERE id = ?', (member_id,))
    member = cursor.fetchone()
    conn.close()
    return member