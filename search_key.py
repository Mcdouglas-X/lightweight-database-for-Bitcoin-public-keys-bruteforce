#@mcdouglasx
import secp256k1 as ice
import random
from bitstring import BitArray
import time


print("Scanning Binary Sequence")

#Pk: 33185509
#cPub: 03057fbea3a2623382628dde556b2a0698e32428d3cd225f3bd034dca82dd7455a

target_ori = "03057fbea3a2623382628dde556b2a0698e32428d3cd225f3bd034dca82dd7455a"

#range
start= 16777215
end=   33554431

file = open("data-base.bin", "rb")

dat = bytes(file.read())       
start_time = time.time()
while True:

    pk= random.randint(start, end)
    print(pk)
    
    target = ice.scalar_multiplication(pk)

    num = 24 # collision margin.

    sustract= 1 # #amount to subtract each time.

    sustract_pub= ice.scalar_multiplication(sustract)

    res= ice.point_loop_subtraction(num, target, sustract_pub)
    
    binary = ''
    
    binary = ''.join('0' if int((res[t*65:t*65+65]).hex()[2:], 16) % 2 == 0 else '1' for t in range(num))
    
        
    my_str = binary

    b = bytes(BitArray(bin=my_str))
    
    
    
    if b  in dat:

        s = b
        f = dat
        inx = f.find(s)*sustract
        inx_0=inx
        Pk = (int(pk) + int(inx_0))+int(inx_0)*7
        A0 = ice.scalar_multiplication(Pk)
        A1 = A0.hex()
        if target_ori[2:] in A1:
            end_time = time.time()  
            search_time = end_time - start_time
            print("Found")
            B0 = ice.pubkey_to_address(0,1, A0)
            A2 = ice.to_cpub(A1)
            
            data = open("win.txt","a")
            data.write(f"Pk: {Pk}\n")
            data.write(f"cPub: {A2}\n")
            data.write(f"Addr: {B0}\n")
            data.write(f"Search Time: {search_time} seconds\n")
            data.close()
            file.close()
            break
        
        

   

    

    
