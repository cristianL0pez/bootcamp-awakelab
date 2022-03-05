
bodega_a = [{}]
bodega_b = [{}]
def envios():
    cliente = input('ingrese el cliente')
    producto=input('ingrese el producto')
    numero_producto = int(input('ingrese numero de producto'))
    direccion = input('ingrese la direccion')
    distancia = int(input('ingrese la distancia de envio'))
    if distancia > 1000:
        print(bodega_b)
        bodega_b.append({'cliente':cliente,'producto':producto,'numero':numero_producto, 'direccion':direccion})
        print('el producto',bodega_b[-1],'sera enviado a la bodega b ')
        for producto in bodega_b:
            if producto>500:
                print('el limite de la bodega es 500 unidades por producto')
    else:
        print(bodega_a)
        bodega_a.append({'cliente':cliente,'producto':producto,'direccion':direccion})
        print(f'el producto',{bodega_b[-1]},'sera enviado a la bodega a ')
        for producto in bodega_b:
            if producto>500:
                print('el limite de la bodega es 500 unidades por producto')


    



