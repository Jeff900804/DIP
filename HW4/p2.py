# -*- coding: utf-8 -*-
"""
Created on Fri Nov 15 14:40:32 2024

@author: jeff9
"""


import numpy as np
from table import huffman_ac_table
from table import huffman_dc_table


quantized_block = np.array([
    [-10, -3, -6, 2, -1, 0, 0, 0],
    [0, -2, 2, 0, 1, 0, 0, 0],
    [4, 3, 5, -1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, -1, 0, 0, 0, 0, 0],
    [-1, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
])

zigzag_array = [quantized_block[row, col] for row, col in [
    (0, 0), (0, 1), (1, 0), (2, 0), (1, 1), (0, 2), (0, 3), (1, 2),
    (2, 1), (3, 0), (4, 0), (3, 1), (2, 2), (1, 3), (0, 4), (0, 5),
    (1, 4), (2, 3), (3, 2), (4, 1), (5, 0), (6, 0), (5, 1), (4, 2),
    (3, 3), (2, 4), (1, 5), (0, 6), (0, 7), (1, 6), (2, 5), (3, 4),
    (4, 3), (5, 2), (6, 1), (7, 0), (7, 1), (6, 2), (5, 3), (4, 4),
    (3, 5), (2, 6), (1, 7), (2, 7), (3, 6), (4, 5), (5, 4), (6, 3),
    (7, 2), (7, 3), (6, 4), (5, 5), (4, 6), (3, 7), (4, 7), (5, 6),
    (6, 5), (7, 4), (7, 5), (6, 6), (5, 7), (6, 7), (7, 6), (7, 7)
]]
def one_complement(num):
    num = list(str(num))
    size = len(num)
    for i in range(size):
        if num[i] == '0':
            num[i] = '1'
        elif num[i] =='1':
            num[i] = '0'
    return  ''.join(num)


def encode_ac_coefficients(zigzag_array):
    ac_code_stream = []
    run_length = 0
    
    for i in range(1, len(zigzag_array)):
        coeff = zigzag_array[i]
        if coeff == 0:
            run_length += 1
        else:
            
            size = int(np.ceil(np.log2(abs(coeff) + 1)))
            ac_codeword = huffman_ac_table.get((run_length, size), "")
            
            
            if coeff > 0:
                encoded_segment = ac_codeword + format(abs(coeff), 'b').zfill(size)
            elif coeff < 0:
                encoded_segment = ac_codeword + one_complement(format(abs(coeff), 'b').zfill(size))
            ac_code_stream.append(encoded_segment)  
            run_length = 0
    
    
    ac_code_stream.append(huffman_ac_table.get((0, 0), ""))
    
    return ac_code_stream


def encode_dc_coefficient(dc_coefficient, previous_dc):
    diff = dc_coefficient - previous_dc
    size = int(np.ceil(np.log2(abs(diff) + 1))) if diff != 0 else 0
    dc_codeword = huffman_dc_table.get(size, "")
    
    
    if diff > 0:
        encoded_segment = dc_codeword + format(abs(diff), 'b').zfill(size)
    elif diff < 0:
        encoded_segment = dc_codeword + one_complement(format(abs(diff), 'b').zfill(size))
    else:
        encoded_segment = dc_codeword
    
    return encoded_segment

previous_dc = -5
current_dc = zigzag_array[0]

ac_code_segments = encode_ac_coefficients(zigzag_array)
dc_code_segment = encode_dc_coefficient(current_dc, previous_dc)

print("AC Coefficients Code Stream (Segmented):")
for segment in ac_code_segments:
    print(segment)

print("\nDC Coefficient Code Stream:")
print(dc_code_segment)