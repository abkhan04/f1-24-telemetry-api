from packets.packets import PacketHeader, PacketCarTelemetryData
import socket


class Listener:
    def __init__(self, ip_address, port) -> None:
        self.ip_address = ip_address
        self.port = port

        # AF_INET is Internet
        # SOCK_DGRAM is UDP
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind((self.ip_address, self.port))


    def listener(self) -> PacketCarTelemetryData:
        # Receive the packet
        packet = self.socket.recv(2048)

        # Create PacketHeader class
        header = PacketHeader.from_buffer_copy(packet)

        # Loop until the packet_id is 6
        while (header.packet_id != 6):
            packet = self.socket.recv(2048)
            header = PacketHeader.from_buffer_copy(packet)

        # Create a PacketCarTelemetryData class
        return PacketCarTelemetryData.from_buffer_copy(packet)
