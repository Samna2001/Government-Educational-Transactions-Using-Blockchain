from flask import *
from database import *
from deo import *


dde=Blueprint('dde',__name__)


@dde.route('/dde_home')
def dde_home():
	return render_template('dde_home.html')



@dde.route('/dde_request_verify')
def dde_request_verify():
	data={}
	q="select * from request inner join staff on staff.staff_id=request.staff_id_dde where staff_id_dde='%s' and category='DDE' and place='%s' "%(session['sid_dde'],session['place'])
	data['view']=select(q)
	print("---------------",q)
	

	if 'action' in request.args:
		action=request.args['action']
		rid=request.args['rid']
	else:
		action=None

	if action=='accept':
		q="update request set status='verified and forward to AD' where request_id='%s'"%(rid)
		update(q)
		flash("accepted successfully")
		return redirect(url_for('dde.dde_request_verify'))

	if action=='reject':
		q="update request set status='Declined' where request_id='%s'"%(rid)
		update(q)

		flash("rejected successfully")
		return redirect(url_for('dde.dde_request_verify'))
	return render_template('dde_request_verify.html',data=data)


@dde.route('/dde_view_plans')
def dde_view_plans():
	data={}
	q="select * from plans where staff_id_dde='%s'"%(session['sid_dde'])
	data['view']=select(q)
	print("---------------",q)


	if 'action' in request.args:
		action=request.args['action']
		rid=request.args['rid']
	else:
		action=None

	if action=='accept':
		q="update plans set status='accepted' where plans_id='%s'"%(rid)
		update(q)
		flash("accepted successfully")
		return redirect(url_for('dde.dde_view_plans'))

	if action=='reject':
		q="update plans set status='rejected' where plans_id='%s'"%(rid)
		update(q)
		flash("rejected successfully")
		return redirect(url_for('dde.dde_view_plans'))


	return render_template('dde_view_plans.html',data=data)

@dde.route('/dde_assign_deo',methods=['post','get'])
def dde_assign_deo():

	data={}

	plans_id=request.args['plans_id']

	# q="select * from staff where place='%s' and category='DDE' "%(session['place'])
	q="select * from staff where  category='DEO' "
	res=select(q)
	data['viewsss']=res

	if 'rs' in request.form:
		oid=request.form['oid']
		q="update plans set status='approve and forward to deo', staff_id_deo='%s'  where plans_id='%s'"%(oid,plans_id)
		print("-----------",q)
		update(q)
		flash("forwarded successfully")
		return redirect(url_for('dde.dde_view_plans'))
	

	return render_template('dde_assign_deo.html',data=data)

@dde.route('/dde_view_transcation',methods=['post','get'])
def dde_view_transcation():
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
	return render_template('dde_view_transcation.html',data=data)





@dde.route('/dde_assign_ad',methods=['post','get'])
def dde_assign_ad():

	data={}

	rid=request.args['rid']

	# q="select * from staff where place='%s' and category='DDE' "%(session['place'])
	q="select * from staff where  category='AD' "
	res=select(q)
	data['viewsss']=res

	if 'rs' in request.form:
		oid=request.form['oid']
		q="update request set status='verified and forward to AD', staff_id_ad='%s'  where request_id='%s'"%(oid,rid)
		print("-----------",q)
		update(q)
		flash("forwarded successfully")
		return redirect(url_for('dde.dde_request_verify'))
	

	return render_template('dde_assign_ad.html',data=data)












# @dde.route('/dapp_staff',methods=['post','get'])
# def dapp_staff():
# 	data={}
# 	q="select * from staff"
# 	data['vi']=select(q)

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
# 		return redirect(url_for('dde.dde_home'))

# 	if action=='reject':
# 		q="update staff set category='rejected' where login_id='%s'"%(lid)
# 		update(q)
# 		q="delete from login where login_id='%s'"%(lid)
# 		delete(q)
# 		flash("rejected successfully")
# 		return redirect(url_for('dde.dde_home'))
# 	return render_template('dde_approve_staff.html',data=data)
# @dde.route('/ddapp_verify_req',methods=['post','get'])
# def ddapp_verify_req():
# 	data={}
# 	q="select * from request inner join plans using(request_id)"
# 	data['view']=select(q)

# 	if 'action' in request.args:
# 		action=request.args['action']
		
# 		lid=request.args['lid']
# 	else:
# 		action=None

# 	if action=='approve':
# 		q="update request set status='Approve' where request_id='%s'"%(lid)
# 		update(q)
# 		flash("approved successfully")
# 		return redirect(url_for('dde.ddapp_verify_req'))

# 	if action=='reject':
# 		q="update request set status='rejected' where request_id='%s'"%(lid)
# 		update(q)
# 		flash("rejected successfully")
# 		return redirect(url_for('dde.ddapp_verify_req'))
# 	return render_template('ddapp_verify_req.html',data=data)



# @dde.route('/dde_view_transactions',methods=['post','get'])
# def dde_view_transactions():
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
# 	return render_template('dde_view_transactions.html',data=data)


# @dde.route('/dde_view_schemes',methods=['post','get'])
# def dde_view_schemes():
# 	data={}
# 	q="select * from schemes "
# 	data['view']=select(q)
	



# 	return render_template('dde_view_schemes.html',data=data)