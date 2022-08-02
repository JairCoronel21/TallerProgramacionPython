producto = ['manzana','pera','uva','piña','mango','tomate','platano','melon','coco','sandia']
codigo = ['S01','S02','S03','S04','S05','S06','S07','S08','S09','S10']
precio = [10,8,12,7,6,4,8,9,3,5]

impigv = []
importe = []
index = [] 
carrito = []
rpt = 'si'
while rpt.lower() == 'si':
    prod = input('Ingrese el nombre del producto: ')
    carrito.append(prod)
    cod = input('Ingrese el codigo del producto: ')
    for c in codigo:
      if c == cod:
        i = codigo.index(cod)
        print('bien')
        can = input('Ingrese la cantidad deseada: ')   
        index.append(i)
        igv = precio[i] * 0.18  
        
        pre = precio[i] - igv          
        imp = float(can) * pre

        imp2 = float(can) * precio[i]
        impigv.append(imp2)
        importe.append(imp)
        sub = sum(importe)
        print(sub)
        tot = sum(impigv)
        print(tot)
        a = input('Desea continuar?: ')
       
        break
    else:
        print('No') 
        break 
    rpt = a
    

    
    
    


