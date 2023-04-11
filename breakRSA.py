def common_modulus_attack(ciphertext1, ciphertext2, public_key):
    n, e = public_key
    gcd, s1, s2 = extended_gcd(ciphertext1, ciphertext2)
    if gcd != 1:
        return None
    elif s1 < 0:
        ciphertext1 = pow(pow(ciphertext1, -s1, n), -1, n)
    else:
        ciphertext1 = pow(ciphertext1, s1, n)
    if s2 < 0:
        ciphertext2 = pow(pow(ciphertext2, -s2, n), -1, n)
    else:
        ciphertext2 = pow(ciphertext2, s2, n)
    return (ciphertext1 * ciphertext2) % n
