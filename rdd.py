from flask import *
from database import *
from deo import *
import uuid

rdd=Blueprint('rdd',__name__)


@rdd.route('/rdd_home')
def rdd_home():
	return render_template('rdd_home.html')


@rdd.route('/rdd_add_plans',methods=['post','get'])
def rdd_add_plans():
	data={}
	import random

	fixed_digits = 9 

	print(random.randrange(111111111, 999999999, fixed_digits))
	tranid=random.randrange(111111111, 999999999, fixed_digits)
	print("======",tranid)


	q="select * from staff where  category='AD' "
	res=select(q)
	data['viewsss']=res


	q="select * from plans where staff_id_rdd='%s'"%(session['sid_rdd'])
	data['view']=select(q)


	if 'ss' in request.form:

		oid=request.form['oid']
		pl=request.form['pl']
		desc=request.form['desc']
		im=request.files['plan_file']
		path="static/images/"+str(uuid.uuid4())+im.filename
		im.save(path)
		q="insert into plans values(null,'%s','%s','%s','%s','pending','%s','%s','0','0','0')"%(tranid,pl,desc,path,session['sid_rdd'],oid)
		insert(q)
		print("----------------",q)
		flash("submitted successfully")
		return redirect(url_for('rdd.rdd_add_plans'))

	return render_template('rdd_add_plans.html',data=data)







@rdd.route('/rdd_view_plans')
def rdd_view_plans():
	data={}
	q="select * from plans where staff_id_rdd='%s'"%(session['sid_rdd'])
	data['view']=select(q)

	return render_template('rdd_view_plans.html',data=data)


@rdd.route('/rdd_view_transcation',methods=['post','get'])
def rdd_view_transcation():
	data={}
	plans_id=request.args['plans_id']

	# q="select * from transcations inner join plans using (plans_id) where staff_id_dde='%s'"%(session['sid_dde'])
	# data['view']=select(q)
	# print("-------------",q)


	with open(compiled_contract_path) as file:
		contract_json = json.load(file)  # load contract info as JSON
		contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
	contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
	blocknumber = web3.eth.get_block_number()
	res = []
	try:
		for i in range(blocknumber, 0, -1):
			a = web3.eth.get_transaction_by_block(i, 0)
			decoded_input = contract.decode_function_input(a['input'])
			print(decoded_input)
			if str(decoded_input[0]) == "<Function add_transactionss(uint256,uint256,string,string,string,string,string,string)>":
				if int(decoded_input[1]['plans_id']) == int(plans_id):
					res.append(decoded_input[1])
	except Exception as e:
		print("", e)
	data['viewsss']=res
	print("/////////",res)
	# if res:
	# 	q1="SELECT * FROM transcations where plans_id='%s'"%(res[0]['plans_id'])+++
	# 	data['viewsss']=select(q1)
	# 	print("-------------",q1)
	return render_template('rdd_view_transcation.html',data=data)



@rdd.route('/rdd_request_verify')
def rdd_request_verify():
	data={}
	q="select * from request inner join staff on staff.staff_id=request.staff_id_rdd where staff_id_rdd='%s' and category='RDD' and place='%s' "%(session['sid_rdd'],session['place'])
	data['view']=select(q)
	print("---------------",q)
	

	if 'action' in request.args:
		action=request.args['action']
		rid=request.args['rid']
	else:
		action=None

	if action=='approve':
		q="update request set status='sanctioned' where request_id='%s'"%(rid)
		update(q)
		flash("sanctioned successfully")
		return redirect(url_for('rdd.rdd_request_verify'))

	if action=='reject':
		q="update request set status='rejected' where request_id='%s'"%(rid)
		update(q)
		flash("rejected successfully")
		return redirect(url_for('rdd.rdd_request_verify'))
	return render_template('rdd_request_verify.html',data=data)







# @rdd.route('/rapp_staff',methods=['post','get'])
# def rapp_staff():
# 	data={}
# 	q="select * from staff"
# 	data['v']=select(q)

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
# 		return redirect(url_for('rdd.rdd_home'))

# 	if action=='reject':
# 		q="update staff set category='rejected' where login_id='%s'"%(lid)
# 		update(q)
# 		q="delete from login where login_id='%s'"%(lid)
# 		delete(q)
# 		flash("rejected successfully")
# 		return redirect(url_for('rdd.rdd_home'))
# 	return render_template('rdd_approve_staff.html',data=data)


# @rdd.route('/rdd_view_transactions',methods=['post','get'])
# def rdd_view_transactions():
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
# 	return render_template('rdd_view_transactions.html',data=data)


# @rdd.route('/rdd_view_schemes',methods=['post','get'])
# def rdd_view_schemes():
# 	data={}
# 	q="select * from schemes "
# 	data['view']=select(q)
	



# 	return render_template('rdd_view_schemes.html',data=data)