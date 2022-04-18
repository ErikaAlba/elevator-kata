from controller import Controller
controller = Controller(8,2) 

while True:
    inputVar = input("Elija llamada (externa 1 o interna 2): ")
    
    if inputVar == '1':
        direccion = int(input("hacia donde quiere ir arriba 1, abajo 2: "))
        piso = int(input("a que piso: "))
        if direccion == 1:
            direccion = "up"
        else:
            direccion = "down"
        controller.outside_calls(piso,direccion)
    elif inputVar == '2':
        elevator = int(input(f"elija ascensor (1-{len(controller.getElevators())}): "))
        go_to = int(input("a que piso quiere ir: "))
        controller.inside_calls(elevator,go_to)
    
        
    
    controller.call_move_elevator()
    controller.render()
     
