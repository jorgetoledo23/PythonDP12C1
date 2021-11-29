Rut = "1.123.123-0"

data1 = (Rut) # 1.123.123-0
#DELETE FROM tbl_clientes WHERE rut = 1.123.123-0 (MAL)

data2 = (Rut,) # ('1.123.123-0',)
#DELETE FROM tbl_clientes WHERE rut = '1.123.123-0' (BIEN)

print(data1)

print(data2)