def print_matrix(cipher_text):
    output_matrix = create_prob_matrix(cipher_text)

    for row in output_matrix:
        print(''.join(row))

    print()

    altered_rows = []
    for i in range(0, len(output_matrix), 2):
        altered_rows.append(output_matrix[i + 1])
        altered_rows.append(output_matrix[i])

    for row in altered_rows:
        print(''.join(row))


#todo: incomplete
def search_for_word(cipher_text, word):
    search_matrix = create_prob_matrix(cipher_text)

    current = 0
    for i in range(0, len(cipher_text)):
        print(search_matrix[i][current])
        if search_matrix[i][current] == word[current]:
            current += 1


def create_prob_matrix(cipher_text, amount_of_key_probabilities=10):
    # 2d matrix length [amount_of_key_probabilities * 5][cipher_text]
    output_matrix = [[0] * len(cipher_text) for _ in range((amount_of_key_probabilities * 2))]
    for ind, letter in enumerate(cipher_text):
        if str.isalpha(letter):
            for i in range(0, amount_of_key_probabilities):
                output_matrix[(i * 2)][ind] = str(running_key_prob_dict[letter][i][0])
                output_matrix[((i * 2) + 1)][ind] = str(running_key_prob_dict[letter][i][1])
        else:
            raise Exception("Ciphertext contained illegal character " + str(letter))

    return output_matrix


def main():
    cipher_text = str.upper(''.join(input("Enter cipher text:").split()))

    while True:
        operation_type = str.lower(input("press 'p' to print probability matrix, press 's' to search for word (crib)"))

        if operation_type == 'p':
            print(cipher_text)
            print_matrix(cipher_text)
            break
        elif operation_type == 's':
            # search_word = str.upper(input("word to search for: "))
            # search_for_word(cipher_text, search_word)
            break
        else:
            print("invalid response")
            continue


if __name__ == "__main__":
    running_key_prob_dict = {
        'A': ['HT', 'IS', 'AA', 'EW', 'NN', 'MO', 'LP', 'GU', 'CY', 'FV', 'JR', 'DX'],
        'B': ['IT', 'NO', 'HU', 'AB', 'DY', 'FW', 'MP', 'KR', 'GV', 'EX', 'JS', 'LQ'],
        'C': ['OO', 'EY', 'LR', 'AC', 'IU', 'NP', 'HV', 'KS', 'GW', 'JT', 'BB', 'FX'],
        'D': ['AD', 'LS', 'OP', 'MR', 'HW', 'KT', 'IV', 'FY', 'BC', 'EZ', 'NQ', 'JU'],
        'E': ['AE', 'NR', 'LT', 'IW', 'MS', 'BD', 'GY', 'CC', 'KU', 'PP', 'HX', 'OQ'],
        'F': ['OR', 'NS', 'MT', 'BE', 'AF', 'HY', 'CD', 'LU', 'IX', 'KV', 'JW', 'PQ'],
        'G': ['NT', 'OS', 'CE', 'AG', 'IY', 'PR', 'DD', 'MU', 'LV', 'BF', 'KW', 'HZ'],
        'H': ['OT', 'DE', 'AH', 'NU', 'PS', 'LW', 'CF', 'BG', 'MV', 'QR', 'IZ', 'JY'],
        'I': ['EE', 'AI', 'OU', 'RR', 'PT', 'DF', 'BH', 'NV', 'MW', 'CG', 'KY', 'LX'],
        'J': ['RS', 'EF', 'CH', 'NW', 'BI', 'DG', 'LY', 'OV', 'PU', 'AJ', 'QT', 'MX'],
        'K': ['RT', 'DH', 'EG', 'SS', 'CI', 'OW', 'AK', 'MY', 'FF', 'PV', 'NX', 'LZ'],
        'L': ['EH', 'ST', 'AL', 'DI', 'RU', 'NY', 'PW', 'FG', 'BK', 'OX', 'CJ', 'MZ'],
        'M': ['EI', 'TT', 'AM', 'SU', 'OY', 'FH', 'BL', 'RV', 'CK', 'GG', 'DJ', 'NZ'],
        'N': ['AN', 'TU', 'FI', 'RW', 'GH', 'CL', 'SV', 'PY', 'BM', 'DK', 'EJ', 'OZ'],
        'O': ['AO', 'HH', 'DL', 'SW', 'GI', 'BN', 'EK', 'TV', 'CM', 'UU', 'RX', 'FJ'],
        'P': ['EL', 'HI', 'TW', 'CN', 'AP', 'RY', 'BO', 'DM', 'UV', 'FK', 'SX', 'GJ'],
        'Q': ['EM', 'DN', 'II', 'CO', 'SY', 'FL', 'UW', 'BP', 'GK', 'TX', 'HJ', 'AW'],
        'R': ['EN', 'AR', 'DO', 'TY', 'GL', 'CP', 'FM', 'HK', 'VW', 'IJ', 'SZ', 'UX'],
        'S': ['EO', 'AS', 'HL', 'FN', 'BR', 'DP', 'UY', 'IK', 'GM', 'WW', 'TZ', 'CQ'],
        'T': ['AT', 'IL', 'EP', 'FO', 'CR', 'HM', 'GN', 'BS', 'VY', 'DQ', 'WX', 'UZ'],
        'U': ['HN', 'DR', 'AU', 'CS', 'IM', 'GO', 'BT', 'WY', 'FP', 'EQ', 'JL', 'KK'],
        'V': ['ER', 'IN', 'HO', 'DS', 'CT', 'AV', 'BU', 'GP', 'KL', 'JM', 'XY', 'FQ'],
        'W': ['ES', 'IO', 'DT', 'AW', 'FR', 'HP', 'LL', 'CU', 'YY', 'KM', 'BV', 'JN'],
        'X': ['ET', 'FS', 'IP', 'GR', 'DU', 'LM', 'KN', 'BW', 'CV', 'AX', 'JO', 'HQ'],
        'Y': ['HR', 'EU', 'LN', 'FT', 'AY', 'GS', 'CW', 'KO', 'DV', 'MM', 'IQ', 'JP'],
        'Z': ['IR', 'HS', 'LO', 'GT', 'MN', 'EV', 'DW', 'FU', 'BY', 'KP', 'AZ', 'CX']}

    main()
