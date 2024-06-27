from ctypes import LittleEndianStructure, Union
from ctypes import c_uint8, c_int8, c_uint16, c_int16, c_uint32, c_float, c_double, c_uint64, c_char 


class Packet(LittleEndianStructure):

    _pack_ = 1


class PacketHeader(Packet):
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


class CarTelemetryData(Packet):
    """
    A class representing the CarTelemetryData packet

    This packet details telemetry for all the cars in the race.
    It details various values that would be recorded on the car such as speed, throttle application, DRS etc.
    Note that the rev light configurations are presented separately as well and will mimic real life driver preferences.

    Attributes:
        speed (int): Speed of the car in kilometres per hour
        throttle (float): Amount of throttle applied (0.0 to 1.0)
        steer (float): Steering (-1.0 (full lock left) to 1.0 (full lock right))
        brake (float): Amount of brake applied (0.0 to 1.0)
        clutch (int): Amount of clutch applied (0 to 100)
        gear (int): Gear selected (1-8, N=0, R=-1)
        engine_rpm (int): Engine RPM
        drs (int): 0 = off, 1 = on
        rev_lights_percent (int): Rev lights indicator (percentage)
        rev_lights_bit_value (int): Rev lights (bit 0 = leftmost LED, bit 14 = rightmost LED)
        brakes_temperature[4] (int): Brakes temperature (celsius)
        tyres_surface_temperature[4] (int): Tyres surface temperature (celsius)
        tyres_inner_temperature[4] (int): Tyres inner temperature (celsius)
        engine_temperature (int): Engine temperature (celsius)
        tyres_pressure[4] (float): Tyres pressure (PSI)
        surface_type[4] (int:) Driving surface, see appendices
    """

    _fields_ = [
        ("speed", c_uint16),
        ("throttle", c_float),
        ("steer", c_float),
        ("brake", c_float),
        ("clutch", c_uint8),
        ("gear", c_int8),
        ("engine_rpm", c_uint16),
        ("drs", c_uint8),
        ("rev_lights_percent", c_uint8),
        ("rev_lights_bit_value", c_uint16),
        ("brakes_temperature", c_uint16 * 4),
        ("tyres_surface_temperature", c_uint8 * 4),
        ("tyres_inner_temperature", c_uint8 * 4),
        ("engine_temperature", c_uint16),
        ("tyres_pressure", c_float * 4),
        ("surface_type", c_uint8 * 4),
    ]


class PacketCarTelemetryData(Packet):
    """
    A class representing the CarTelemetryData packet for all cars in a race

    This packet details telemetry for all cars in the race.
    It details the mfd panel index and the suggested gear.

    Attributes:
        packet_header (PacketHeader): Header
        car_telemetry_data[22] (CarTelemetryData): CarTelemetryData
        mfd_panel_index (int): Index of MFD panel open - 255 = MFD closed
                               Single player, race - 0 = Car setup, 1 = Pits
                               2 = Damage, 3 =  Engine, 4 = Temperatures
                               May vary depending on game mode
        mfd_panel_index_secondary_player (int): See above
        suggested_gear (int): Suggested gear for the player (1-8), 0 if no gear suggested
    """

    _fields_ = [
        ("packet_header", PacketHeader),
        ("car_telemetry_data", CarTelemetryData * 22),
        ("mfd_panel_index", c_uint8),
        ("mfd_panel_index_secondary_player", c_uint8),
        ("suggested_gear", c_int8),
    ]
