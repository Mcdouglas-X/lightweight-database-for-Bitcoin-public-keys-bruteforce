#@Mcdouglas-X
import secp256k1 as ice
from bitstring import BitArray


print("Making Binary Data-Base")

target__multi_public_keys = "rand_subtract.txt"

with open(target__multi_public_keys, 'r') as f:

    lines= f.readlines()
    X = len(lines)
    
    for line in lines:
       
        mk= ice.pub2upub(str(line.strip()[:66]))

        num = 128 # number of keys for each pub in rand_substract.txt.

        subtract= 1 #amount to subtract each time.

        subtract_pub= ice.scalar_multiplication(subtract)

        res= ice.point_loop_subtraction(num, mk, subtract_pub)
        
        binary = ''
        for t in range (num):

            h= (res[t*65:t*65+65]).hex()
            hc= int(h[2:], 16)
                
                
            if hc % 2 == 0:
                
                binary+= ''.join('0')
                    
            else:
                binary+= ''.join('1')
                

        my_str = BitArray(bin=binary)

        binary_file = open('multi-data-base.bin', 'ab')
        my_str.tofile(binary_file)
        binary_file.close()


        
        

            

