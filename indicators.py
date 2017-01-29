import pymongo

VOTE_BLANC = "Blanc"
VOTE_REPUBLICAIN = "Trump"
VOTE_DEMOCRATE = "Clinton"

result_by_state_nb_of_votes = "nb_of_vote"
result_by_state_candidate = "candidate"
result_by_state_name = "state_name"
state_nb_subscriptors  = "nb_subscriptors"
state_nb_electors = "nb_electors"

id = "_id"

def get_indicators(collection_result_by_state, collection_state):
	result_by_state = collection_result_by_state.find({},{result_by_state_nb_of_votes:"1","_id":"0",result_by_state_candidate:"1", result_by_state_name:"1"})

	nb_of_votes = 0
	nb_of_votes_republicains = 0
	nb_of_votes_democrates = 0
	nb_of_suffrages = 0
	nb_of_votes_autres = 0
	Abstention_dict = {}

	for result in result_by_state:
		if(result[result_by_state_candidate]  != VOTE_BLANC):
			nb_of_suffrages = nb_of_suffrages + int(result[result_by_state_nb_of_votes])

		if (result[result_by_state_candidate] == VOTE_REPUBLICAIN):
			nb_of_votes_republicains = nb_of_votes_republicains + int(result[result_by_state_nb_of_votes])
		elif (result[result_by_state_candidate] == VOTE_DEMOCRATE):
			nb_of_votes_democrates = nb_of_votes_democrates + int(result[result_by_state_nb_of_votes])
		elif(result[result_by_state_candidate] != VOTE_BLANC ):
			nb_of_votes_autres = nb_of_votes_autres + int(result[result_by_state_nb_of_votes])

		nb_of_votes = nb_of_votes + int(result[result_by_state_nb_of_votes])



		key = result[result_by_state_name]
		Abstention_dict[key] = Abstention_dict.get(key, 0) + int(result[result_by_state_nb_of_votes])
	#print(Abstention_dict)
	nb_Abstention = 0
	big_elector = {}
	for k, v in Abstention_dict.items():
		# get number abstention
		state = collection_state.find_one({result_by_state_name:k},{state_nb_electors:"1","_id":"0",state_nb_subscriptors:"1"})
		nb_Abstention = nb_Abstention + (state[state_nb_subscriptors] - v)
		# get big elector numbers
		winner = collection_result_by_state.find({result_by_state_name:k},
	                                         {result_by_state_candidate:"1",
	                                         result_by_state_name:"1",
	                                         "_id":0,
	                                         result_by_state_nb_of_votes:"1"}).sort([(result_by_state_nb_of_votes,pymongo.DESCENDING)]).limit(1)

		for candidate_winner in winner: # should be unique
			c = candidate_winner[result_by_state_candidate]
			big_elector[c] = big_elector.get(c, 0) + int(state[state_nb_electors])

	#print(big_elector)

	return nb_of_votes, nb_of_suffrages, nb_Abstention, nb_of_votes_republicains, nb_of_votes_democrates, nb_of_votes_autres,big_elector

