import numpy as np

def pack2dict(packet):
    if packet[0] == 0x47:
        data = packet[2:]
        count = packet[1]
        SatNumbers = []
        SignalLevels = []
        for i in range(count):
            SatNumbers.append(data[2*i])
            SignalLevels.append(data[2*i+1])

        return {
            "Report": "0x47",
            "Count": packet[1],
            "Sat Numbers": SatNumbers,
            "Signal Levels": SignalLevels
        }

    if packet[0] == 0x58:
        if packet[2] == 0x2: #Almanac
            return {
                "Report": "0x38",
                "Type of data": packet[2],
                "Sat PRN": packet[3],
                "Length": packet[4],
                "t_oa_raw":packet[5],
                "SV_HEALTH":packet[6],
                "e":packet[7],
                "t_oa":packet[8],
                "i_o":packet[9],
                "OMEGADOT":packet[10],
                "sqrt_A":packet[11],
                "OMEGA_0":packet[12],
                "OMEGA":packet[13],
                "M_0":packet[14],
                "a_f0":packet[15],
                "a_f1":packet[16],
                "Axis":packet[17],
                "n":packet[18],
                "OMEGA_n":packet[19],
                "ODOT_n":packet[20],
                "t_zc":packet[21],
                "Week":packet[22],
                "WN_oa":packet[22]
            }

        if packet[2] == 0x3: #Health page, t_oa, WN_oa
            return {
                "Report": "0x38",
                "Type of data": packet[2],
                "Sat PRN": packet[3],
                "Length": packet[4],
                "Week number for health": packet[5],
                "SV_health": packet[6],
                "t_oa": packet[7],
                "Current t_oa": packet[8],
                "Current week": packet[9]
            }

        if packet[2] == 0x4: #Ionosphere
            return {
                "Report": "0x38",
                "Type of data": packet[2],
                "Sat PRN": packet[3],
                "Length": packet[4],
                "Alpha_0":packet[6],
                "Alpha_1":packet[7],
                "Alpha_2":packet[8],
                "Alpha_3":packet[9],
                "Beta_0":packet[10],
                "Beta_1":packet[11],
                "Beta_2":packet[12],
                "Beta_3":packet[13]
            }

        if packet[2] == 0x5: #UTC
            return {
                "Report": "0x38",
                "Type of data": packet[2],
                "Sat PRN": packet[3],
                "Length": packet[4],
                "A_0":packet[6],
                "A_1":packet[7],
                "Dalta_t_LS":packet[8],
                "t_ot":packet[9],
                "WN_t":packet[10],
                "WN_LSF":packet[11],
                "DN":packet[12],
                "Delta_t_LSF":packet[13]
            }

        if packet[3] == 0x6: #Ephemeris
            return {
                "Report": "0x38",
                "Type of data": packet[2],
                "Sat PRN": packet[3],
                "Length": packet[4],
                "SV_number":packet[5],
                "t_ephem":packet[6],
                "weeknumber":packet[7],
                "CodeL2":packet[8],
                "L2Pdata":packet[9],
                "SVacc_raw":packet[10],
                "SV_health":packet[11],
                "IODC":packet[12],
                "t_GD":packet[13],
                "t_oc":packet[14],
                "a_f2":packet[15],
                "a_f1":packet[16],
                "a_f0":packet[17],
                "SVacc":packet[18],
                "IODE":packet[19],
                "fit_interval":packet[20],
                "C_rs":packet[21],
                "Dalta_n":packet[22],
                "M_0":packet[23],
                "C_uc":packet[24],
                "e":packet[25],
                "C_us":packet[26],
                "aqrt_A":packet[27],
                "t_oe":packet[28],
                "C_ic":packet[29],
                "OMEGA_0":packet[30],
                "C_is":packet[31],
                "i_0":packet[32],
                "C_rc":packet[33],
                "Omega":packet[34],
                "OMEGADOT":packet[35],
                "IDOT":packet[36],
                "Axis":packet[37],
                "n":packet[38],
                "r1me2":packet[39],
                "OMEGA_n":packet[40],
                "ODOT_n":packet[41]
            }

    if packet[0] == 0x5A:
        return {
            "Report": "0x5A",
            "SV PRN": packet[1],
            "Sample length": packet[2],
            "Signal level": packet[3],
            "Code phase": packet[4],
            "Doppler": packet[5],
            "Time of measurement": packet[6]
        }

    if packet[0] == 0x5D:
        return {
            "Report": "0x5D",
            "SV PRN": packet[1],
            "Channel number": packet[2],
            "Acquisition flag": packet[3],
            "SV used in Pos or Time calc": packet[4],
            "signal level": packet[5],
            "time of last measurement": packet[6],
            "elevation angles": packet[7],
            "azimuth angle": packet[8],
            "old measurement flag": packet[9],
            "integer msec flag": packet[10],
            "bad data flag": packet[11],
            "data collection flag": packet[12],
            "Used flags": packet[13],
            "SV Type": packet[14]
        }

    if packet[0] == 0x6C:
        return {
            "Report": "0x6C",
            "fix dimension": packet[1]&0x7,
            "fix mode": (packet[1]>>3)&0x1,
            "PDOP": packet[2],
            "HDOP": packet[3],
            "VDOP": packet[4],
            "TDOP": packet[5],
            "SV Count":packet[6],
            "SV List":packet[7:]
        }

    if packet[0] == 0x8F:
        if packet[1] == 0xAC: #Supplemental Timing Packet
            return {
                "Report": "0x8F-AC",
                "Reciver Mode": packet[2],
                "Disciplining Mode":packet[3],
                "Self-Survey Progress": packet[4],
                "Holdover Duration":packet[5],
                "Critical Arams": packet[6],
                "Minor Alarms":packet[7],
                "GPS Decoding Status":packet[8],
                "Disciplining Activity":packet[9],
                "PPS indication":packet[10],
                "Spare Status 2":packet[11],
                "PPS Offset":packet[12],
                "Clock Offset":packet[13],
                "DAC Value":packet[14],
                "DAC Voltage":packet[15],
                "Temperature":packet[16],
                "Latitude": np.rad2deg(packet[17]),
                "Longitude":np.rad2deg(packet[18]),
                "Altitude":packet[19],
                "PPS Quantization Error":packet[20],
                "Spare":packet[21]
            }
        
        if packet[1] == 0xAB: #0x8F-AB: Primary Timing Packet
            return {
                "Report": "0x8F-AB",
                "Time of week": packet[2],
                "Week Number": packet[3],
                "UTC Offset": packet[4],
                "Time Flag": packet[5],
                "Seconds": packet[6],
                "Minutes":packet[7],
                "Hours":packet[8],
                "Day of Month":packet[9],
                "Month":packet[10],
                "Year":packet[11]
            }
    
    if packet[0] == 0xBB:
        return {
            "Report":"0xBB",
            "Subpacket ID": packet[1],
            "Receiver mode": packet[2],
            "Elevation mask": packet[6],
            "C/No mask": packet[7],
            "PDOP mask": packet[8],
            "PDOP switch": packet[9],
            "Anti-Jam Mode": packet[11],
            "Constellation": packet[13]
        }

    return "Packet not find in list"