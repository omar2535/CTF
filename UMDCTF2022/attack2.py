def decode_the_ciphertexts(list_of_ciphers, key):
    for index, c in enumerate(list_of_ciphers):
        index_of_spaces = {}
        list_of_space_indexes = []

        for index_n, c_n in enumerate(list_of_ciphers):
            if index != index_n:
                c_decoded = hex_decoding(c)
                c_n_decoded = hex_decoding(c_n)

                c_list = make_list_of(c_decoded)
                c_n_list = make_list_of(c_n_decoded)

                c_ord = convert_to_unicode(c_list)
                c_n_ord = convert_to_unicode(c_n_list)

                xor_res = perform_xor_on_dec(c_ord, c_n_ord)
                char_res = convert_unicode_to_char(xor_res)
                find_possible_spaces(char_res, index_of_spaces)

        confirm_possible_spaces(index_of_spaces, list_of_space_indexes)

        get_key(list_of_space_indexes, c, key)


def get_key(index_of_spaces, c, key):
    x = ' ' * 215
    c_decoded = hex_decoding(c)

    c_list = make_list_of(c_decoded)
    space_list = make_list_of(x)

    c_ord = convert_to_unicode(c_list)
    space_ord = convert_to_unicode(space_list)

    xor_res = perform_xor_on_dec(c_ord, space_ord)
    char_res = convert_unicode_to_char(xor_res)

    for index in index_of_spaces:
        key[index] = char_res[index].encode('hex')


def confirm_possible_spaces(index_of_spaces, list_of_space_indexes):
    for index, num_spaces in index_of_spaces.items():
        if num_spaces >= 10:
            list_of_space_indexes.append(index)


def find_possible_spaces(res, dict):
    for index, c in enumerate(res):
        if c.isalpha():
            try:
                dict[index] += 1
            except KeyError:
                dict[index] = 1

    return dict


def convert_unicode_to_char(dec):
    result = []

    for i in range(len(dec)):
        result.append(chr(dec[i]))

    return result


def convert_to_unicode(s):
    s_ord = []

    for i in range(len(s)):
        s_ord += [ord(s[i])]

    return s_ord


def make_list_of(s):
    list = []

    for char in range(len(s)):
        list += [s[char]]

    return list


def hex_decoding(s):
    result = s.decode("hex")
    return result


def perform_xor_on_dec(s1, s2):
    result = []

    if len(s1) < len(s2):
        s1_len = len(s1)
        # s2_len = len(s2)

        new_s2 = s2[:s1_len]

        for i in range(len(s1)):
            result.append(s1[i] ^ new_s2[i])
        return result

    if len(s1) > len(s2):
        # s1_len = len(s1)
        s2_len = len(s2)
        new_s1 = s1[:s2_len]

        for i in range(len(s2)):
            result.append(new_s1[i] ^ s2[i])
        return result

    else:
        for i in range(len(s2)):
            result.append(s1[i] ^ s2[i])
        return result


def decode_the_target(target, key):
    target_decoded = hex_decoding(target)

    target_list = make_list_of(target_decoded)

    target_ord = convert_to_unicode(target_list)

    for index, val in enumerate(key):
        key[index] = val.decode('hex')

    key_ord = convert_to_unicode(key)

    xor_res = perform_xor_on_dec(target_ord, key_ord)
    char_res = convert_unicode_to_char(xor_res)

    ans = "".join(char_res)
    return ans


if __name__ == '__main__':
    c1 = 'c909eb881127081823ecf53b383e8b6cd1a8b65e0b0c3bacef53d83f80fb'
    c2 = 'cf00ec8a5635095d33bfa12a317bc2789eabf95e090c29abe81dd4339ffb'
    c3 = 'c700ec851e72124b6afef52c3f37cf2bcda9f74202426fa2f54f9c3797fb'
    c4 = 'cd0ebe8718365b4f2bebb6277039c469dfecf05419586fb4f658dd2997fb'
    c5 = 'c341ff8b562114552ff0bb2a702cc3649ea0ff5a085f6fb0f51dd93b86f4'
    c6 = 'da13f1801321085738bf9e2e24218b7fdfb9f159190c22a1ba49d43381fb'
    c7 = 'cb0df2c63f721c573ebfba21702fc36e9ea9ee50000c38a5e91ddd7ab0fb'
    target_cipher = 'c913e796023d1c4a2befbd367032d82bdfecf55e02406fa7f548ce2997f4'

    list_of_ciphers = [c1, c2, c3, c4, c5, c6, c7]

    key = ['00'] * 215

    decode_the_ciphertexts(list_of_ciphers, key)
    print "KEY:", key

    ans = decode_the_target(target_cipher, key)

    print "DECRYPTED CIPHERTEXT:", ans
