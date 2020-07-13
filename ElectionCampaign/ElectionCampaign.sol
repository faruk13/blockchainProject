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
	struct ExpensesOnMediaAd {
		string state;
		string nameOfPayee;
		string nameOfMedia;
		string dateOfTelecast;
		uint256 amount;
	}
	struct ExpensesOnPublicityMaterial {
		string state;
		string nameOfRegion;
		string detailsOfItems;
		uint256 amount;
	}
	struct ExpensesOnPublicMeetings {
		string stateAndVenue;
		string dateOfMeeting;
		string detailsOfItems;
		uint256 amount;
	}
	struct ElectionRecord {
		uint Id;
		string electionName;
		string unitHQ;
		string partyName;
		OpeningBalance opBal;
		GrossReceipt grRec;
		GrossExpenditure grExp;
		TravelExpensesStarCampaigners[] trExpStCam;
		ExpensesOnMediaAd[] expMedia;
		ExpensesOnPublicityMaterial[] expPubMat;
		ExpensesOnPublicMeetings[] expPubMeet;
		bool verifiedByECAgent;
	}
	mapping(uint => ElectionRecord ) records;
	uint256 recordCount = 0;

	function addElectionRecord(
		uint _id,
		string memory _pName,
		string memory _electionName,
		string memory _unitHQ,
        uint256 _c,
        uint256 _oD,
		string memory _bName,
        uint256 _bAmt
		) public {
			records[_id].Id = _id;
			records[_id].partyName = _pName;
			records[_id].electionName = _electionName;
			records[_id].unitHQ = _unitHQ;
			records[_id].opBal.cash = _c;
			records[_id].opBal.otherDeposits = _oD;
			OpeningBankBalance memory b = OpeningBankBalance({
				bankName: _bName,
				bankAmount: _bAmt
			});
			records[_id].opBal.bankBalances.push(b);
			records[_id].verifiedByECAgent = false;

			recordCount++;
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

	function addExpensesOnMediaAd(
		uint _recordId,
		string _state,
		string _nOfPayee,
		string _nOfMedia,
		string _dOfTele,
		uint256 _amt
	) public {
		ExpensesOnMediaAd memory expM = ExpensesOnMediaAd(
			_state,
			_nOfPayee,
			_nOfMedia,
			_dOfTele,
			_amt
		);
		records[_recordId].expMedia.push(expM);
	}

	function addExpensesOnPublicityMaterial(
		uint _recordId,
		string _state,
		string _nOfRegion,
		string _detOfItems,
		uint256 _amt
	) public {
		ExpensesOnPublicityMaterial memory expPM = ExpensesOnPublicityMaterial(
			_state,
			_nOfRegion,
			_detOfItems,
			_amt
		);
		records[_recordId].expPubMat.push(expPM);
	}

	function addExpensesOnPublicMeetings(
		uint _recordId,
		string _state,
		string _dOfMeet,
		string _detOfItems,
		uint256 _amt
	) public {
		ExpensesOnPublicMeetings memory expPMeet = ExpensesOnPublicMeetings(
			_state,
			_dOfMeet,
			_detOfItems,
			_amt
		);
		records[_recordId].expPubMeet.push(expPMeet);
	}

	function getERecCount()
	public view returns(uint256)
    {
		return recordCount;
	}

	function getERecPartyName(uint _id)
	public view returns(string)
    {
		return records[_id].partyName;
	}

	function getERecElectionName(uint _id)
	public view returns(string)
    {
		return records[_id].electionName;
	}

	function getERecUnitHQ(uint _id)
	public view returns(string)
    {
		return records[_id].unitHQ;
	}

	function getERecOpeningBalance(uint _id)
	public view returns(OpeningBalance)
    {
		return records[_id].opBal;
	}

	function getERecGrossReceipt(uint _id)
	public view returns(GrossReceipt)
    {
		return records[_id].grRec;
	}

	function getERecGrossExpenditure(uint _id)
	public view returns(GrossExpenditure)
    {
		return records[_id].grExp;
	}

	function getERecTravelExpensesStarCampaigners(uint _id)
	public view returns(TravelExpensesStarCampaigners[])
    {
		return records[_id].trExpStCam;
	}

	function getERecExpensesOnMediaAd(uint _id)
	public view returns(ExpensesOnMediaAd[])
    {
		return records[_id].expMedia;
	}

	function getERecExpensesOnPublicityMaterial(uint _id)
	public view returns(ExpensesOnPublicityMaterial[])
    {
		return records[_id].expPubMat;
	}

	function getERecExpensesOnPublicMeetings(uint _id)
	public view returns(ExpensesOnPublicMeetings[])
    {
		return records[_id].expPubMeet;
	}

	function getERecVerifiedByECAgent(uint _id)
	public view returns(bool)
    {
		return records[_id].verifiedByECAgent;
	}

}
