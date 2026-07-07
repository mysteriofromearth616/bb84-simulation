import random
num_photons = 80

#Alice

alice_bits = []
for _ in range(num_photons):
    alice_bits.append(random.randint(0,1))
print("Alice`s Bits",alice_bits)

alice_bases = []
for _ in range(num_photons):
    alice_bases.append(random.choice(["R","D"]))
print("Alice`s basis",alice_bases)

photons_from_alice =[]
for i in range(num_photons):
    photons_from_alice.append((alice_bases[i], alice_bits[i]))
print("Encoded photons from Alice",photons_from_alice)

#Bob

bob_bases =[]
for i in range(num_photons):
    bob_bases.append(random.choice(["R","D"]))
print("Bob`s measurement Bases",bob_bases)

bob_bits =[]
for i in range(num_photons):
    if alice_bases[i]==bob_bases[i]:
        bob_bits.append(alice_bits[i])
    else:
        bob_bits.append(random.randint(0,1))
print("Bob`s measured bits",bob_bits)

#Basis Reconciliation

matching_indices=[]
for i in range(num_photons):
    if alice_bases[i]==bob_bases[i]:
        matching_indices.append(i)
print("Matching Indices:",matching_indices)

#Sifting
alice_key=[]
bob_key=[]

for i in matching_indices:
    alice_key.append(alice_bits[i])
    bob_key.append(bob_bits[i])
print("Alice's Key:", alice_key)
print("Bob's Key:", bob_key)

#Statistics

print(f"Photons sent      : {num_photons}")
print(f"Matching bases    : {len(matching_indices)}")
print(f"Sifted key length : {len(alice_key)}")
print(f"Keys identical    : {alice_key == bob_key}")