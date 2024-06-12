from flask import *
from database import *

import uuid


aeo=Blueprint('aeo',__name__)


@aeo.route('/aeo_home')
def aeo_home():
	return render_template('aeo_home.html')



@aeo.route('/aeo_send_complaint',methods=['post','get'])
def aeo_send_complaint():
	data={}
	if 'cs' in request.form:
		comp=request.form['comp']
		fi=request.files['fi']
		path="static/images/"+str(uuid.uuid4())+fi.filename
		fi.save(path)
		q="insert into complaint values(null,'%s','%s','%s','pending',curdate())"%(session['sid'],comp,path)
		insert(q)
		flash("submitted successfully")
		return redirect(url_for('aeo.aeo_send_complaint'))
	# q="select * from complaint where officer_id='%s'"%(session['oid'])
	q="select * from complaint where officer_id='%s' "%(session['sid'])
	data['view']=select(q)
	return render_template('aeo_send_complaint.html',data=data)




@aeo.route('/aeo_send_request',methods=['post','get'])
def aeo_send_request():

	data={}

	q="select * from staff where place='%s' and category='DEO' "%(session['place'])
	res=select(q)
	data['viewsss']=res

	if 'rs' in request.form:
		oid=request.form['oid']
		req=request.form['req']
		amt=request.form['amt']
		q="insert into request values(null,'%s','%s',curdate(),'pending','%s','%s','0','0','0')"%(req,amt,session['sid'],oid)
		insert(q)
		flash("shortage requested successfully")
		return redirect(url_for('aeo.aeo_send_request'))
	

	q="select * from request inner join staff on staff.staff_id=request.staff_id_aeo where staff_id_aeo='%s' and category='AEO' and place='%s' "%(session['sid'],session['place'])
	data['view']=select(q)


	return render_template('aeo_send_request.html',data=data)

@aeo.route('/aeo_request_status',methods=['post','get'])
def aeo_request_status():

	data={}	
	q="select * from request inner join staff on staff.staff_id=request.staff_id_aeo where staff_id_aeo='%s' and category='AEO' and place='%s' "%(session['sid'],session['place'])
	data['view']=select(q)
	return render_template('aeo_request_status.html',data=data)


@aeo.route('/aeo_view_plans')
def aeo_view_plans():
	data={}
	q="select * from plans"
	data['view']=select(q)
	return render_template('aeo_view_plans.html',data=data)

@aeo.route('/aeo_add_transcation',methods=['post','get'])
def aeo_add_transcation():

	data={}
	plan_id=request.args['plans_id']
	import random

	fixed_digits = 9 

	print(random.randrange(111111111, 999999999, fixed_digits))
	tranid=random.randrange(111111111, 999999999, fixed_digits)
	print("======",tranid)

	# out:
	# 271533




	q="select * from staff where place='%s' and category='DEO' "%(session['place'])
	res=select(q)
	data['viewsss']=res

	if 'ss' in request.form:
		oid=request.form['oid']
		sch=request.form['sch']
		det=request.form['det']
		pri=request.form['pri']
		qqq="select * from transcations where transcation_name='%s'"%(sch)
		ree=select(qqq)
		if ree:
			flash("Transcation already added ")
			return redirect(url_for('aeo.aeo_view_plans'))
		else:

			q="insert into transcations values(null,'%s','%s','%s','%s','%s',curdate(),'pending')"%(plan_id,tranid,sch,det,pri)
			insert(q)
			qq="update plans set staff_id_deo='%s' ,status='transaction added' where plans_id='%s'"%(oid,plan_id)
			update(qq)
			flash("Transcation added successfully")
			return redirect(url_for('aeo.aeo_view_plans'))



	return render_template('aeo_add_transcation.html',data=data)

@aeo.route('/aeo_view_transcation')
def aeo_view_transcation():
	data={}
	# plan_id=request.args['plans_id']
	q="select * from transcations inner join plans using (plans_id) where staff_id_aeo='%s'"%(session['sid'])
	data['view']=select(q)
	print("----------------",q)
	return render_template('aeo_view_transcation.html',data=data)



# @aeo.route('/aaapp_staff',methods=['post','get'])
# def aaapp_staff():
# 	data={}
# 	q="select * from staff"
# 	data['viww']=select(q)

# 	if 'action' in request.args:
# 		action=request.args['action']
		
# 		lid=request.args['lid']
# 	else:
# 		action=None

# 	if action=='approve':
# 		q="update staff set category='approved' where login_id='%s'"%(lid)
# 		update(q)
# 		q="update login set usertype='staff' where login_id='%s'"%(lid)
# 		update(q)
# 		flash("approved successfully")
# 		return redirect(url_for('aeo.aeo_home'))

# 	if action=='reject':
# 		q="update staff set category='rejected' where login_id='%s'"%(lid)
# 		update(q)
# 		q="delete from login where login_id='%s'"%(lid)
# 		delete(q)
# 		flash("rejected successfully")
# 		return redirect(url_for('aeo.aaapp_staff'))
# 	return render_template('aeo_approve_staff.html',data=data)



# @aeo.route('/aeo_viewrequest')
# def aeo_viewrequest():
# 	data={}
# 	q="select * from request inner join offices on request.office_id=offices.offices_id"
# 	data['view']=select(q)
	

# 	if 'action' in request.args:
# 		action=request.args['action']
# 		rid=request.args['rid']
# 	else:
# 		action=None

# 	if action=='accept':
# 		q="update request set status='accepted' where request_id='%s'"%(rid)
# 		update(q)
# 		flash("accepted successfully")
# 		return redirect(url_for('aeo.aeo_viewrequest'))

# 	if action=='reject':
# 		q="delete from request where request_id='%s'"%(rid)
# 		delete(q)
# 		flash("rejected successfully")
# 		return redirect(url_for('aeo.aeo_viewrequest'))
# 	return render_template('aeo_viewrequest.html',data=data)


# @aeo.route('/staff_uploadwork',methods=['post','get'])
# def staff_uploadwork():
# 	data={}
	
# 	if 'is' in request.form:
# 		plid=request.args['plan_id']
# 		im=request.files['im']
# 		path="static/images"+str(uuid.uuid4())+im.filename
# 		im.save(path)
# 		q="insert into uploadwork values(null,'%s','%s',now())"%(plid,path)
# 		insert(q)
# 		flash("submitted successfully")
# 		return redirect(url_for('aeo.staff_uploadwork'))

# 	q="select * from uploadwork"
# 	data['view']=select(q)

# 	if 'action' in request.args:
# 		action=request.args['action']
# 		sid=request.args['sid']
# 	else:
# 		action=None

# 	if action=='update':
# 		q="select * from uploadwork"
# 		data['up']=select(q)

# 		if 'update' in request.form:
# 			plid=request.args['sid']
# 			im=request.files['im']
# 			path="static/images"+str(uuid.uuid4())+im.filename
# 			im.save(path)
# 			q="update uploadwork set upload='%s' where upload_id='%s'"%(path,sid)
# 			update(q)
# 			flash("submitted successfully")
# 			return redirect(url_for('aeo.staff_home'))
# 	if action=='delete':
# 		q="delete from uploadwork where upload_id='%s'"%(sid)
# 		delete(q)
# 		flash("deleted successfully")
# 		return redirect(url_for('aeo.staff_home'))
# 	return render_template('staff_uploadwork.html',data=data)



# @aeo.route('/staff_view_plans')
# def staff_view_plans():
# 	data={}
# 	rid=request.args['rid']
# 	q="select * from plans where request_id='%s'"%(rid)
# 	data['view']=select(q)
# 	return render_template('staff_view_plans.html',data=data)


# @aeo.route('/staff_add_suggestion',methods=['post','get'])
# def staff_add_suggestion():
# 	data={}
	
# 	if 'ss' in request.form:
# 		rid=request.args['rid']
# 		sug=request.form['sug']
# 		det=request.form['det']
# 		q="insert into suggestion values(null,'%s','%s','%s')"%(rid,sug,det)
# 		insert(q)
# 		flash("submitted successfully")
# 		return redirect(url_for('aeo.staff_add_suggestion'))
# 	q="select * from suggestion"
# 	data['view']=select(q)

# 	if 'action' in request.args:
# 		action=request.args['action']
# 		sid=request.args['sid']
# 	else:
# 		action=None

# 	if action=='update':
# 		q="select * from suggestion"
# 		data['up']=select(q)

# 		if 'update' in request.form:
# 			sug=request.form['sug']
# 			det=request.form['det']
# 			q="update suggestion set suggestions='%s',details='%s' where suggestion_id='%s'"%(sug,det,sid)
# 			update(q)
# 			flash("submitted successfully")
# 			return redirect(url_for('aeo.staff_home'))
# 	if action=='delete':
# 		q="delete from suggestion where staff_add_suggestion='%s'"%(sid)
# 		delete(q)
# 		flash("deleted successfully")
# 		return redirect(url_for('aeo.staff_add_suggestion'))
# 	return render_template('staff_add_suggestion.html',data=data)




# @aeo.route('/aeo_view_transactions',methods=['post','get'])
# def aeo_view_transactions():
# 	data={}

# 	if 'search' in request.form:
# 		searchs=request.form['searchs']
# 		q="select * from request inner join offices on request.office_id=offices.offices_id like '%s'"%(searchs)
# 		res=select(q)
# 		if res:
# 			data['search']=res
# 		else:





# 			q="select * from request inner join offices on request.office_id=offices.offices_id"
# 			data['view']=select(q)
# 	return render_template('aeo_view_transactions.html',data=data)


# @aeo.route('/aeo_view_schemes',methods=['post','get'])
# def aeo_view_schemes():
# 	data={}
# 	q="select * from schemes "
# 	data['view']=select(q)
	



# 	return render_template('aeo_view_schemes.html',data=data)