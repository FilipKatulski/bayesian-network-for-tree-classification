# License issued by BayesFusion Licensing Server
# The code below must be executed before any PySMILE object is created.
# You can use "import pysmile_license" or copy the pysmile.License
# call into your Python source code.
import pysmile

pysmile.License((
	b"SMILE LICENSE aed44788 f0fe3c1d b0705d64 "
	b"THIS IS AN ACADEMIC LICENSE AND CAN BE USED "
	b"SOLELY FOR ACADEMIC RESEARCH AND TEACHING, "
	b"AS DEFINED IN THE BAYESFUSION ACADEMIC "
	b"SOFTWARE LICENSING AGREEMENT. "
	b"Serial #: a6820kjx54d21kkhqx4jpvm23 "
	b"Issued for: Patul Patulak (p4t00lak@gmail.com) "
	b"Academic institution: AGH University of Science and Technology "
	b"Valid until: 2023-07-13 "
	b"Issued by BayesFusion activation server"
	),[
	0x3b,0x22,0xbb,0xec,0x3a,0x95,0x74,0x7e,0x2c,0x68,0x7e,0xdf,0x0f,0xf0,0x18,0xbd,
	0x9f,0xcb,0xcb,0x32,0x37,0x00,0xd1,0xcb,0x05,0xef,0x7f,0x05,0x0f,0x8b,0xe2,0xa0,
	0x87,0x7c,0x4c,0x7e,0xa4,0x4f,0xee,0xe0,0x36,0xcf,0xb7,0xd2,0x4d,0x6d,0x52,0x30,
	0xc8,0x76,0x43,0x64,0x93,0x0f,0x24,0x92,0x14,0x47,0x59,0xda,0xf5,0x4a,0x45,0xb6])


def load_network(path: str) -> pysmile.Network:
	net = pysmile.Network()
	net.read_file(path)
	net.update_beliefs()

	return net 

def load_current_state(network: pysmile.Network) -> dict:
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

def update_trees(network: pysmile.Network, tree_data: dict) -> pysmile.Network:
	"""
	Updates the "drzewo" node in the network, returns the new network.
	The parameter 'tree_data' should look like: 
	{
		'brzoza': 0.1, 
		'dab': 0.5, 
		'swierk': 0.35, 
		'sosna': 0.05000000000000004
	}
	"""
	net = network
	probabilities = []

	for tree in tree_data.items():
		#print(tree[1], type(tree[1]))
		probabilities.append(tree[1])
	
	net.set_node_definition('drzewo', probabilities)
	net.update_beliefs()
	return net


def main():
	net = load_network("networks/Network1.xdsl")
	curr_state = load_current_state(network=net)
	print(curr_state) 

	trees =	{
		'brzoza': 0.3, 
		'dab': 0.3, 
		'swierk': 0.35, 
		'sosna': 0.05000000000000004
	}


	new_net = update_trees(network=net, tree_data=trees)

	print(load_current_state(network=new_net))


if __name__ == '__main__':
    main()
