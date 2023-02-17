from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__,template_folder='.')

# Hardcoded list of student organizations
STUDENT_ORGS = ['Club A', 'Club B', 'Club C', 'Club D', 'Club E']

# Global dictionary to store registered users
users = {}

# Home page
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get user input
        name = request.form.get('name')
        org = request.form.get('org')

        # Validate user input
        if not name:
            return render_template('index.html', error='Please enter a name.')
        if not org or org not in STUDENT_ORGS:
            return render_template('index.html', error='Please select a valid organization.')

        # Save user to dictionary
        users[name] = org

        # Redirect to registered users page
        return redirect(url_for('registered'))

    # Render home page
    return render_template('index.html', orgs=STUDENT_ORGS)

# Registered users page
@app.route('/registered')
def registered():
    return render_template('registered.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)