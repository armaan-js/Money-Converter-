# Currency converter program

# -------------------------
# Subprograms
# -------------------------
def exchange(gbp, currency):
  if currency == "USD":
    return gbp * 1.3 
    
  elif currency == "Euro":
    return gbp * 1.11
    
  elif currency == "Yuan":
    return gbp * 8.92
    
  elif currency == "Yen":
    return gbp * 138.32
# -------------------------
# Main program
# -------------------------
gbp = int(input())
currency = str(input())
money = exchange(gbp, currency)
print(gbp, "GBP =", money, currency)
