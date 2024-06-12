from flask import *
from database import *
from deo import *


ad=Blueprint('ad',__name__)


@ad.route('/ad_home')
def ad_home():
	return render_template('ad_home.html')




@ad.route('/ad_view_plans')
def ad_view_plans():
	data={}
	q="select * from plans where staff_id_ad='%s'"%(session['sid_ad'])
	data['view']=select(q)


	if 'action' in request.args:
		action=request.args['action']
		rid=request.args['rid']
	else:
		action=None

	if action=='accept':
		q="update plans set status='accepted' where plans_id='%s'"%(rid)
		update(q)
		flash("accepted successfully")
		return redirect(url_for('ad.ad_view_plans'))

	if action=='reject':
		q="update plans set status='rejected' where plans_id='%s'"%(rid)
		update(q)
		flash("rejected successfully")
		return redirect(url_for('ad.ad_view_plans'))



	return render_template('ad_view_plans.html',data=data)





@ad.route('/ad_assign_rdd',methods=['post','get'])
def ad_assign_rdd():

	data={}

	plans_id=request.args['plans_id']

	# q="select * from staff where place='%s' and category='DDE' "%(session['place'])
	q="select * from staff where  category='DDE' "
	res=select(q)
	data['viewsss']=res

	if 'rs' in request.form:
		oid=request.form['oid']
		q="update plans set status='approve and forward to DDE', staff_id_dde='%s'  where plans_id='%s'"%(oid,plans_id)
		print("-----------",q)
		update(q)
		flash("forwarded successfully")
		return redirect(url_for('ad.ad_view_plans'))
	

	return render_template('ad_assign_dde.html',data=data)

@ad.route('/ad_view_transcation',methods=['post','get'])
def ad_view_transcation():
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
	return render_template('ad_view_transcation.html',data=data)



@ad.route('/ad_request_verify')
def ad_request_verify():
	data={}
	q="select * from request inner join staff on staff.staff_id=request.staff_id_ad where staff_id_ad='%s' and category='AD' and place='%s' "%(session['sid_ad'],session['place'])
	data['view']=select(q)
	print("---------------",q)
	

	if 'action' in request.args:
		action=request.args['action']
		rid=request.args['rid']
	else:
		action=None

	if action=='accept':
		q="update request set status='verified and forward to RDD' where request_id='%s'"%(rid)
		update(q)
		flash("accepted successfully")
		return redirect(url_for('ad.ad_request_verify'))

	if action=='reject':
		q="update request set status='Declined' where request_id='%s'"%(rid)
		update(q)

		flash("rejected successfully")
		return redirect(url_for('ad.ad_request_verify'))
	return render_template('ad_request_verify.html',data=data)




@ad.route('/ad_assign_rdd_request',methods=['post','get'])
def ad_assign_rdd_request():

	data={}

	rid=request.args['rid']

	# q="select * from staff where place='%s' and category='DDE' "%(session['place'])
	q="select * from staff where  category='RDD' "
	res=select(q)
	data['viewsss']=res

	if 'rs' in request.form:
		oid=request.form['oid']
		q="update request set status='approve and forward to RDD', staff_id_rdd='%s'  where request_id='%s'"%(oid,rid)
		print("-----------",q)
		update(q)
		flash("forwarded successfully")
		return redirect(url_for('ad.ad_view_plans'))
	

	return render_template('ad_assign_rdd.html',data=data)







# @ad.route('/ad_approve_staff',methods=['post','get'])
# def ad_approve_staff():
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
# 		return redirect(url_for('ad.ad_home'))

# 	if action=='reject':
# 		q="update staff set category='rejected' where login_id='%s'"%(lid)
# 		update(q)
# 		q="delete from login where login_id='%s'"%(lid)
# 		delete(q)
# 		flash("rejected successfully")
# 		return redirect(url_for('ad.ad_home'))
# 	return render_template('ad_approve_staff.html',data=data)


# @ad.route('/ad_view_transactions',methods=['post','get'])
# def ad_view_transactions():
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
# 	return render_template('ad_view_transactions.html',data=data)


# @ad.route('/ad_view_schemes',methods=['post','get'])
# def ad_view_schemes():
# 	data={}
# 	q="select * from schemes "
# 	data['view']=select(q)
	



# 	return render_template('ad_view_schemes.html',data=data)