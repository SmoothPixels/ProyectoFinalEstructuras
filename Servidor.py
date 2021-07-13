

from multiprocessing.connection import Listener
from array import array

address = ('localhost', 6000)    

with Listener(address, authkey=b'contraseña secreta') as listener:
    with listener.accept() as conn:
        print('conexion aceptada desde', listener.last_accepted)

        conn.send([89.3, None, 'prueba', float ,21312])

        conn.send_bytes(b'hola')

        conn.send_bytes(array('i', [12, 12]))
