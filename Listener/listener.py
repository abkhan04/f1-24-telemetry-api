from packets import packets
import socket


class Listener:
    def __init__(self, ip_address, port) -> None:
        self.ip_address = ip_address
        self.port = port

        # AF_INET is Internet
        # SOCK_DGRAM is UDP
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind((self.ip_address, self.port))


    def listener(self):
        # Receive the packet
        packet = self.socket.recv(2048)

        # Create PacketHeader class
        header = packets.PacketHeader.from_buffer_copy(packet)

        # If the packet_id is 6, then create a PacketCarTelemetryData class
        if header.packet_id == 6:
            return packets.PacketCarTelemetryData.from_buffer_copy(packet)
