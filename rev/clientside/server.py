#!/usr/bin/python3

import time
from socketserver import ThreadingTCPServer, StreamRequestHandler

HOST = "0.0.0.0"  # All ifaces
PORT = 31423  # Port to listen on (non-privileged ports are > 1023)

class EchoHandler(StreamRequestHandler):
    allow_reuse_address = True

    def handle(self):
        print(f"Connected by {self.client_address[0]}:{self.client_address[1]}")
        gates = [0] * 10
        print(gates)
        start = time.time()
        while True:
            data = self.rfile.readline()
            if time.time() - start > 10:
                print("TIMEOUT")
                break
            if not data:
                break
            d = data.split(b"\x00")
            print(d)
            if d[0] == b"\x04\x04":
                print("Protocol matched")
            if d[1] == b"PING\n":
                print("PONG")
                self.wfile.write(b"PONG\n")
            if d[1] == b"GETVERSION\n":
                self.wfile.write(b"1.0-BETA\n")
            if d[1] == b"READ":
                addr = int(d[2].strip())
                if 0 > addr or addr > 9:
                    print(b"KO\n")
                    self.wfile.write(b"KO\n")
                else:
                    print(str(gates[addr]).encode() + b"\n")
                    self.wfile.write(str(gates[addr]).encode() + b"\n")
            if d[1] == b"WRITE":
                addr = int(d[2])
                value = int(d[3].strip())
                if 0 > addr or addr > 9:
                    print(b"KO1\n")
                    self.wfile.write(b"KO\n")
                elif value != 0 and value != 1:
                    print(b"KO2\n")
                    self.wfile.write(b"KO\n")
                else:
                    gates[addr] = value
                    print(b"OK\x00")
                    self.wfile.write(b"OK\n")
            if d[1] == b"GETFLAG\n":
                open = 0
                for i in gates:
                    if not i:
                        open += 1
                if open:
                    print("{} gates left\n".format(open).encode())
                    self.wfile.write("{} gates left\n".format(open).encode())
                else:
                    print(b"ETSIIT_CTF{S3rver-s1de_is_th3_imp0rtant_sid33!!}\n")
                    self.wfile.write(b"ETSIIT_CTF{S3rver-s1de_is_th3_imp0rtant_sid33!!}\n")

server = ThreadingTCPServer((HOST, PORT), EchoHandler)
server.serve_forever()
