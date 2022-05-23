import select
import socket
import logging

class TcpApp(object):
    def __init__(self, **kwargs) -> None:
        self.tcp_ip = kwargs["address"]
        logging.info(self.tcp_ip)
        self.tcp_port = kwargs["port"]
        logging.info(self.tcp_port)
        self.buffer_size = kwargs["buffer_size"]
        logging.info(self.buffer_size)
        self.node_id = kwargs["node_id"]
        logging.info(self.node_id)

        self.param = []
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.tcp_ip, self.tcp_port))
        self.server.listen(1)
        self.rxset = [self.server]
        self.txset = []

    def perform(self):
        while 1:
            rxfds, txfds, exfds = select.select(self.rxset, self.txset, self.rxset)
            for sock in rxfds:
                if sock is self.server:
                    conn, addr = self.server.accept()
                    conn.setblocking(0)
                    self.rxset.append(conn)
                    logging.info("Connection from address:", addr)
                else:
                    try:
                        data = sock.recv(self.buffer_size)

                        with open("/tmp/logs/data.log", 'a+') as datalog:
                            datalog.write(data.decode("utf-8"))

                        if data == ";":
                            logging.info("Received all the data")
                            for x in param:
                                logging.info(x)
                            param = []
                            self.rxset.remove(sock)
                            sock.close()
                        else:
                            logging.info("received data", data.decode("utf-8"))
                            param.append(data)
                    except:
                        logging.info("Connection closed by remote end")
                        param = []
                        self.rxset.remove(sock)
                        sock.close()
