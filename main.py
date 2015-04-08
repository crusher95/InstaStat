from flask import jsonify
from flask import Flask, request, redirect, url_for, make_response, render_template
import time
import handler
import helper

from storage import Storage

from conf import *
import sys, os

app = Flask(__name__, static_url_path='')


@app.errorhandler(403)
@app.errorhandler(404)
def error(x):
    return redirect(url_for('root'))


f = {'error': "You Don't have permission to access this page"}


@app.route('/', methods=['GET', 'POST'])
def root():
    try:
        authUrl = helper.getLoginUrl()
       # return '<a href="%s">Connect with Instagram</a>' % authUrl

        return render_template('login.html', authUrl=authUrl), 200, html_header

    except Exception as e:
        print(e)


@app.route("/oauth_callback", methods=['GET'])
def callback():
    try:
        code = request.args.get('code', False)
        if code:
            access_token, user_info = helper.getAccessToken(code=code)
            # cookie = db.put(access_token)
            db.put2(access_token, user_info)
            response = make_response(redirect(url_for('dashboard')))
            response.set_cookie('session_id', db.put(access_token))
            return response

        else:
            return redirect(url_for('root'))
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        print(exc_type, fname, exc_tb.tb_lineno)
        print(e)
        return redirect(url_for('root'))


@app.route("/dashboard", methods=['GET'])
def dashboard():
    try:
        sid = request.cookies.get('session_id', False)
        if sid and db.get(sid, False):
            return redirect('main.html'), 200, html_header
        else:
            response = make_response(redirect(url_for('root')))
            response.set_cookie('session_id', None)
            return response
    except Exception as e:
        print e


@app.route("/dashboard/user_details", methods=['GET'])
def dashboard_user_details():
    sid = request.cookies.get('session_id', False)
    if sid and db.get(sid, False):
        user = handler.UserDetails(access_token=db.get(sid))
        resp = user.get()
        return resp, 200, json_header
    else:
        return jsonify(**f), 200,json_header


@app.route("/dashboard/fans", methods=['GET'])
def dashboard_fans():
    try:
        sid = request.cookies.get('session_id', False)
        if sid and db.get(sid, False):
            fans = handler.MyFans(access_token=db.get(sid))
            resp = fans.get()
            return resp, 200, json_header
        else:
            return jsonify(**f), 200,json_header

    except Exception as e:
        print e


@app.route("/dashboard/non_followers", methods=['GET'])
def dashboard_non_followers():
    sid = request.cookies.get('session_id', False)

    if sid and db.get(sid, False):
        non_followers = handler.MyNonFollowers(access_token=db.get(sid))
        resp = non_followers.get()
        return resp, 200, json_header

    else:
        return jsonify(**f), 200,json_header


@app.route("/follow", methods=['GET'])
def follow():
    sid = request.cookies.get('session_id', False)
    if sid and db.get(sid, False):
        id = request.args.get("id")
        #print(id)

        if helper.follow(access_token=db.get(sid),userid=id):
            return "Successfully followed"
        else:
            return "Some Error Occured", 400
    else:
        return jsonify(**f), 200,json_header


@app.route("/unfollow", methods=['GET'])
def unfollow():
    sid = request.cookies.get('session_id', False)
    if sid and db.get(sid, False):
        id = request.args.get("id")
        #print id
        #return "Successfully Unfollowed"
        if helper.unfollow(access_token=db.get(sid),userid=id):
            return "Successfully Unfollowed"
        else:
            return "Some Error Occured", 400
    else:
        return jsonify(**f), 200,json_header

if __name__ == '__main__':
    try:
        db = Storage()
        app.run(host=webconfig['host'], port=int(webconfig['port']))
    except Exception as e:
        print e