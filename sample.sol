pragma solidity >= 0.5.0 < 0.7.0;
contract government{
 struct transactionss{
	// State variables
	 uint transcation_id;
	 uint plans_id;
	 string transcationid;
	 string transcation_name;
	 string details;
	 string amount;
	 string date;
	 string status;

}



transactionss []p;



function add_transactionss(uint transcation_id,uint plans_id, string memory transcationid, string memory transcation_name,string memory details,string memory amount,string memory date,
	string memory status) public{
	transactionss memory p1=transactionss(transcation_id,plans_id,transcationid,transcation_name,details,amount,date,status);
	p.push(p1);
}

}
