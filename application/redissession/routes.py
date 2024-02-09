from . import redis_session_blueprint
from flask import request, session, render_template_string, redirect

@redis_session_blueprint.route('/set-username', methods=['GET', 'POST'])
def redis_session_set_username():
    if request.method == "POST":
        session['username'] = request.form['username']
        return redirect('/get-username')
        
    return """
        <form method="post">
        <lable>Enter your username </lable>
        <input type="text" name="username" autocomplete="off" required />
        <button type="submit">Submit</button>
        </form>
    """
    
@redis_session_blueprint.route('/get-username', methods=['GET'])
def redis_session_get_username():
    return render_template_string("""
        {% if session['username'] %}
            <h1> wlcome {{session['username']}}</h1>
        {% else %}
            <h1> please enter your username <a href="/set-username"> here </a></h1>
        {% endif %}
    """)
    
@redis_session_blueprint.route('/delete-username', methods=['GET'])
def delete_redis_session_username():
    session.pop('username', default=None)
    return '<h1> session deleted</1>'