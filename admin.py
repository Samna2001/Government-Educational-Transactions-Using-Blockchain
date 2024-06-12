from flask import *
from database import *


admin=Blueprint('admin',__name__)


@admin.route('/admin_home')
def admin_home():
	return render_template('adminhome.html')


@admin.route('/admin_verify_staff',methods=['post','get'])
def admin_verify_staff():
	data={}
	q="select * from staff inner join login using(login_id)"
	data['viee']=select(q)

	if 'action' in request.args:
		action=request.args['action']
		
		lid=request.args['lid']
		category=request.args['category']
	else:
		action=None

	if action=='approve':
		q="update login set usertype='%s' where login_id='%s'"%(category,lid)
		update(q)
		flash("approved successfully")
		return redirect(url_for('admin.admin_verify_staff'))

	if action=='reject':
		q="update login set usertype='rejected' where login_id='%s'"%(lid)
		update(q)

		flash("rejected successfully")
		return redirect(url_for('admin.admin_verify_staff'))
	return render_template('admin_verify_staff.html',data=data)
	




@admin.route('/admin_public_complaint',methods=['post','get'])
def admin_public_complaint():
	data={}

	q="select * from public_complaint "
	data['view']=select(q)
	return render_template('admin_public_complaint.html',data=data)


@admin.route('/admin_public_reply',methods=['get','post'])
def admin_public_reply():
	if 'rs' in request.form:
		rid=request.args['rid']
		rep=request.form['rep']
		q="update public_complaint set reply='%s' where pcomplaint_id='%s'"%(rep,rid)
		update(q)
		flash("replied successfully")
		return redirect(url_for('admin.admin_public_complaint'))
	return render_template('admin_public_reply.html')



@admin.route('/admin_view_request')
def admin_view_request():
	data={}
	# q="select * from request inner join staff using (staff_id)"
	q="select * from request "
	data['view']=select(q)
	return render_template('admin_view_request.html',data=data)

@admin.route('/admin_view_complaints')
def admin_view_complaints():
	data={}
	q="select * from complaint"
	data['view']=select(q)
	return render_template('admin_view_complaints.html',data=data)

@admin.route('/admin_reply',methods=['get','post'])
def admin_reply():
	if 'rs' in request.form:
		rid=request.args['rid']
		rep=request.form['rep']
		q="update complaint set reply='%s' where complaint_id='%s'"%(rep,rid)
		update(q)
		flash("replied successfully")
		return redirect(url_for('admin.admin_view_complaints'))
	return render_template('admin_reply.html')


@admin.route('/admin_view_plans')
def admin_view_plans():
	data={}
	q="select * from plans"
	data['view']=select(q)
	return render_template('admin_view_plans.html',data=data)


@admin.route('/admin_view_transcation')
def admin_view_transcation():
	data={}
	plan_id=request.args['plans_id']
	q="select * from transcations where plans_id='%s'"%(plan_id)
	data['view']=select(q)
	return render_template('admin_view_transcation.html',data=data)






# @admin.route('/assign_plans',methods=['post','get'])
# def assign_plans():
# 	data={}
# 	if 'aas' in request.form:
# 		o=request.form['off']
# 		p=request.args['plan_id']
# 		s=request.form['sda']
# 		st=request.form['sstaff']
# 		d=request.form['dead']
# 		q="insert into assign_plans values(null,'%s','%s','%s','%s','%s','pending')"%(o,p,s,st,d)
# 		insert(q)
# 		flash("submitted successfully")
# 		return redirect(url_for('admin.admin_home'))

# 	q="select * from offices"
# 	data['offi']=select(q)

# 	q="select * from plans"
# 	data['plan']=select(q)
# 	return render_template('admin_assign_plans.html',data=data)

# @admin.route('/aview_plans')
# def aview_plans():
# 	data={}
# 	q="select * from plans inner join request using(request_id)"
# 	data['view']=select(q)
# 	return render_template('admin_view_plans.html',data=data)

# @admin.route('/adminview_plans')
# def adminview_plans():
# 	data={}
# 	q="select * from plans"
# 	data['view']=select(q)
# 	return render_template('admin_viewplans.html',data=data)




# @admin.route('/admin_manage_staff',methods=['post','get'])
# def admin_manage_staff():
# 	data={}
# 	if 'ss' in request.form:
# 		fname=request.form['fname']
# 		lname=request.form['lname']
# 		place=request.form['place']
# 		phone=request.form['phone']
# 		mail=request.form['mail']
# 		uname=request.form['uname']
# 		passw=request.form['passw']
# 		q="insert into login values(null,'%s','%s','staff')"%(uname,passw)
# 		res=insert(q)
# 		q1="insert into staff values(null,'%s','%s','%s','%s','%s','%s')"%(res,fname,lname,place,phone,mail)
# 		insert(q1)

# 	if 'action' in request.args:
# 		action=request.args['action']
# 		sid=request.args['sid']
# 	else:
# 		action=None

# 	if action=='update':
# 		q="select * from staff where staff_id='%s'"%(sid)
# 		data['up']=select(q)
# 		if 'update' in request.form:
# 			fname=request.form['fname']
# 			lname=request.form['lname']
# 			place=request.form['place']
# 			phone=request.form['phone']
# 			mail=request.form['mail']
# 			q="update staff set fname='%s',lname='%s',place='%s',phone='%s',email='%s' where staff_id='%s'"%(fname,lname,place,phone,mail,sid)
# 			update(q)
# 			return redirect(url_for('admin.admin_home'))

# 	if action=='delete':
# 		q="delete from staff where staff_id='%s'"%(sid)
# 		delete(q)
# 		return redirect(url_for('admin.admin_home'))

# 	q="select * from staff"
# 	data['view']=select(q)
# 	return render_template('admin_manage_staff.html',data=data)