pragma solidity >=0.4.22 <0.7.0;
pragma experimental ABIEncoderV2;

contract ElectionCampaign {
	struct OpeningBankBalance {
		string bankName;
		uint256 bankAmount;
	}
	struct OpeningBalance {
		uint256 cash;
		uint256 otherDeposits;
		OpeningBankBalance[] bankBalances;
	}
	struct GrossReceipt {
		uint256 cash;
		uint256 chequeAmount;
	}
	struct GrossExpenditure {
		uint256 cash;
		uint256 chequeAmount;
		uint256 draft;
	}
	// struct StarCampaigner {
	// 	string candidateName;
	// }
	struct TravelExpensesStarCampaigners {
		uint trExpId;
		string stateAndVenue;
		string dateOfMeeting;
		string[] starCampaigners;
		string modeOfTravel;
		string nameOfAircraftPayee;
		uint256 totalExpenses;
	}
	struct ElectionRecord {
		uint Id;
		string partyName;
		OpeningBalance opBal;
		GrossReceipt grRec;
		GrossExpenditure grExp;
		TravelExpensesStarCampaigners[] trExpStCam;
		bool verifiedByECAgent;
	}
	//TravelExpensesStarCampaigners[] trExpStCam;
	mapping(uint => ElectionRecord ) records;
	//mapping(uint =>  TravelExpensesStarCampaigners) trExps;
	//mapping(uint => StarCampaigner) stCms;

    //OpeningBalance[] opBals;

	function addElectionRecord(
		uint _id,
		string memory _pName,
        uint256 _c,
        uint256 _oD,
		string memory _bName,
        uint256 _bAmt
		) public {
			records[_id].Id = _id;
			records[_id].partyName = _pName;
			records[_id].opBal.cash = _c;
			records[_id].opBal.otherDeposits = _oD;
			OpeningBankBalance memory b = OpeningBankBalance({
				bankName: _bName,
				bankAmount: _bAmt
			});
			records[_id].opBal.bankBalances.push(b);
			records[_id].verifiedByECAgent = false;
	}

	function getElectionRecord(uint _id) public view returns(
		ElectionRecord memory str)
    {
		return records[_id];
	}

	function updateOpeningBankBalance(
		uint _recordId,
		string memory _bName,
        uint256 _bAmt
	) public {
		OpeningBankBalance memory b = OpeningBankBalance({
			bankName: _bName,
			bankAmount: _bAmt
		});
		records[_recordId].opBal.bankBalances.push(b);
	}

	function addGrossReceipt(
		uint _recordId,
		uint256 _c,
		uint256 _chqAmt
	) public {
		records[_recordId].grRec.cash = _c;
		records[_recordId].grRec.chequeAmount = _chqAmt;
	}

	function addGrossExpenditure(
		uint _recordId,
		uint256 _c,
		uint256 _chqAmt,
		uint256 _draft
	) public {
		records[_recordId].grExp.cash = _c;
		records[_recordId].grExp.chequeAmount = _chqAmt;
		records[_recordId].grExp.draft = _draft;
	}

	string[] starC;
	function addTravelExpensesStarCampaigners(
		uint _recordId,
		uint _trExpId,
		string memory _stVen,
		string memory _dOfMeet,
		string memory _starCampaigner1,
		string memory _mOfTr,
		string memory _nOfPayee
	) public {
		// StarCampaigner memory sc = StarCampaigner({
		// 	candidateName: _starCampaigner1
		// });
		// TravelExpensesStarCampaigners memory trExp = TravelExpensesStarCampaigners({
		// 	trExpId: _trExpId,
		// 	stateAndVenue: _stVen,
		// 	dateOfMeeting: _dOfMeet,
		// 	starCampaigners: sc,
		// 	modeOfTravel: _mOfTr,
		// 	nameOfAircraftPayee: _nOfPayee,
		// 	totalExpenses: 0
		// });
		//string[] storage starC;
		//records[_recordId].trExpStCam[_trExpId].starCampaigners;
		starC.push(_starCampaigner1);
		TravelExpensesStarCampaigners memory trExp = TravelExpensesStarCampaigners(
			_trExpId,
			_stVen,
			_dOfMeet,
			starC,
			_mOfTr,
			_nOfPayee,
			0
		);
		//starC.clear();
		delete starC;
		records[_recordId].trExpStCam.push(trExp);

		// trExps[_trExpId] = TravelExpensesStarCampaigners(
		// 	_trExpId,
		// 	_stVen,
		// 	_dOfMeet,

		// 	_mOfTr,
		// 	_nOfPayee,
		// 	0
		// );
		// stCms[] = StarCampaigner(_starCampaigner1);

		// if (records[_recordId].trExpStCam.length == 0){
		// 	return ;
		// }
		// TravelExpensesStarCampaigners storage tr = records[_recordId].trExpStCam;
		// //TravelExpensesStarCampaigners storage
		// //tr = records[_recordId].trExpStCam;
		// tr[_trExpId].trExpId = _trExpId;
		// tr[_trExpId].stateAndVenue = _stVen;
		// tr[_trExpId].dateOfMeeting = _dOfMeet;
		// tr[_trExpId].starCampaigners.push(_starCampaigner1);
		// tr[_trExpId].modeOfTravel = _mOfTr;
		// tr[_trExpId].nameOfAircraftPayee = _nOfPayee;
		// tr[_trExpId].totalExpenses = 0;

		// records[_recordId].trExpStCam.push(tr);
		// //records[_recordId].trExpStCam[]

		if (records[_recordId].trExpStCam.length == 0){
			return ;
		}

		//trExps[_trExpId].trExpId = _trExpId;
		// records[_recordId].trExpStCam[_trExpId].trExpId = _trExpId;
		// records[_recordId].trExpStCam[_trExpId].stateAndVenue = _stVen;
		// records[_recordId].trExpStCam[_trExpId].dateOfMeeting = _dOfMeet;
		// records[_recordId].trExpStCam[_trExpId].modeOfTravel = _mOfTr;
		// records[_recordId].trExpStCam[_trExpId].nameOfAircraftPayee = _nOfPayee;
		// records[_recordId].trExpStCam[_trExpId].totalExpenses = 0;
		 //records[_recordId].trExpStCam[_trExpId].starCampaigners.push(sc);
	}

	function addStarCampaignerInRecord(
		uint _recordId,
		uint _trExpId,
		string _starCampaignerName
	) public returns (uint) {
		// StarCampaigner memory sc = StarCampaigner({
		// 	candidateName: _starCampaignerName
		// });
		//records[_recordId].trExpStCam[_trExpId].starCampaigners.push(sc);

		TravelExpensesStarCampaigners storage trE = records[_recordId].trExpStCam[_trExpId-1];
		trE.starCampaigners.push(_starCampaignerName);

		return trE.starCampaigners.length;
	}



	// function addOpeningBalance(
	// 	uint _opBalId,
	// 	string memory _pName,
    //     uint256 _c,
    //     uint256 _oD,
	// 	string memory _bName,
    //     uint256 _bAmt
	// ) public {
	// 	opBals[_opBalId].openingBalanceId = _opBalId;
	// 	opBals[_opBalId].partyName = _pName;
	// 	opBals[_opBalId].cash = _c;
	// 	opBals[_opBalId].otherDeposits = _oD;
	// 	OpeningBankBalance memory b = OpeningBankBalance({
	// 		bankName: _bName,
	// 		bankAmount: _bAmt
	// 	});
	// 	opBals[_opBalId].bankBalances.push(b);
	// }

	// function getOpeningBalance(uint _id) public view returns(
	// 	OpeningBalance memory oB)
    // {
	// 	return opBals[_id];
	// }





    // function addOpeningBalance(
    //     uint _opBalId,
    //     string memory _pName,
    //     uint256 _c,
    //     uint256 _oD,
    //     string memory _bName,
    //     uint256 _bAmt
    //     ) public //returns (bool success)
    //     {
    //         opBals.push(OpeningBalance(_opBalId,_pName,_c,_oD, OpeningBankBalance(_bName,_bAmt)));
    //     }

    // function getOpeningBalance(uint id) public view returns(string, uint256, uint256, string, uint256)
    // {
    //     // return(openingBalance);
    //     return (
    //         opBals[id].partyName,
    //         opBals[id].cash,
    //         opBals[id].otherDeposits,
    //         opBals[id].bankBalance.bankName,
    //         opBals[id].bankBalance.bankAmount
    //     );
    // }

    // function getInstructor(address _address) public view returns (uint, string, string) {
    //     return (instructors[_address].age, instructors[_address].fName, instructors[_address].lName);
    // }


	//ElectionRecord[] public records;

	// mapping(uint => ElectionRecord) public records;
	// uint public recordCount;

	// function addElectionRecord(string memory _partyName, openingBalance _opBal, string memory _verifiedByECAgent) public {
	// 	recordCount++;
	// 	records[recordCount] = ElectionRecord(
	// 							recordCount,
	// 							_partyName,
	// 							_opBal,
	// 							_verifiedByECAgent
	// 							);


	// }
	// function getElectionRecord(uint _recordId) public view returns (string memory, string memory){

	// 	return (records[_recordId].candidateName, records[_recordId].partyName);
	// }

	// constructor() public {
	// 	addElectionRecord("cand1","party1","act1",123,"agenn1","date1");
	// 	addElectionRecord("cand2","party2","act2",123422,"agenn4","date33");

	// }


}