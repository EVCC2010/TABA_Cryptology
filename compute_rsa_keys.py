def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def compute_keys(p, q, e):
    N = p * q
    phi_N = (p - 1) * (q - 1)
    
    # Check if e and phi(N) are coprime
    if gcd(e, phi_N) == 1:
        # Obtain d using the modular inverse
        d = mod_inverse(e, phi_N)
        
        # Public key: {e, N}
        public_key = (e, N)
        
        # Private key: {d, N}
        private_key = (d, N)
        
        print("Step 1: Primes p={}, q={}".format(p, q))
        print("Step 2: Obtain N=p*q={}, ϕ(N)={}, select e={}".format(N, phi_N, e))
        print("Step 3: e and ϕ(N) are coprime (gcd({}, {}) == 1)".format(e, phi_N))
        print("Step 4: Calculate d: de ≡ 1 modϕ(N)")
        print("   => d = (e mod ϕ(N))⁻¹")
        print("   => Using extended Euclidean algorithm:")
        print("   => P({}) + Q({}) = 1".format(e, phi_N))
        print("   => 1 = {}*{} - {}*{}".format(e, mod_inverse(e, phi_N), phi_N, mod_inverse(e, phi_N)))
        print("   => d = (e mod ϕ(N))⁻¹ = {}".format(d))
        print("\nPublic key:", public_key)
        print("Private key:", private_key)
        
        return public_key, private_key
    else:
        raise ValueError("e and ϕ(N) are not coprime. Choose a different e.")

# Step 1: Primes p, q
p = 137
q = 101

# Step 2: Obtain N=p*q, ϕ(N), select e
e = 257

# Step 3: Calculate d: de ≡ 1 modϕ(N)
public_key, private_key = compute_keys(p, q, e)

# Step 1: Primes p, q
p = 149
q = 113

# Step 2: Obtain N=p*q, ϕ(N), select e
e = 179

# Step 3: Calculate d: de ≡ 1 modϕ(N)
public_key, private_key = compute_keys(p, q, e)
