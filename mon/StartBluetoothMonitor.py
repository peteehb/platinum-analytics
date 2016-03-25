from ProcessManager import Process

def run():
    conn_established = check_connection()




def check_connection():
    conn_established = False
    conn = connected_to_internet()
    return conn_established


def connected_to_internet():
    conn_established = False

    p = Process('sudo ip route ls')
    
    if p.error:
	conn_established = False	

    if p.output:
        conn_established = True
    
    return conn_established
