#@Mcdouglas-X
import secp256k1 as ice
from bitstring import BitArray
import bitcoin

def generate_binary_data(target_public_key, num_keys, sustract, low_m):
    print("Making Binary Data-Base")

    target = ice.pub2upub(target_public_key)
    lm = num_keys // low_m
    print(lm)

    sustract_pub = ice.scalar_multiplication(sustract)
    res = ice.point_loop_subtraction(lm, target, sustract_pub)

    def process_res(res, lm):
        binary = ''.join('0' if int((res[t*65:t*65+65]).hex()[2:], 16) % 2 == 0 else '1' for t in range(lm))
        return BitArray(bin=binary)

    my_str = process_res(res, lm)
    with open('data-base.bin', 'ab') as binary_file:
        my_str.tofile(binary_file)

    for i in range(1, low_m):
        lm_upub = ice.scalar_multiplication((lm * i) * sustract)
        A1 = ice.point_subtraction(target, lm_upub)
        res = ice.point_loop_subtraction(lm, A1, sustract_pub)
        my_str = process_res(res, lm)
        with open('data-base.bin', 'ab') as binary_file:
            my_str.tofile(binary_file)

target_public_key = "03057fbea3a2623382628dde556b2a0698e32428d3cd225f3bd034dca82dd7455a"
num_keys = 1000000
sustract = 1
low_m = 100

generate_binary_data(target_public_key, num_keys, sustract, low_m)
