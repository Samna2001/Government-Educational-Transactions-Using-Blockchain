from flask import *
from database import *


public=Blueprint('public',__name__)


@public.route('/')
def index():
	return render_template('index.html')


@public.route('/login',methods=['post','get'])
def login():
	if 'us' in request.form:
		uname=request.form['uname']
		passw=request.form['passw']
		q="select * from login where username='%s' and password='%s'"%(uname,passw)
		val=select(q)
		if val:
			session['lid']=val[0]['login_id']
			if val[0]['usertype']=='admin':
				flash("login successfully")
				return redirect(url_for('admin.admin_home'))


			# elif val[0]['usertype']=='staff':
			# 	r="select * from staff where login_id='%s'"%(session['lid'])
			# 	res=select(r)
			# 	if res:
			# 		session['sid']=res[0]['staff_id']
			# 		flash("login successfully")
			# 		return redirect(url_for('staff.staff_home'))



			# elif val[0]['usertype']=='office':
			# 	r="select * from offices where login_id='%s'"%(session['lid'])
			# 	res1=select(r)
			# 	if res1:
			# 		session['oid']=res1[0]['offices_id']
			# 		print(session['oid'],'---------------------------------------------')
			# 		flash("login successfully")
			# 		return redirect(url_for('office.office_home'))
			# elif val[0]['usertype']=='PSGE':
			# 	flash("login successfully")
			# 	return redirect(url_for('psge.psge_home'))


			elif val[0]['usertype']=='RDD':

				r4="select * from staff where login_id='%s' and category='RDD'"%(session['lid'])
				res4=select(r4)
				print(res4)
				if res4:
					session['sid_rdd']=res4[0]['staff_id']
					session['place']=res4[0]['place']
					flash("login successfully")
				return redirect(url_for('rdd.rdd_home'))


			elif val[0]['usertype']=='AD':
				r3="select * from staff where login_id='%s' and category='AD'"%(session['lid'])
				res3=select(r3)
				print(res3)
				if res3:
					session['sid_ad']=res3[0]['staff_id']
					session['place']=res3[0]['place']
					flash("login successfully")
				return redirect(url_for('ad.ad_home'))

	



			elif val[0]['usertype']=='DDE':
				r2="select * from staff where login_id='%s' and category='DDE'"%(session['lid'])
				res2=select(r2)
				print(res2)
				if res2:
					session['sid_dde']=res2[0]['staff_id']
					session['place']=res2[0]['place']
					flash("login successfully")
					return redirect(url_for('dde.dde_home'))



			elif val[0]['usertype']=='DEO':
				r1="select * from staff where login_id='%s' and category='DEO'"%(session['lid'])
				res1=select(r1)
				print(res1)
				if res1:
					session['sid_deo']=res1[0]['staff_id']
					session['place']=res1[0]['place']
					flash("login successfully")
					return redirect(url_for('deo.deo_home'))

			elif val[0]['usertype']=='AEO':
				r="select * from staff where login_id='%s' and category='AEO'"%(session['lid'])
				res=select(r)
				print(res)
				if res:
					session['sid']=res[0]['staff_id']
					session['place']=res[0]['place']
					flash("login successfully")
					return redirect(url_for('aeo.aeo_home'))
	
	return render_template('login.html')

# @public.route('/office_registration',methods=['post','get'])
# def office_registration():
# 	if 'os' in request.form:
# 		o=request.form['off']
# 		plac=request.form['plac']
# 		phn=request.form['phn']
# 		mail=request.form['mail']
# 		uname=request.form['uname']
# 		pwd=request.form['pwd']
# 		q="select * from offices inner join login using (login_id) where email='%s'"%(mail)
# 		res=select(q)
# 		if res:
# 			flash("already successfully")
# 			return redirect(url_for('public.office_registration'))
# 		else:
# 			q="insert into login values(null,'%s','%s','office')"%(uname,pwd)
# 			res=insert(q)
# 			q1="insert into offices values(null,'%s','%s','%s','%s','%s')"%(res,o,plac,phn,mail)
# 			insert(q1)
# 			print("----------",q1)
# 			flash("submitted successfully")
# 			return redirect(url_for('public.office_registration'))

# 	return render_template('office_registration.html')



@public.route('/signup',methods=['post','get'])
def signup():
	if 'login' in request.form:
		f=request.form['fname']
		l=request.form['lname']
		m=request.form['e']
		pla=request.form['pla']
		u=request.form['uname']
		p=request.form['pwd']
		c=request.form['cat']
		phn=request.form['phn']

		qq="select * from login inner join staff using (login_id) where login.`password`='%s' or staff.email='%s'"%(p,m)
		re=select(qq)
		print("-------",qq)

		if re:
			flash("Already Exist! Please try new one")
			return redirect(url_for('public.login'))
		else:
			qi="select * from staff where place='%s' and category='%s'"%(pla,c)
			ri=select(qi)
			print("-------",qi)
			if ri:
				flash("Already Exist! ")
				return redirect(url_for('public.login'))
			else:
				q="insert into login values(null,'%s','%s','pending')"%(u,p)
				res=insert(q)
				print("-------",q)
				q1="insert into staff values(null,'%s','%s','%s','%s','%s','%s','%s')"%(res,f,l,m,c,phn,pla)
				insert(q1)
				print("-------",q1)

				flash("submitted successfully")
				return redirect(url_for('public.login'))


			
	return render_template('officer_register.html')


# @public.route('/view_plans')
# def view_plans():
# 	data={}
# 	q="select * from plans inner join request using(request_id)"
# 	data['view']=select(q)
# 	return render_template('view_plans.html',data=data)


# @public.route('/view_transactions',methods=['post','get'])
# def view_transactions():
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
# 	return render_template('view_transactions.html',data=data)




@public.route('/public_complaint',methods=['post','get'])
def public_complaint():
	data={}
	if 'cs' in request.form:
		comp=request.form['comp']
		usern=request.form['usern']

		q="insert into public_complaint values(null,'%s','%s',curdate(),'pending')"%(comp,usern)
		insert(q)
		flash("submitted successfully")
		return redirect(url_for('public.public_complaint'))
	q="select * from public_complaint "
	data['view']=select(q)
	return render_template('public_complaint.html',data=data)



@public.route('/public_view_transcation')
def public_view_transcation():
	data={}
	q="select * from transcations inner join plans using(plans_id) "
	data['view']=select(q)
	return render_template('public_view_transcation.html',data=data)


# @public.route('/staff_view_officess')
# def staff_view_officess():
# 	data={}
# 	q="select * from offices"
# 	data['view']=select(q)
# 	return render_template('staff_view_officess.html',data=data)