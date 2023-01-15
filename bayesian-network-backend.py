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

def load_node_ids(network: pysmile.Network):
	node_ids = network.get_all_node_ids() 
	for id in node_ids:
		print(id, network.get_node_value(id))
		for i in range(0, len(network.get_node_value(id))):
			print(network.get_outcome_id(id, i), "=", str(network.get_node_value(id)[i]))


def main():
	net = load_network("networks/Network1.xdsl")
	load_node_ids(network=net)



if __name__ == '__main__':
    main()
