\ Model example
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  - 1e+06 y_state0_action0 - 1e+06 y_state0_action1 - 1e+06 y_state1_action1
   - 1e+06 y_state2_action0 - 1e+06 y_state2_action1
   - 1e+06 y_state3_action1 - 1e+06 y_state4_action0
   - 1e+06 y_state4_action1 - 1e+06 y_state5_action0
   - 1e+06 y_state5_action1 - 1e+06 y_state6_action1
   - 1e+06 y_state7_action0 - 1e+06 y_state7_action1
   - 1e+06 y_state8_action1 - 1e+06 y_state9_action0
   - 1e+06 y_state10_action0 - 1e+06 y_state11_action0
   - 1e+06 y_state12_action0 - 1e+06 y_state13_action0
   - 1e+06 y_state14_action0 - 1e+06 y_state15_action0
   - 1e+06 y_state16_action1 - 1e+06 y_state17_action0
   - 1e+06 y_state18_action0 - 1e+06 y_state19_action0
   - 1e+06 y_state20_action1 - 1e+06 y_state21_action0
   - 1e+06 y_state22_action0 - 1e+06 y_state23_action0
   - 1e+06 y_state24_action0 - 1e+06 y_state25_action2
   - 1e+06 y_state26_action2 - 1e+06 y_state26_action1
   - 1e+06 y_state27_action0 - 1e+06 y_state28_action0
   - 1e+06 y_state29_action0 - 1e+06 y_state30_action2
   - 1e+06 y_state31_action2 - 1e+06 y_state31_action1
   - 1e+06 y_state32_action0 - 1e+06 y_state33_action0
   - 1e+06 y_state34_action0 - 1e+06 y_state35_action2
   - 1e+06 y_state36_action2 - 1e+06 y_state37_action2
   - 1e+06 y_state38_action2 - 1e+06 y_state38_action1
   - 1e+06 y_state39_action0 - 1e+06 y_state40_action2
   - 1e+06 y_state41_action2 - 1e+06 y_state42_action2
   - 1e+06 y_state43_action2 - 1e+06 y_state44_action0
   - 1e+06 y_state44_action1 - 1e+06 y_state45_action1
   - 1e+06 y_state46_action0 - 1e+06 y_state46_action1
   - 1e+06 y_state47_action1 - 1e+06 y_state48_action0
   - 1e+06 y_state48_action1 - 1e+06 y_state49_action0
   - 1e+06 y_state49_action1 - 1e+06 y_state50_action1
   - 1e+06 y_state51_action0 - 1e+06 y_state51_action1
   - 1e+06 y_state52_action1 - 1e+06 y_state53_action0
   - 1e+06 y_state54_action0 - 1e+06 y_state55_action0
   - 1e+06 y_state56_action0 - 1e+06 y_state57_action0
   - 1e+06 y_state58_action0 - 1e+06 y_state59_action0
   - 1e+06 y_state60_action1 - 1e+06 y_state61_action0
   - 1e+06 y_state62_action0 - 1e+06 y_state63_action0
   - 1e+06 y_state64_action1 - 1e+06 y_state65_action0
   - 1e+06 y_state66_action0 - 1e+06 y_state67_action0
   - 1e+06 y_state68_action0 - 1e+06 y_state69_action2
   - 1e+06 y_state70_action2 - 1e+06 y_state70_action1
   - 1e+06 y_state71_action0 - 1e+06 y_state72_action0
   - 1e+06 y_state73_action0 - 1e+06 y_state74_action2
   - 1e+06 y_state75_action2 - 1e+06 y_state75_action1
   - 1e+06 y_state76_action0 - 1e+06 y_state77_action0
   - 1e+06 y_state79_action2 - 1e+06 y_state80_action2
   - 1e+06 y_state81_action2 - 1e+06 y_state82_action2
   - 1e+06 y_state82_action1 - 1e+06 y_state83_action3
   - 1e+06 y_state84_action2 - 1e+06 y_state85_action2
   - 1e+06 y_state86_action2 - 1e+06 y_state87_action2
   - x_reward0_state0_lower + x_reward0_state0_upper + 1.03e+08 Constant
Subject To
 R0: y_state0_action0 + y_state0_action1 <= 1e+06
 R1: 1e+06 y_state0_action0 + 1e+06 y_state0_action1 >= 1
 R2: 1e+06 y_state0_action1 - y_state1_action1 >= 0
 R3: y_state0_action1 - 1e+06 y_state1_action1 <= 0
 R4: 1e+06 y_state1_action1 - y_state2_action0 - y_state2_action1 >= 0
 R5: y_state1_action1 - 1e+06 y_state2_action0 - 1e+06 y_state2_action1
   <= 0
 R6: 1e+06 y_state2_action1 - y_state3_action1 >= 0
 R7: y_state2_action1 - 1e+06 y_state3_action1 <= 0
 R8: 1e+06 y_state3_action1 - y_state4_action0 - y_state4_action1 >= 0
 R9: y_state3_action1 - 1e+06 y_state4_action0 - 1e+06 y_state4_action1
   <= 0
 R10: 1e+06 y_state4_action1 - y_state5_action0 - y_state5_action1 >= 0
 R11: y_state4_action1 - 1e+06 y_state5_action0 - 1e+06 y_state5_action1
   <= 0
 R12: 1e+06 y_state5_action1 - y_state6_action1 >= 0
 R13: y_state5_action1 - 1e+06 y_state6_action1 <= 0
 R14: 1e+06 y_state6_action1 - y_state7_action0 - y_state7_action1 >= 0
 R15: y_state6_action1 - 1e+06 y_state7_action0 - 1e+06 y_state7_action1
   <= 0
 R16: 1e+06 y_state7_action1 - y_state8_action1 >= 0
 R17: y_state7_action1 - 1e+06 y_state8_action1 <= 0
 R18: 1e+06 y_state8_action1 - y_state9_action0 >= 0
 R19: y_state8_action1 - 1e+06 y_state9_action0 <= 0
 R20: 1e+06 y_state0_action0 - y_state10_action0 >= 0
 R21: y_state0_action0 - 1e+06 y_state10_action0 <= 0
 R22: 1e+06 y_state2_action0 - y_state11_action0 >= 0
 R23: y_state2_action0 - 1e+06 y_state11_action0 <= 0
 R24: 1e+06 y_state4_action0 - y_state12_action0 >= 0
 R25: y_state4_action0 - 1e+06 y_state12_action0 <= 0
 R26: 1e+06 y_state5_action0 - y_state13_action0 >= 0
 R27: y_state5_action0 - 1e+06 y_state13_action0 <= 0
 R28: 1e+06 y_state7_action0 - y_state14_action0 >= 0
 R29: y_state7_action0 - 1e+06 y_state14_action0 <= 0
 R30: 1e+06 y_state9_action0 - y_state15_action0 >= 0
 R31: y_state9_action0 - 1e+06 y_state15_action0 <= 0
 R32: 1e+06 y_state10_action0 - y_state16_action1 >= 0
 R33: y_state10_action0 - 1e+06 y_state16_action1 <= 0
 R34: 1e+06 y_state16_action1 - y_state17_action0 >= 0
 R35: y_state16_action1 - 1e+06 y_state17_action0 <= 0
 R36: 1e+06 y_state11_action0 - y_state18_action0 >= 0
 R37: y_state11_action0 - 1e+06 y_state18_action0 <= 0
 R38: 1e+06 y_state12_action0 - y_state19_action0 >= 0
 R39: y_state12_action0 - 1e+06 y_state19_action0 <= 0
 R40: 1e+06 y_state13_action0 - y_state20_action1 >= 0
 R41: y_state13_action0 - 1e+06 y_state20_action1 <= 0
 R42: 1e+06 y_state20_action1 - y_state21_action0 >= 0
 R43: y_state20_action1 - 1e+06 y_state21_action0 <= 0
 R44: 1e+06 y_state14_action0 - y_state22_action0 >= 0
 R45: y_state14_action0 - 1e+06 y_state22_action0 <= 0
 R46: 1e+06 y_state15_action0 - y_state23_action0 >= 0
 R47: y_state15_action0 - 1e+06 y_state23_action0 <= 0
 R48: - y_state24_action0 + 1e+06 y_state25_action2 >= 0
 R49: - 1e+06 y_state24_action0 + y_state25_action2 <= 0
 R50: 1e+06 y_state17_action0 - y_state25_action2 + 1e+06 y_state26_action2
   >= 0
 R51: y_state17_action0 - 1e+06 y_state25_action2 + y_state26_action2 <= 0
 R52: 1e+06 y_state18_action0 - y_state26_action2 - y_state26_action1 >= 0
 R53: y_state18_action0 - 1e+06 y_state26_action2 - 1e+06 y_state26_action1
   <= 0
 R54: 1e+06 y_state26_action1 - y_state27_action0 >= 0
 R55: y_state26_action1 - 1e+06 y_state27_action0 <= 0
 R56: 1e+06 y_state19_action0 - y_state28_action0 >= 0
 R57: y_state19_action0 - 1e+06 y_state28_action0 <= 0
 R58: - y_state29_action0 + 1e+06 y_state30_action2 >= 0
 R59: - 1e+06 y_state29_action0 + y_state30_action2 <= 0
 R60: 1e+06 y_state21_action0 - y_state30_action2 + 1e+06 y_state31_action2
   >= 0
 R61: y_state21_action0 - 1e+06 y_state30_action2 + y_state31_action2 <= 0
 R62: 1e+06 y_state22_action0 - y_state31_action2 - y_state31_action1 >= 0
 R63: y_state22_action0 - 1e+06 y_state31_action2 - 1e+06 y_state31_action1
   <= 0
 R64: 1e+06 y_state31_action1 - y_state32_action0 >= 0
 R65: y_state31_action1 - 1e+06 y_state32_action0 <= 0
 R66: 1e+06 y_state23_action0 - y_state33_action0 >= 0
 R67: y_state23_action0 - 1e+06 y_state33_action0 <= 0
 R68: 1e+06 y_state24_action0 - y_state34_action0 + 1e+06 y_state35_action2
   >= 0
 R69: y_state24_action0 - 1e+06 y_state34_action0 + y_state35_action2 <= 0
 R70: - y_state35_action2 + 1e+06 y_state36_action2 >= 0
 R71: - 1e+06 y_state35_action2 + y_state36_action2 <= 0
 R72: - y_state36_action2 + 1e+06 y_state37_action2 >= 0
 R73: - 1e+06 y_state36_action2 + y_state37_action2 <= 0
 R74: 1e+06 y_state27_action0 - y_state37_action2 + 1e+06 y_state38_action2
   >= 0
 R75: y_state27_action0 - 1e+06 y_state37_action2 + y_state38_action2 <= 0
 R76: 1e+06 y_state28_action0 - y_state38_action2 - y_state38_action1 >= 0
 R77: y_state28_action0 - 1e+06 y_state38_action2 - 1e+06 y_state38_action1
   <= 0
 R78: 1e+06 y_state29_action0 + 1e+06 y_state38_action1 - y_state39_action0
   + 1e+06 y_state40_action2 >= 0
 R79: y_state29_action0 + y_state38_action1 - 1e+06 y_state39_action0
   + y_state40_action2 <= 0
 R80: - y_state40_action2 + 1e+06 y_state41_action2 >= 0
 R81: - 1e+06 y_state40_action2 + y_state41_action2 <= 0
 R82: - y_state41_action2 + 1e+06 y_state42_action2 >= 0
 R83: - 1e+06 y_state41_action2 + y_state42_action2 <= 0
 R84: 1e+06 y_state32_action0 - y_state42_action2 + 1e+06 y_state43_action2
   >= 0
 R85: y_state32_action0 - 1e+06 y_state42_action2 + y_state43_action2 <= 0
 R86: 1e+06 y_state33_action0 - y_state43_action2 >= 0
 R87: y_state33_action0 - 1e+06 y_state43_action2 <= 0
 R88: 1e+06 y_state34_action0 - y_state44_action0 - y_state44_action1 >= 0
 R89: y_state34_action0 - 1e+06 y_state44_action0 - 1e+06 y_state44_action1
   <= 0
 R90: 1e+06 y_state44_action1 - y_state45_action1 >= 0
 R91: y_state44_action1 - 1e+06 y_state45_action1 <= 0
 R92: 1e+06 y_state45_action1 - y_state46_action0 - y_state46_action1 >= 0
 R93: y_state45_action1 - 1e+06 y_state46_action0 - 1e+06 y_state46_action1
   <= 0
 R94: 1e+06 y_state46_action1 - y_state47_action1 >= 0
 R95: y_state46_action1 - 1e+06 y_state47_action1 <= 0
 R96: 1e+06 y_state47_action1 - y_state48_action0 - y_state48_action1 >= 0
 R97: y_state47_action1 - 1e+06 y_state48_action0 - 1e+06 y_state48_action1
   <= 0
 R98: 1e+06 y_state39_action0 + 1e+06 y_state48_action1 - y_state49_action0
   - y_state49_action1 >= 0
 R99: y_state39_action0 + y_state48_action1 - 1e+06 y_state49_action0
   - 1e+06 y_state49_action1 <= 0
 R100: 1e+06 y_state49_action1 - y_state50_action1 >= 0
 R101: y_state49_action1 - 1e+06 y_state50_action1 <= 0
 R102: 1e+06 y_state50_action1 - y_state51_action0 - y_state51_action1
   >= 0
 R103: y_state50_action1 - 1e+06 y_state51_action0
   - 1e+06 y_state51_action1 <= 0
 R104: 1e+06 y_state51_action1 - y_state52_action1 >= 0
 R105: y_state51_action1 - 1e+06 y_state52_action1 <= 0
 R106: 1e+06 y_state52_action1 - y_state53_action0 >= 0
 R107: y_state52_action1 - 1e+06 y_state53_action0 <= 0
 R108: 1e+06 y_state44_action0 - y_state54_action0 >= 0
 R109: y_state44_action0 - 1e+06 y_state54_action0 <= 0
 R110: 1e+06 y_state46_action0 - y_state55_action0 >= 0
 R111: y_state46_action0 - 1e+06 y_state55_action0 <= 0
 R112: 1e+06 y_state48_action0 - y_state56_action0 >= 0
 R113: y_state48_action0 - 1e+06 y_state56_action0 <= 0
 R114: 1e+06 y_state49_action0 - y_state57_action0 >= 0
 R115: y_state49_action0 - 1e+06 y_state57_action0 <= 0
 R116: 1e+06 y_state51_action0 - y_state58_action0 >= 0
 R117: y_state51_action0 - 1e+06 y_state58_action0 <= 0
 R118: 1e+06 y_state53_action0 - y_state59_action0 >= 0
 R119: y_state53_action0 - 1e+06 y_state59_action0 <= 0
 R120: 1e+06 y_state54_action0 - y_state60_action1 >= 0
 R121: y_state54_action0 - 1e+06 y_state60_action1 <= 0
 R122: 1e+06 y_state60_action1 - y_state61_action0 >= 0
 R123: y_state60_action1 - 1e+06 y_state61_action0 <= 0
 R124: 1e+06 y_state55_action0 - y_state62_action0 >= 0
 R125: y_state55_action0 - 1e+06 y_state62_action0 <= 0
 R126: 1e+06 y_state56_action0 - y_state63_action0 >= 0
 R127: y_state56_action0 - 1e+06 y_state63_action0 <= 0
 R128: 1e+06 y_state57_action0 - y_state64_action1 >= 0
 R129: y_state57_action0 - 1e+06 y_state64_action1 <= 0
 R130: 1e+06 y_state64_action1 - y_state65_action0 >= 0
 R131: y_state64_action1 - 1e+06 y_state65_action0 <= 0
 R132: 1e+06 y_state58_action0 - y_state66_action0 >= 0
 R133: y_state58_action0 - 1e+06 y_state66_action0 <= 0
 R134: 1e+06 y_state59_action0 - y_state67_action0 >= 0
 R135: y_state59_action0 - 1e+06 y_state67_action0 <= 0
 R136: - y_state68_action0 + 1e+06 y_state69_action2 >= 0
 R137: - 1e+06 y_state68_action0 + y_state69_action2 <= 0
 R138: 1e+06 y_state61_action0 - y_state69_action2
   + 1e+06 y_state70_action2 >= 0
 R139: y_state61_action0 - 1e+06 y_state69_action2 + y_state70_action2
   <= 0
 R140: 1e+06 y_state62_action0 - y_state70_action2 - y_state70_action1
   >= 0
 R141: y_state62_action0 - 1e+06 y_state70_action2
   - 1e+06 y_state70_action1 <= 0
 R142: 1e+06 y_state70_action1 - y_state71_action0 >= 0
 R143: y_state70_action1 - 1e+06 y_state71_action0 <= 0
 R144: 1e+06 y_state63_action0 - y_state72_action0 >= 0
 R145: y_state63_action0 - 1e+06 y_state72_action0 <= 0
 R146: - y_state73_action0 + 1e+06 y_state74_action2 >= 0
 R147: - 1e+06 y_state73_action0 + y_state74_action2 <= 0
 R148: 1e+06 y_state65_action0 - y_state74_action2
   + 1e+06 y_state75_action2 >= 0
 R149: y_state65_action0 - 1e+06 y_state74_action2 + y_state75_action2
   <= 0
 R150: 1e+06 y_state66_action0 - y_state75_action2 - y_state75_action1
   >= 0
 R151: y_state66_action0 - 1e+06 y_state75_action2
   - 1e+06 y_state75_action1 <= 0
 R152: 1e+06 y_state75_action1 - y_state76_action0 >= 0
 R153: y_state75_action1 - 1e+06 y_state76_action0 <= 0
 R154: 1e+06 y_state67_action0 - y_state77_action0 >= 0
 R155: y_state67_action0 - 1e+06 y_state77_action0 <= 0
 R156: 1e+06 y_state68_action0 + 1e+06 y_state79_action2 >= 0
 R157: y_state68_action0 + y_state79_action2 <= 0
 R158: - y_state79_action2 + 1e+06 y_state80_action2 >= 0
 R159: - 1e+06 y_state79_action2 + y_state80_action2 <= 0
 R160: - y_state80_action2 + 1e+06 y_state81_action2 >= 0
 R161: - 1e+06 y_state80_action2 + y_state81_action2 <= 0
 R162: 1e+06 y_state71_action0 - y_state81_action2
   + 1e+06 y_state82_action2 >= 0
 R163: y_state71_action0 - 1e+06 y_state81_action2 + y_state82_action2
   <= 0
 R164: 1e+06 y_state72_action0 - y_state82_action2 - y_state82_action1
   >= 0
 R165: y_state72_action0 - 1e+06 y_state82_action2
   - 1e+06 y_state82_action1 <= 0
 R166: 1e+06 y_state73_action0 + 1e+06 y_state82_action1
   + 999999 y_state83_action3 + 1e+06 y_state84_action2 >= 0
 R167: y_state73_action0 + y_state82_action1 - 999999 y_state83_action3
   + y_state84_action2 <= 0
 R168: - y_state84_action2 + 1e+06 y_state85_action2 >= 0
 R169: - 1e+06 y_state84_action2 + y_state85_action2 <= 0
 R170: - y_state85_action2 + 1e+06 y_state86_action2 >= 0
 R171: - 1e+06 y_state85_action2 + y_state86_action2 <= 0
 R172: 1e+06 y_state76_action0 - y_state86_action2
   + 1e+06 y_state87_action2 >= 0
 R173: y_state76_action0 - 1e+06 y_state86_action2 + y_state87_action2
   <= 0
 R174: 1e+06 y_state77_action0 - y_state87_action2 >= 0
 R175: y_state77_action0 - 1e+06 y_state87_action2 <= 0
 R176: x_reward0_state0_lower >= 16
 R177: x_reward0_state0_upper <= 16
 R178: x_reward0_state83_lower = 0
 R179: x_reward0_state83_upper = 0
 R180: 1e+06 y_state0_action0 + x_reward0_state0_lower
   - x_reward0_state10_lower <= 1.000001e+06
 R181: - 1e+06 y_state0_action0 + x_reward0_state0_upper
   - x_reward0_state10_upper >= -999999
 R182: 1e+06 y_state0_action1 + x_reward0_state0_lower
   - x_reward0_state1_lower <= 1.000001e+06
 R183: - 1e+06 y_state0_action1 + x_reward0_state0_upper
   - x_reward0_state1_upper >= -999999
 R184: 1e+06 y_state1_action1 + x_reward0_state1_lower
   - x_reward0_state2_lower <= 1.000001e+06
 R185: - 1e+06 y_state1_action1 + x_reward0_state1_upper
   - x_reward0_state2_upper >= -999999
 R186: 1e+06 y_state2_action0 + x_reward0_state2_lower
   - x_reward0_state11_lower <= 1.000001e+06
 R187: - 1e+06 y_state2_action0 + x_reward0_state2_upper
   - x_reward0_state11_upper >= -999999
 R188: 1e+06 y_state2_action1 + x_reward0_state2_lower
   - x_reward0_state3_lower <= 1.000001e+06
 R189: - 1e+06 y_state2_action1 + x_reward0_state2_upper
   - x_reward0_state3_upper >= -999999
 R190: 1e+06 y_state3_action1 + x_reward0_state3_lower
   - x_reward0_state4_lower <= 1.000001e+06
 R191: - 1e+06 y_state3_action1 + x_reward0_state3_upper
   - x_reward0_state4_upper >= -999999
 R192: 1e+06 y_state4_action0 + x_reward0_state4_lower
   - x_reward0_state12_lower <= 1.000001e+06
 R193: - 1e+06 y_state4_action0 + x_reward0_state4_upper
   - x_reward0_state12_upper >= -999999
 R194: 1e+06 y_state4_action1 + x_reward0_state4_lower
   - x_reward0_state5_lower <= 1.000001e+06
 R195: - 1e+06 y_state4_action1 + x_reward0_state4_upper
   - x_reward0_state5_upper >= -999999
 R196: 1e+06 y_state5_action0 + x_reward0_state5_lower
   - x_reward0_state13_lower <= 1.000001e+06
 R197: - 1e+06 y_state5_action0 + x_reward0_state5_upper
   - x_reward0_state13_upper >= -999999
 R198: 1e+06 y_state5_action1 + x_reward0_state5_lower
   - x_reward0_state6_lower <= 1.000001e+06
 R199: - 1e+06 y_state5_action1 + x_reward0_state5_upper
   - x_reward0_state6_upper >= -999999
 R200: 1e+06 y_state6_action1 + x_reward0_state6_lower
   - x_reward0_state7_lower <= 1.000001e+06
 R201: - 1e+06 y_state6_action1 + x_reward0_state6_upper
   - x_reward0_state7_upper >= -999999
 R202: 1e+06 y_state7_action0 + x_reward0_state7_lower
   - x_reward0_state14_lower <= 1.000001e+06
 R203: - 1e+06 y_state7_action0 + x_reward0_state7_upper
   - x_reward0_state14_upper >= -999999
 R204: 1e+06 y_state7_action1 + x_reward0_state7_lower
   - x_reward0_state8_lower <= 1.000001e+06
 R205: - 1e+06 y_state7_action1 + x_reward0_state7_upper
   - x_reward0_state8_upper >= -999999
 R206: 1e+06 y_state8_action1 + x_reward0_state8_lower
   - x_reward0_state9_lower <= 1.000001e+06
 R207: - 1e+06 y_state8_action1 + x_reward0_state8_upper
   - x_reward0_state9_upper >= -999999
 R208: 1e+06 y_state9_action0 + x_reward0_state9_lower
   - x_reward0_state15_lower <= 1.000001e+06
 R209: - 1e+06 y_state9_action0 + x_reward0_state9_upper
   - x_reward0_state15_upper >= -999999
 R210: 1e+06 y_state10_action0 + x_reward0_state10_lower
   - x_reward0_state16_lower <= 1.000001e+06
 R211: - 1e+06 y_state10_action0 + x_reward0_state10_upper
   - x_reward0_state16_upper >= -999999
 R212: 1e+06 y_state11_action0 + x_reward0_state11_lower
   - x_reward0_state18_lower <= 1.000001e+06
 R213: - 1e+06 y_state11_action0 + x_reward0_state11_upper
   - x_reward0_state18_upper >= -999999
 R214: 1e+06 y_state12_action0 + x_reward0_state12_lower
   - x_reward0_state19_lower <= 1.000001e+06
 R215: - 1e+06 y_state12_action0 + x_reward0_state12_upper
   - x_reward0_state19_upper >= -999999
 R216: 1e+06 y_state13_action0 + x_reward0_state13_lower
   - x_reward0_state20_lower <= 1.000001e+06
 R217: - 1e+06 y_state13_action0 + x_reward0_state13_upper
   - x_reward0_state20_upper >= -999999
 R218: 1e+06 y_state14_action0 + x_reward0_state14_lower
   - x_reward0_state22_lower <= 1.000001e+06
 R219: - 1e+06 y_state14_action0 + x_reward0_state14_upper
   - x_reward0_state22_upper >= -999999
 R220: 1e+06 y_state15_action0 + x_reward0_state15_lower
   - x_reward0_state23_lower <= 1.000001e+06
 R221: - 1e+06 y_state15_action0 + x_reward0_state15_upper
   - x_reward0_state23_upper >= -999999
 R222: 1e+06 y_state16_action1 + x_reward0_state16_lower
   - x_reward0_state17_lower <= 1.000001e+06
 R223: - 1e+06 y_state16_action1 + x_reward0_state16_upper
   - x_reward0_state17_upper >= -999999
 R224: 1e+06 y_state17_action0 + x_reward0_state17_lower
   - x_reward0_state25_lower <= 1.000001e+06
 R225: - 1e+06 y_state17_action0 + x_reward0_state17_upper
   - x_reward0_state25_upper >= -999999
 R226: 1e+06 y_state18_action0 + x_reward0_state18_lower
   - x_reward0_state26_lower <= 1.000001e+06
 R227: - 1e+06 y_state18_action0 + x_reward0_state18_upper
   - x_reward0_state26_upper >= -999999
 R228: 1e+06 y_state19_action0 + x_reward0_state19_lower
   - x_reward0_state28_lower <= 1.000001e+06
 R229: - 1e+06 y_state19_action0 + x_reward0_state19_upper
   - x_reward0_state28_upper >= -999999
 R230: 1e+06 y_state20_action1 + x_reward0_state20_lower
   - x_reward0_state21_lower <= 1.000001e+06
 R231: - 1e+06 y_state20_action1 + x_reward0_state20_upper
   - x_reward0_state21_upper >= -999999
 R232: 1e+06 y_state21_action0 + x_reward0_state21_lower
   - x_reward0_state30_lower <= 1.000001e+06
 R233: - 1e+06 y_state21_action0 + x_reward0_state21_upper
   - x_reward0_state30_upper >= -999999
 R234: 1e+06 y_state22_action0 + x_reward0_state22_lower
   - x_reward0_state31_lower <= 1.000001e+06
 R235: - 1e+06 y_state22_action0 + x_reward0_state22_upper
   - x_reward0_state31_upper >= -999999
 R236: 1e+06 y_state23_action0 + x_reward0_state23_lower
   - x_reward0_state33_lower <= 1.000001e+06
 R237: - 1e+06 y_state23_action0 + x_reward0_state23_upper
   - x_reward0_state33_upper >= -999999
 R238: 1e+06 y_state24_action0 + x_reward0_state24_lower
   - x_reward0_state34_lower <= 1.000001e+06
 R239: - 1e+06 y_state24_action0 + x_reward0_state24_upper
   - x_reward0_state34_upper >= -999999
 R240: 1e+06 y_state25_action2 - x_reward0_state24_lower
   + x_reward0_state25_lower <= 1.000001e+06
 R241: - 1e+06 y_state25_action2 - x_reward0_state24_upper
   + x_reward0_state25_upper >= -999999
 R242: 1e+06 y_state26_action2 - x_reward0_state25_lower
   + x_reward0_state26_lower <= 1.000001e+06
 R243: - 1e+06 y_state26_action2 - x_reward0_state25_upper
   + x_reward0_state26_upper >= -999999
 R244: 1e+06 y_state26_action1 + x_reward0_state26_lower
   - x_reward0_state27_lower <= 1.000001e+06
 R245: - 1e+06 y_state26_action1 + x_reward0_state26_upper
   - x_reward0_state27_upper >= -999999
 R246: 1e+06 y_state27_action0 + x_reward0_state27_lower
   - x_reward0_state37_lower <= 1.000001e+06
 R247: - 1e+06 y_state27_action0 + x_reward0_state27_upper
   - x_reward0_state37_upper >= -999999
 R248: 1e+06 y_state28_action0 + x_reward0_state28_lower
   - x_reward0_state38_lower <= 1.000001e+06
 R249: - 1e+06 y_state28_action0 + x_reward0_state28_upper
   - x_reward0_state38_upper >= -999999
 R250: 1e+06 y_state29_action0 + x_reward0_state29_lower
   - x_reward0_state39_lower <= 1.000001e+06
 R251: - 1e+06 y_state29_action0 + x_reward0_state29_upper
   - x_reward0_state39_upper >= -999999
 R252: 1e+06 y_state30_action2 - x_reward0_state29_lower
   + x_reward0_state30_lower <= 1.000001e+06
 R253: - 1e+06 y_state30_action2 - x_reward0_state29_upper
   + x_reward0_state30_upper >= -999999
 R254: 1e+06 y_state31_action2 - x_reward0_state30_lower
   + x_reward0_state31_lower <= 1.000001e+06
 R255: - 1e+06 y_state31_action2 - x_reward0_state30_upper
   + x_reward0_state31_upper >= -999999
 R256: 1e+06 y_state31_action1 + x_reward0_state31_lower
   - x_reward0_state32_lower <= 1.000001e+06
 R257: - 1e+06 y_state31_action1 + x_reward0_state31_upper
   - x_reward0_state32_upper >= -999999
 R258: 1e+06 y_state32_action0 + x_reward0_state32_lower
   - x_reward0_state42_lower <= 1.000001e+06
 R259: - 1e+06 y_state32_action0 + x_reward0_state32_upper
   - x_reward0_state42_upper >= -999999
 R260: 1e+06 y_state33_action0 + x_reward0_state33_lower
   - x_reward0_state43_lower <= 1.000001e+06
 R261: - 1e+06 y_state33_action0 + x_reward0_state33_upper
   - x_reward0_state43_upper >= -999999
 R262: 1e+06 y_state34_action0 + x_reward0_state34_lower
   - x_reward0_state44_lower <= 1.000001e+06
 R263: - 1e+06 y_state34_action0 + x_reward0_state34_upper
   - x_reward0_state44_upper >= -999999
 R264: 1e+06 y_state35_action2 - x_reward0_state34_lower
   + x_reward0_state35_lower <= 1.000001e+06
 R265: - 1e+06 y_state35_action2 - x_reward0_state34_upper
   + x_reward0_state35_upper >= -999999
 R266: 1e+06 y_state36_action2 - x_reward0_state35_lower
   + x_reward0_state36_lower <= 1.000001e+06
 R267: - 1e+06 y_state36_action2 - x_reward0_state35_upper
   + x_reward0_state36_upper >= -999999
 R268: 1e+06 y_state37_action2 - x_reward0_state36_lower
   + x_reward0_state37_lower <= 1.000001e+06
 R269: - 1e+06 y_state37_action2 - x_reward0_state36_upper
   + x_reward0_state37_upper >= -999999
 R270: 1e+06 y_state38_action2 - x_reward0_state37_lower
   + x_reward0_state38_lower <= 1.000001e+06
 R271: - 1e+06 y_state38_action2 - x_reward0_state37_upper
   + x_reward0_state38_upper >= -999999
 R272: 1e+06 y_state38_action1 + x_reward0_state38_lower
   - x_reward0_state39_lower <= 1.000001e+06
 R273: - 1e+06 y_state38_action1 + x_reward0_state38_upper
   - x_reward0_state39_upper >= -999999
 R274: 1e+06 y_state39_action0 + x_reward0_state39_lower
   - x_reward0_state49_lower <= 1.000001e+06
 R275: - 1e+06 y_state39_action0 + x_reward0_state39_upper
   - x_reward0_state49_upper >= -999999
 R276: 1e+06 y_state40_action2 - x_reward0_state39_lower
   + x_reward0_state40_lower <= 1.000001e+06
 R277: - 1e+06 y_state40_action2 - x_reward0_state39_upper
   + x_reward0_state40_upper >= -999999
 R278: 1e+06 y_state41_action2 - x_reward0_state40_lower
   + x_reward0_state41_lower <= 1.000001e+06
 R279: - 1e+06 y_state41_action2 - x_reward0_state40_upper
   + x_reward0_state41_upper >= -999999
 R280: 1e+06 y_state42_action2 - x_reward0_state41_lower
   + x_reward0_state42_lower <= 1.000001e+06
 R281: - 1e+06 y_state42_action2 - x_reward0_state41_upper
   + x_reward0_state42_upper >= -999999
 R282: 1e+06 y_state43_action2 - x_reward0_state42_lower
   + x_reward0_state43_lower <= 1.000001e+06
 R283: - 1e+06 y_state43_action2 - x_reward0_state42_upper
   + x_reward0_state43_upper >= -999999
 R284: 1e+06 y_state44_action0 + x_reward0_state44_lower
   - x_reward0_state54_lower <= 1.000001e+06
 R285: - 1e+06 y_state44_action0 + x_reward0_state44_upper
   - x_reward0_state54_upper >= -999999
 R286: 1e+06 y_state44_action1 + x_reward0_state44_lower
   - x_reward0_state45_lower <= 1.000001e+06
 R287: - 1e+06 y_state44_action1 + x_reward0_state44_upper
   - x_reward0_state45_upper >= -999999
 R288: 1e+06 y_state45_action1 + x_reward0_state45_lower
   - x_reward0_state46_lower <= 1.000001e+06
 R289: - 1e+06 y_state45_action1 + x_reward0_state45_upper
   - x_reward0_state46_upper >= -999999
 R290: 1e+06 y_state46_action0 + x_reward0_state46_lower
   - x_reward0_state55_lower <= 1.000001e+06
 R291: - 1e+06 y_state46_action0 + x_reward0_state46_upper
   - x_reward0_state55_upper >= -999999
 R292: 1e+06 y_state46_action1 + x_reward0_state46_lower
   - x_reward0_state47_lower <= 1.000001e+06
 R293: - 1e+06 y_state46_action1 + x_reward0_state46_upper
   - x_reward0_state47_upper >= -999999
 R294: 1e+06 y_state47_action1 + x_reward0_state47_lower
   - x_reward0_state48_lower <= 1.000001e+06
 R295: - 1e+06 y_state47_action1 + x_reward0_state47_upper
   - x_reward0_state48_upper >= -999999
 R296: 1e+06 y_state48_action0 + x_reward0_state48_lower
   - x_reward0_state56_lower <= 1.000001e+06
 R297: - 1e+06 y_state48_action0 + x_reward0_state48_upper
   - x_reward0_state56_upper >= -999999
 R298: 1e+06 y_state48_action1 + x_reward0_state48_lower
   - x_reward0_state49_lower <= 1.000001e+06
 R299: - 1e+06 y_state48_action1 + x_reward0_state48_upper
   - x_reward0_state49_upper >= -999999
 R300: 1e+06 y_state49_action0 + x_reward0_state49_lower
   - x_reward0_state57_lower <= 1.000001e+06
 R301: - 1e+06 y_state49_action0 + x_reward0_state49_upper
   - x_reward0_state57_upper >= -999999
 R302: 1e+06 y_state49_action1 + x_reward0_state49_lower
   - x_reward0_state50_lower <= 1.000001e+06
 R303: - 1e+06 y_state49_action1 + x_reward0_state49_upper
   - x_reward0_state50_upper >= -999999
 R304: 1e+06 y_state50_action1 + x_reward0_state50_lower
   - x_reward0_state51_lower <= 1.000001e+06
 R305: - 1e+06 y_state50_action1 + x_reward0_state50_upper
   - x_reward0_state51_upper >= -999999
 R306: 1e+06 y_state51_action0 + x_reward0_state51_lower
   - x_reward0_state58_lower <= 1.000001e+06
 R307: - 1e+06 y_state51_action0 + x_reward0_state51_upper
   - x_reward0_state58_upper >= -999999
 R308: 1e+06 y_state51_action1 + x_reward0_state51_lower
   - x_reward0_state52_lower <= 1.000001e+06
 R309: - 1e+06 y_state51_action1 + x_reward0_state51_upper
   - x_reward0_state52_upper >= -999999
 R310: 1e+06 y_state52_action1 + x_reward0_state52_lower
   - x_reward0_state53_lower <= 1.000001e+06
 R311: - 1e+06 y_state52_action1 + x_reward0_state52_upper
   - x_reward0_state53_upper >= -999999
 R312: 1e+06 y_state53_action0 + x_reward0_state53_lower
   - x_reward0_state59_lower <= 1.000001e+06
 R313: - 1e+06 y_state53_action0 + x_reward0_state53_upper
   - x_reward0_state59_upper >= -999999
 R314: 1e+06 y_state54_action0 + x_reward0_state54_lower
   - x_reward0_state60_lower <= 1.000001e+06
 R315: - 1e+06 y_state54_action0 + x_reward0_state54_upper
   - x_reward0_state60_upper >= -999999
 R316: 1e+06 y_state55_action0 + x_reward0_state55_lower
   - x_reward0_state62_lower <= 1.000001e+06
 R317: - 1e+06 y_state55_action0 + x_reward0_state55_upper
   - x_reward0_state62_upper >= -999999
 R318: 1e+06 y_state56_action0 + x_reward0_state56_lower
   - x_reward0_state63_lower <= 1.000001e+06
 R319: - 1e+06 y_state56_action0 + x_reward0_state56_upper
   - x_reward0_state63_upper >= -999999
 R320: 1e+06 y_state57_action0 + x_reward0_state57_lower
   - x_reward0_state64_lower <= 1.000001e+06
 R321: - 1e+06 y_state57_action0 + x_reward0_state57_upper
   - x_reward0_state64_upper >= -999999
 R322: 1e+06 y_state58_action0 + x_reward0_state58_lower
   - x_reward0_state66_lower <= 1.000001e+06
 R323: - 1e+06 y_state58_action0 + x_reward0_state58_upper
   - x_reward0_state66_upper >= -999999
 R324: 1e+06 y_state59_action0 + x_reward0_state59_lower
   - x_reward0_state67_lower <= 1.000001e+06
 R325: - 1e+06 y_state59_action0 + x_reward0_state59_upper
   - x_reward0_state67_upper >= -999999
 R326: 1e+06 y_state60_action1 + x_reward0_state60_lower
   - x_reward0_state61_lower <= 1.000001e+06
 R327: - 1e+06 y_state60_action1 + x_reward0_state60_upper
   - x_reward0_state61_upper >= -999999
 R328: 1e+06 y_state61_action0 + x_reward0_state61_lower
   - x_reward0_state69_lower <= 1.000001e+06
 R329: - 1e+06 y_state61_action0 + x_reward0_state61_upper
   - x_reward0_state69_upper >= -999999
 R330: 1e+06 y_state62_action0 + x_reward0_state62_lower
   - x_reward0_state70_lower <= 1.000001e+06
 R331: - 1e+06 y_state62_action0 + x_reward0_state62_upper
   - x_reward0_state70_upper >= -999999
 R332: 1e+06 y_state63_action0 + x_reward0_state63_lower
   - x_reward0_state72_lower <= 1.000001e+06
 R333: - 1e+06 y_state63_action0 + x_reward0_state63_upper
   - x_reward0_state72_upper >= -999999
 R334: 1e+06 y_state64_action1 + x_reward0_state64_lower
   - x_reward0_state65_lower <= 1.000001e+06
 R335: - 1e+06 y_state64_action1 + x_reward0_state64_upper
   - x_reward0_state65_upper >= -999999
 R336: 1e+06 y_state65_action0 + x_reward0_state65_lower
   - x_reward0_state74_lower <= 1.000001e+06
 R337: - 1e+06 y_state65_action0 + x_reward0_state65_upper
   - x_reward0_state74_upper >= -999999
 R338: 1e+06 y_state66_action0 + x_reward0_state66_lower
   - x_reward0_state75_lower <= 1.000001e+06
 R339: - 1e+06 y_state66_action0 + x_reward0_state66_upper
   - x_reward0_state75_upper >= -999999
 R340: 1e+06 y_state67_action0 + x_reward0_state67_lower
   - x_reward0_state77_lower <= 1.000001e+06
 R341: - 1e+06 y_state67_action0 + x_reward0_state67_upper
   - x_reward0_state77_upper >= -999999
 R342: 1e+06 y_state68_action0 + x_reward0_state68_lower
   - x_reward0_state78_lower <= 1.000001e+06
 R343: - 1e+06 y_state68_action0 + x_reward0_state68_upper
   - x_reward0_state78_upper >= -999999
 R344: 1e+06 y_state69_action2 - x_reward0_state68_lower
   + x_reward0_state69_lower <= 1.000001e+06
 R345: - 1e+06 y_state69_action2 - x_reward0_state68_upper
   + x_reward0_state69_upper >= -999999
 R346: 1e+06 y_state70_action2 - x_reward0_state69_lower
   + x_reward0_state70_lower <= 1.000001e+06
 R347: - 1e+06 y_state70_action2 - x_reward0_state69_upper
   + x_reward0_state70_upper >= -999999
 R348: 1e+06 y_state70_action1 + x_reward0_state70_lower
   - x_reward0_state71_lower <= 1.000001e+06
 R349: - 1e+06 y_state70_action1 + x_reward0_state70_upper
   - x_reward0_state71_upper >= -999999
 R350: 1e+06 y_state71_action0 + x_reward0_state71_lower
   - x_reward0_state81_lower <= 1.000001e+06
 R351: - 1e+06 y_state71_action0 + x_reward0_state71_upper
   - x_reward0_state81_upper >= -999999
 R352: 1e+06 y_state72_action0 + x_reward0_state72_lower
   - x_reward0_state82_lower <= 1.000001e+06
 R353: - 1e+06 y_state72_action0 + x_reward0_state72_upper
   - x_reward0_state82_upper >= -999999
 R354: 1e+06 y_state73_action0 + x_reward0_state73_lower
   - x_reward0_state83_lower <= 1.000001e+06
 R355: - 1e+06 y_state73_action0 + x_reward0_state73_upper
   - x_reward0_state83_upper >= -999999
 R356: 1e+06 y_state74_action2 - x_reward0_state73_lower
   + x_reward0_state74_lower <= 1.000001e+06
 R357: - 1e+06 y_state74_action2 - x_reward0_state73_upper
   + x_reward0_state74_upper >= -999999
 R358: 1e+06 y_state75_action2 - x_reward0_state74_lower
   + x_reward0_state75_lower <= 1.000001e+06
 R359: - 1e+06 y_state75_action2 - x_reward0_state74_upper
   + x_reward0_state75_upper >= -999999
 R360: 1e+06 y_state75_action1 + x_reward0_state75_lower
   - x_reward0_state76_lower <= 1.000001e+06
 R361: - 1e+06 y_state75_action1 + x_reward0_state75_upper
   - x_reward0_state76_upper >= -999999
 R362: 1e+06 y_state76_action0 + x_reward0_state76_lower
   - x_reward0_state86_lower <= 1.000001e+06
 R363: - 1e+06 y_state76_action0 + x_reward0_state76_upper
   - x_reward0_state86_upper >= -999999
 R364: 1e+06 y_state77_action0 + x_reward0_state77_lower
   - x_reward0_state87_lower <= 1.000001e+06
 R365: - 1e+06 y_state77_action0 + x_reward0_state77_upper
   - x_reward0_state87_upper >= -999999
 R366: 1e+06 y_state79_action2 - x_reward0_state78_lower
   + x_reward0_state79_lower <= 1.000001e+06
 R367: - 1e+06 y_state79_action2 - x_reward0_state78_upper
   + x_reward0_state79_upper >= -999999
 R368: 1e+06 y_state80_action2 - x_reward0_state79_lower
   + x_reward0_state80_lower <= 1.000001e+06
 R369: - 1e+06 y_state80_action2 - x_reward0_state79_upper
   + x_reward0_state80_upper >= -999999
 R370: 1e+06 y_state81_action2 - x_reward0_state80_lower
   + x_reward0_state81_lower <= 1.000001e+06
 R371: - 1e+06 y_state81_action2 - x_reward0_state80_upper
   + x_reward0_state81_upper >= -999999
 R372: 1e+06 y_state82_action2 - x_reward0_state81_lower
   + x_reward0_state82_lower <= 1.000001e+06
 R373: - 1e+06 y_state82_action2 - x_reward0_state81_upper
   + x_reward0_state82_upper >= -999999
 R374: 1e+06 y_state82_action1 + x_reward0_state82_lower
   - x_reward0_state83_lower <= 1.000001e+06
 R375: - 1e+06 y_state82_action1 + x_reward0_state82_upper
   - x_reward0_state83_upper >= -999999
 R376: 1e+06 y_state83_action3 <= 1e+06
 R377: - 1e+06 y_state83_action3 >= -1e+06
 R378: 1e+06 y_state84_action2 - x_reward0_state83_lower
   + x_reward0_state84_lower <= 1.000001e+06
 R379: - 1e+06 y_state84_action2 - x_reward0_state83_upper
   + x_reward0_state84_upper >= -999999
 R380: 1e+06 y_state85_action2 - x_reward0_state84_lower
   + x_reward0_state85_lower <= 1.000001e+06
 R381: - 1e+06 y_state85_action2 - x_reward0_state84_upper
   + x_reward0_state85_upper >= -999999
 R382: 1e+06 y_state86_action2 - x_reward0_state85_lower
   + x_reward0_state86_lower <= 1.000001e+06
 R383: - 1e+06 y_state86_action2 - x_reward0_state85_upper
   + x_reward0_state86_upper >= -999999
 R384: 1e+06 y_state87_action2 - x_reward0_state86_lower
   + x_reward0_state87_lower <= 1.000001e+06
 R385: - 1e+06 y_state87_action2 - x_reward0_state86_upper
   + x_reward0_state87_upper >= -999999
Bounds
 Constant = 1
Binaries
 y_state0_action0 y_state0_action1 y_state1_action1 y_state2_action0
 y_state2_action1 y_state3_action1 y_state4_action0 y_state4_action1
 y_state5_action0 y_state5_action1 y_state6_action1 y_state7_action0
 y_state7_action1 y_state8_action1 y_state9_action0 y_state10_action0
 y_state11_action0 y_state12_action0 y_state13_action0 y_state14_action0
 y_state15_action0 y_state16_action1 y_state17_action0 y_state18_action0
 y_state19_action0 y_state20_action1 y_state21_action0 y_state22_action0
 y_state23_action0 y_state24_action0 y_state25_action2 y_state26_action2
 y_state26_action1 y_state27_action0 y_state28_action0 y_state29_action0
 y_state30_action2 y_state31_action2 y_state31_action1 y_state32_action0
 y_state33_action0 y_state34_action0 y_state35_action2 y_state36_action2
 y_state37_action2 y_state38_action2 y_state38_action1 y_state39_action0
 y_state40_action2 y_state41_action2 y_state42_action2 y_state43_action2
 y_state44_action0 y_state44_action1 y_state45_action1 y_state46_action0
 y_state46_action1 y_state47_action1 y_state48_action0 y_state48_action1
 y_state49_action0 y_state49_action1 y_state50_action1 y_state51_action0
 y_state51_action1 y_state52_action1 y_state53_action0 y_state54_action0
 y_state55_action0 y_state56_action0 y_state57_action0 y_state58_action0
 y_state59_action0 y_state60_action1 y_state61_action0 y_state62_action0
 y_state63_action0 y_state64_action1 y_state65_action0 y_state66_action0
 y_state67_action0 y_state68_action0 y_state69_action2 y_state70_action2
 y_state70_action1 y_state71_action0 y_state72_action0 y_state73_action0
 y_state74_action2 y_state75_action2 y_state75_action1 y_state76_action0
 y_state77_action0 y_state79_action2 y_state80_action2 y_state81_action2
 y_state82_action2 y_state82_action1 y_state83_action3 y_state84_action2
 y_state85_action2 y_state86_action2 y_state87_action2
End
