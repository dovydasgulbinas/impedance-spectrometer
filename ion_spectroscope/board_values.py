resistors = {
    "register_pairs": [[], [], [], [], [], [], [], [], [], [], []],
    "real_value": [250, 1e3, 4e3, 1.6e4, 64e3, 250e3, 1e6, 4e6, 16e6, 64e6, 240e6],
    "complex_value": [250, 1e3, 4e3, 1.6e4, 64e3, 250e3, 1e6, 4e6, 16e6, 64e6, 240e6],
    "labels": ['250  om ', '1,00 kom', '4,00 kom', '16,0 kom', '64,0 kom', '256  kom',
               '1,00 Mom', '4,00 Mom', '16,0 Mom', '64,0 Mom', '256  Mom'],
    "max_frequency": [2.2e6, 2.2e6, 2.2e6, 2.2e6, .512e6, .128e6, 32e3, 8e3, 2e3, 500,
                      125],
    "hf_resistor_range": range(0, 6),
    "lf_resistor_range": range(6, 11),
}

dif_amps = {
    "ui_dif_amp": ["ON", "OFF"],
    "ui_pos_amp": ["ON", "OFF"],
    "ui_neg_amp": ["ON", "OFF"],
    "ui_gain": ["K=6.8", "K=1.7"],
    "reg_gains":  [int('00001000', 2), int('00000000', 2)],
    "ui_pos_input": ["GND", "Vcc"],
    "ui_neg_input": ["GND", "Vcc"],
}

main_control = {
    "ui_control": ["GUI", "Appl."],
    "ui_meas_rate": ["Fast", "", ""],
    "ui_ref_channel": ["Ch1", "Ch2", "Ch3", "Ch4"]

}

oscilloscope = {
    "ui_ch1_range": ["0.2", "xxx?"],
    "ui_ch1_coupling": ["ACV", "xxx?"],
    "ui_ch2_range": ["0.2", "xxx?"],
    "ui_ch2_coupling": ["ACV", "xxx?"],
    "ui_ch3_range": ["0.2", "xxx?"],
    "ui_ch3_coupling": ["ACV", "xxx?"],
    "ui_ch4_range": ["0.2", "xxx?"],
    "ui_ch4_coupling": ["ACV", "xxx?"],
}