
from multiprocessing.connection import Client
from array import array

address = ('localhost', 6000)

with Client(address, authkey=b'contraseña secreta') as conn:
    
    print(conn.recv())                  # => se recibe [89.3, None, 'prueba', float ,21312]

    print(conn.recv_bytes())            # => se recibe 'hola'

    arr = array('i', [0, 0, 0, 0, 0])   # => [12, 12, 0, 0, 0]
    print(conn.recv_bytes_into(arr))    
    print(arr)                          