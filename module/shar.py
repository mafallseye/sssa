import numpy as np
import galois

# Apply GF calculation implement Shamir Secret Share
# system parameter
# field param

n = 10
t = 6
F_num = 2**8
GF256 = galois.GF(F_num)


def distribute_shares(s):
    # Construct the polynomial and distribute the shares
    #
    print('The secret is :', s)
    powers = [i for i in range(t-1, -1, -1)]
    coeffs = [np.random.randint(F_num) for _ in range(t-1)]
    # append the secret as intercept;
    coeffs.append(s)
    p = galois.Poly.Degrees(powers, coeffs, field=GF256)
    print('construct the polynomials:', p)

    # randomly generate n points
    secret_shares = []
    xp = np.random.choice(range(F_num), n, replace=False)
    secret_shares = [str(xi)+'-'+str(int(p(xi).base)) for xi in xp]
    return secret_shares


def reconstruct_secret(collected_shares):
    # reconstruct the secret with collected shares
    if len(collected_shares) != t:
        return np.nan
    x = []
    y = []
    for item in collected_shares:
        xi = int(item.split('-')[0])
        yi = int(item.split('-')[1])
        x.append(xi)
        y.append(yi)

    ss_0 = GF256(0)
    for i in range(t):
        item = GF256(y[i])
        for j in range(t):
            if i != j:
                item *= -1*GF256(x[j])/(GF256(x[i])-GF256(x[j]))
        ss_0 += item
    return int(ss_0.base)


# generate secret shares
secret_shares = distribute_shares(33)

# collect random share
collected_shares = np.random.choice(secret_shares, t, replace=False)
print('Randomly selected t shares \'x-y\':')
print(collected_shares)

recon_secret = reconstruct_secret(collected_shares)
print('Reconstructed secret:', recon_secret)
