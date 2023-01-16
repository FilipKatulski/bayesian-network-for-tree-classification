import pysmile

pysmile.License(
	# COPY LICENCE HERE
)


class BayesNetwork:
	def __init__(self, path_to_network_file) -> None:
		self.net = self.load_network(path = path_to_network_file)
		self.current_state = self.load_current_state(self.net)

	def load_network(self, path: str) -> pysmile.Network:
		net = pysmile.Network()
		net.read_file(path)
		net.update_beliefs()
		return net 

	def load_current_state(self, network: pysmile.Network) -> dict:
		"""
		Loads the current state of the network, returns in a form of dict of dicts.
		The shape created by the function:
		data = {
        	'rodzaj_lisci':
            	{
                	'igly':10,
                	'blaszki':40,
                	'łuski':50
            	},
        	'kolor kory': {
            	'bialy':10,
            	'czarny':30,
            	'brazowy':60
            	}
    	}
		"""
		data = {}
		node_ids = network.get_all_node_ids() 
		for id in node_ids:
			# print(id, network.get_node_value(id))
			sub_data = {}
			for i in range(0, len(network.get_node_value(id))):
				# print( "-", network.get_outcome_id(id, i), "=", str(network.get_node_value(id)[i]))
				sub_data[network.get_outcome_id(id, i)] = network.get_node_value(id)[i]
			# print(sub_data)
			data[id] = sub_data
		return data

	def update_trees(self, tree_data: dict):
		"""
		Updates the "drzewo" node in the network.
		The parameter 'tree_data' should look like: 
		{
			'brzoza': 0.1, 
			'dab': 0.5, 
			'swierk': 0.35, 
			'sosna': 0.05000000000000004
		}
		"""
		probabilities = []
		for tree in tree_data.items():
			#print(tree[1], type(tree[1]))
			probabilities.append(tree[1])
	
		self.net.set_node_definition('drzewo', probabilities)
		self.net.update_beliefs()
		# print_all_posteriors(net)
		self.current_state = self.load_current_state(self.net)

	def print_posteriors(self, node_handle):
		node_id = self.net.get_node_id(node_handle)
		if self.net.is_evidence(node_handle):
			print(node_id + " has evidence set (" + self.net.get_outcome_id(node_handle, self.net.get_evidence(node_handle)) + ")")
		else :
			posteriors = self.net.get_node_value(node_handle)
			for i in range(0, len(posteriors)):
				print("P(" + node_id + "=" + self.net.get_outcome_id(node_handle, i) + ")=" + str(posteriors[i]))

	def print_all_posteriors(self):
		for handle in self.net.get_all_nodes():
			self.print_posteriors(self.net, handle)
