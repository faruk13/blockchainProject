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
	mapping(uint => ElectionRecord ) records;

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
		delete starC;
		records[_recordId].trExpStCam.push(trExp);
		if (records[_recordId].trExpStCam.length == 0){
			return ;
		}
	}

	function addStarCampaignerInRecord(
		uint _recordId,
		uint _trExpId,
		string _starCampaignerName
	) public returns (uint) {

		TravelExpensesStarCampaigners storage trE = records[_recordId].trExpStCam[_trExpId-1];
		trE.starCampaigners.push(_starCampaignerName);

		return trE.starCampaigners.length;
	}

}
