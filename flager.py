def flager(packet):
    import time #libreria tiempo
    if not hasattr(packet,"wait"): #declaracion variable auxiliar
        packet.global_var("wait",0)
        packet.global_var("terminated",0)
        packet.global_var("elapsed",time.time())
    if (packet["TCP"]["dstport"] == 25565 or packet["TCP"]["srcport"] ==25565) and packet.terminated==0:
        #dfine los ack del paquete, los seq y el tamaño del payload
        ack = int(packet["TCP"]["ack"],16)
        seq = int(packet["TCP"]["seq"],16)
        lenIP = packet["IP"]["len"]
        tam=lenIP-(5+8)*4
        #se definen variables globales
        if not hasattr(packet,"ackesperado"):
            packet.global_var("ackesperado",0)
            packet.global_var("antes",0)
            packet.global_var("despues",0)
            packet.global_var("lost",0)
            packet.global_var("logrados",0)
            packet.global_var("tiempoSuma",0)
            
        #se define si es pushack o ack
        flag=packet["TCP"]["flags"]
        #se guarda el puerto de destino y origen
        sport = packet["TCP"]["srcport"]
        dport = packet["TCP"]["dstport"]
        #print("flag=",flag,"=",int("0x"+str(24),16))
        if flag==24 and sport==25565 and packet.wait!=1: #server envia pshack
            #en caso de que el servidor envie un paquete al cliente
            #este debe responder con un ack, este define el tiempo
            #de envio y se espera una confirmacion para el siguiente paquete
            print("******************")
            print("-----Servidor envio paquete,esperando respuesta.------.")
            packet.global_var("size",tam)
            if packet.ackesperado == 0:
                packet.ackesperado=tam+seq
                packet.antes=time.time()
            
            print("se espera un ack de:",tam+seq)    
            packet.wait=1
        elif flag == 16 and dport==25565 and packet.ackesperado==ack :
            if True: #si es el ack esperado guarda el tiempo y imprime
                print("      RECIBIDO el ack del push anterior!")
                packet.despues=time.time()
                demora = round(1000*(packet.despues-packet.antes),3)
                print("     demoro esta respuesta entre push y ack=",demora,"ms")
                packet.logrados+=1
                packet.tiempoSuma+=demora
                print("               tiempoAck promedio=",packet.tiempoSuma/packet.logrados)
                packet.ackesperado=0
                packet.wait=0
                
        elif (time.time()-packet.antes)>1 and packet.wait!=2:
            #si polymorph no encuentra el paquete ack en 1 segundo
            #ignora esta respuesta y definela como un ack DEMORADO
            packet.lost+=1
            print("            -----------------------------------------------------")
            print("            No se encontro el ack despues de 1 segundo, contador ack demorado:",packet.lost,"-->")
            print("            vs paquetes totales(lost+sucess)=",packet.lost+packet.logrados)
            print("            -----------------------------------------------------")
        
            packet.ackesperado=0
            packet.wait=2
        
        if time.time()-packet.elapsed>=30:
            packet.terminated=1
            print("ANALISIS TERMINADO,tiempo 30 segundos")
            print("Paquetes totales PUSH del servidor capturados=",packet.lost+packet.logrados)
            print("Paquetes totales ACK del cliente para estos push detectados=",packet.logrados)
            print("Tiempo promedio entre un PUSH y un ACK cliente-servidor=",packet.tiempoSuma/packet.logrados,"ms")
        # If the condition is meet
        #print("-----")
    return packet
