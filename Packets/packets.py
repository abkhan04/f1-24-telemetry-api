from ctypes import LittleEndianStructure, Union
from ctypes import c_uint8, c_int8, c_uint16, c_int16, c_uint32, c_float, c_double, c_uint64, c_char 


class PacketHeader(LittleEndianStructure):
    """
    A class representing the base structure for packet headers

    Attributes:
        packet_format (int): 2024
        game_year (int): Game year - last two digits e.g. 24
        game_major_version (int): Game major version - "X.00"
        game_minor_version (int): Game minor version - "1.XX"
        packet_version (int): Version of this packet type, all start from 1
        packet_id (int): Identifier for the packet type
        session_uid (int): Unique identifier for the session
        session_time (int): Session timestamp
        frame_identifier (int): Identifier for the frame the data was retrieved on
        overall_frame_identifier (int): Overall identifier for the frame the data was retrieved on, doesn't go back after flashbacks
        player_car_index (int): Index of player's car in the array
        secondary_player_car_index (int): Index of secondary player's car in the array (splitscreen), 255 if no second player
    """

    _pack_ = 1

    _fields_ = [
        ("packet_format", c_int16),
        ("game_year", c_uint8),
        ("game_major_version", c_uint8),
        ("game_minor_version", c_uint8),
        ("packet_version", c_uint8),
        ("packet_id", c_uint8),
        ("session_uid", c_uint64),
        ("session_time", c_float),
        ("frame_identifier", c_uint32),
        ("overall_frame_identifier", c_uint32),
        ("player_car_index", c_uint8),
        ("secondary_player_car_index", c_uint8),
    ]
