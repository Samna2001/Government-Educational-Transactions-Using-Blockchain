from flask import *
from database import *

import json
from web3 import Web3, HTTPProvider

# truffle development blockchain address
blockchain_address = 'http://127.0.0.1:9545'
# Client instance to interact with the blockchain
web3 = Web3(HTTPProvider(blockchain_address))
# Set the default account (so we don't need to set the "from" for every transaction call)
web3.eth.defaultAccount = web3.eth.accounts[0]
compiled_contract_path = 'X:/e-government/node_modules/.bin/build/contracts/government.json'
# Deployed contract address (see `migrate` command output: `contract address`)
deployed_contract_address = '0x369D940AbD04cADbf214eAd32BAa9eE3B9E37e33'
syspath=r"X:\e-government\static\\"


deo=Blueprint('deo',__name__)


@deo.route('/deo_home')
def deo_home():
	return render_template('deo_home.html')

# @deo.route('/ddapp_staff',methods=['post','get'])
# def ddapp_staff():
# 	data={}
# 	q="select * from staff"
# 	data['viee']=select(q)

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
# 		return redirect(url_for('deo.deo_home'))

# 	if action=='reject':
# 		q="update staff set category='rejected' where login_id='%s'"%(lid)
# 		update(q)
# 		q="delete from login where login_id='%s'"%(lid)
# 		delete(q)
# 		flash("rejected successfully")
# 		return redirect(url_for('deo.deo_home'))
# 	return render_template('deo_approve_staff.html',data=data)

@deo.route('/deo_view_plans')
def deo_view_plans():
	data={}
	q="select * from plans where staff_id_deo='%s'"%(session['sid_deo'])
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
		return redirect(url_for('deo.deo_view_plans'))

	if action=='reject':
		q="update plans set status='rejected' where plans_id='%s'"%(rid)
		update(q)
		flash("rejected successfully")
		return redirect(url_for('deo.deo_view_plans'))

	return render_template('deo_view_plans.html',data=data)


@deo.route('/deo_assign_aeo',methods=['post','get'])
def deo_assign_aeo():

	data={}

	plans_id=request.args['plans_id']

	# q="select * from staff where place='%s' and category='DDE' "%(session['place'])
	q="select * from staff where  category='AEO' "
	res=select(q)
	data['viewsss']=res

	if 'rs' in request.form:
		oid=request.form['oid']
		q="update plans set status='approve and forward to aeo', staff_id_aeo='%s'  where plans_id='%s'"%(oid,plans_id)
		print("-----------",q)
		update(q)
		flash("forwarded successfully")
		return redirect(url_for('deo.deo_view_plans'))
	

	return render_template('deo_assign_aeo.html',data=data)


	
@deo.route('/deo_view_transcation',methods=['post','get'])
def deo_view_transcation():
	data={}
	q="select *,transcations.status as tstatus from transcations inner join plans using (plans_id) where staff_id_deo='%s'"%(session['sid_deo'])
	data['view']=select(q)
	print("-------------",q)

	if 'action' in request.args:
		action=request.args['action']
		transcation_id=request.args['transcation_id']
	else:
		action=None

	if action=='verify':

		q="select * from transcations  where transcation_id='%s'"%(transcation_id)
		res=select(q)
		if res:
			with open(compiled_contract_path) as file:
				contract_json = json.load(file)  # load contract info as JSON
				contract_abi = contract_json['abi']  # fetch contract's abi - necessary to call its functions
			contract = web3.eth.contract(address=deployed_contract_address, abi=contract_abi)
			message = contract.functions.add_transactionss(int(res[0]['transcation_id']),res[0]['plans_id'], res[0]['transcationid'], res[0]['transcation_name'], res[0]['details'], res[0]['amount'], res[0]['date'], 'verified').transact()
			# return redirect(url_for('deo.deo_approve_plan'))
			q="update transcations set status='deo_verify' where transcation_id='%s'"%(transcation_id)
			update(q)
			q="update plans set status='deo_verify' where plans_id='%s'"%(res[0]['plans_id'])
			update(q)
			flash("verified successfully")
			return redirect(url_for('deo.deo_home'))

	# if action=='reject':
	# 	q="update request set status='rejected' where request_id='%s'"%(lid)
	# 	update(q)
	# 	flash("rejected successfully")
	# 	return redirect(url_for('deo.deo_home'))
	return render_template('deo_view_transcation.html',data=data)






@deo.route('/deo_request_verify')
def deo_request_verify():
	data={}
	q="select * from request inner join staff on staff.staff_id=request.staff_id_deo where staff_id_deo='%s' and category='DEO' and place='%s' "%(session['sid_deo'],session['place'])
	data['view']=select(q)
	print("---------------",q)
	

	if 'action' in request.args:
		action=request.args['action']
		rid=request.args['rid']
	else:
		action=None

	if action=='accept':
		q="update request set status='accepted' where request_id='%s'"%(rid)
		update(q)
		flash("accepted successfully")
		return redirect(url_for('deo.deo_request_verify'))

	if action=='reject':
		q="update request set status='Declined' where request_id='%s'"%(rid)
		update(q)

		flash("rejected successfully")
		return redirect(url_for('deo.deo_request_verify'))
	return render_template('deo_request_verify.html',data=data)



@deo.route('/deo_assign_dde',methods=['post','get'])
def deo_assign_dde():

	data={}

	request_id=request.args['request_id']

	# q="select * from staff where place='%s' and category='DDE' "%(session['place'])
	q="select * from staff where  category='DDE' "
	res=select(q)
	data['viewsss']=res

	if 'rs' in request.form:
		oid=request.form['oid']
		q="update request set status='forward_to_dde', staff_id_dde='%s'  where request_id='%s'"%(oid,request_id)
		print("-----------",q)
		update(q)
		flash("forwarded successfully")
		return redirect(url_for('deo.deo_request_verify'))
	

	return render_template('deo_assign_dde.html',data=data)


# @deo.route('/deo_view_transactions',methods=['post','get'])
# def deo_view_transactions():
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
# 	return render_template('deo_view_transactions.html',data=data)


# @deo.route('/deo_view_schemes',methods=['post','get'])
# def deo_view_schemes():
# 	data={}
# 	q="select * from schemes "
# 	data['view']=select(q)
	



# 	return render_template('deo_view_schemes.html',data=data)



# @deo.route('/deo_viewrequest')
# def deo_viewrequest():
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
# 		return redirect(url_for('deo.deo_viewrequest'))

# 	if action=='reject':
# 		q="delete from request where request_id='%s'"%(rid)
# 		delete(q)
# 		flash("rejected successfully")
# 		return redirect(url_for('deo.deo_viewrequest'))
# 	return render_template('deo_viewrequest.html',data=data)