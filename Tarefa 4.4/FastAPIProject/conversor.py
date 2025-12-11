# --- TEMPERATURAS ---
def c_to_f(c):
    return (c * 9/5) + 32

def f_to_c(f):
    return (f - 32) * 5/9

def c_to_k(c):
    return c + 273.15

# --- DISTANCIAS ---
def metros_a_km(m):
    return m / 1000

def km_a_millas(km):
    return km * 0.621371

def millas_a_km(mi):
    return mi * 1.60934

# --- PESOS ---
def kg_a_g(kg):
    return kg * 1000

def g_a_kg(g):
    return g / 1000

def kg_a_lb(kg):
    return kg * 2.20462
