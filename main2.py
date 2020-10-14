import destinos
from telegram.ext import Updater, CommandHandler
#import telegram

TOKEN = '1353912374:AAEA39Fwyk7kqJCG2IUnkTp5t5PdK29JbZI'
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    first_name = update.message.from_user.first_name
    message = "Bienvenido {} a La Agencia De Viajes KAMUI".format(first_name)
    message2= '\n 1. Ingrese un comando para iniciar el trámite ' \
              '\n 2. Ingrese /list para mostrar todos los codigos IATA disponibles'\
              '\n 3. Ingrese /origen + IATA Ciudad para seleccionar pais de origen ' \
              '\n 4. Ingrese /destiny + IATA Ciudad para seleccionar pais de destino' \
              '\n 5. Ingrese /registro_nombre + Nombre para registrar nombre de Comprador ' \
              '\n 6. Ingrese /registro_pasajeros + Cantidad de boletos' \
              '\n 7. Ingrese /registro_fecha + dd/mm/aa - dd/mm/aa para saber fecha de viaje' \
              '\n 8. Ingrese /total_a_pagar para saber Valor total a cancelar' \
              '\n 9. Ingrese /reserve  Imprimir TIcket' \
              '\n 10. Ingrese /exit para salir'
    update.message.reply_text(message)
    update.message.reply_text(message2)

class vuelo:
    date=0
    name=0
    departure=0
    landing=0
    price=0
    passsengers=0
    total=0

def registro_nombre(update,context):
 m1="Ingresando tu Nombre completo"
 update.message.reply_text(m1)
 args = context.args

 #args = args[0].upper()

 if len(args) ==0:
  m1 = "Datos Incorrectos"
  update.message.reply_text(m1)
 else:
   m1 = "Datos guardados con exito"
   update.message.reply_text(m1)
 vuelo.name = str(args)
#print(vuelo.name)


def registro_pasajeros(update,context):
 m2 = "Ingresando el numero de asientos "
 pas = context.args
 update.message.reply_text(m2)

 if len(pas) == 0:
    m2 = "Datos Incorrectos"
    update.message.reply_text(m2)

 else:
    m2 = "Datos guardados con exito"
    update.message.reply_text(m2)
 vuelo.passsengers= pas



def registro_fecha(update,context):
 m3 = "Ingresando fecha de viaje"
 update.message.reply_text(m3)
 dat = context.args

 if len(dat) == 0:
     m3 = "Datos Incorrectos"
 else:
  m3 = "Datos guardados con exito"
 vuelo.date= str(dat)
 update.message.reply_text(m3)





def origen (update, context):
    args = context.args
    args = args[0].upper()
    if len(args) == 0:
     msg = 'No has elegido tu ubicación'
    elif len(args) > 0:
        if args in destinos.keys_p:
            msg = 'Usted ha seleccionado su lugar de partida', destinos.keys_p[args]
            vuelo.departure=destinos.keys_p[args]
        else:
            msg  = 'Error en el ingreso de datos'
    #context.bot.sendMessage(chat_id=update.message.chat_id, text=msg)
    update.message.reply_text(msg)
    return args

def destiny(update, context):
    destino = context.args
    destino = destino[0].upper()
    #precio = destino[1].upper()
    if len(destino) == 0:
            msg2 = 'Nos has elegido tu lugar de destino'
    elif len(destino) > 0:
        if destino in destinos.keys_p:
            msg2 = 'Usted ha seleccionado su destino', destinos.keys_p[destino]
            vuelo.price = destinos.keys_p[destino][4]
            vuelo.landing = destinos.keys_p[destino]


        else:
            msg2 = 'Error en el ingreso de datos, vuelva a intentarlo'
          #context.bot.sendMessage(chat_id=update.message.chat_id, text=msg2)
    update.message.reply_text(msg2)
def list(update, context):
    keys = destinos.keys_p.items()
    for key, value in keys:
        message2 = "Los IATA son /country {}".format(key)
        update.message.reply_text(message2)
        for valor in value:
            message3 = "\t {}".format(valor)
            update.message.reply_text(message3)

def exit(update,context):

    message3 = " Gracias por usar nuestros servicios"
    update.message.reply_text(message3)

def reserve(update,context):
   message4 = 'DEPARTURE:' , vuelo.departure
   message5 =  'LANDING:' , vuelo.landing
   message6 = 'DATE:', vuelo.date
   message7 = ' NAME OF RESERVE:', vuelo.name
   message8 = 'No PASSENGERS:' ,vuelo.passsengers
   message9 = 'PRICE UNIT: $ ', vuelo.price
   message10 = 'TOTAL TO PAY: $ ', vuelo.total

   update.message.reply_text(message4)
   update.message.reply_text(message5)
   update.message.reply_text(message6)
   update.message.reply_text(message7)
   update.message.reply_text(message8)
   update.message.reply_text(message9)
   update.message.reply_text(message10)
def total_a_pagar(update,context):
    #vuelo.passsengers= list(map(int, vuelo.passsengers[0]))
    #print(vuelo.passsengers)
    s = [str(i) for i in vuelo.passsengers]  # Converting integers into strings
    result = str("".join(s))  # Join the string values into one string
    print(result)
    print(vuelo.price)
    vuelo.total = int(result) * int(vuelo.price)
    print(vuelo.total)


    message7 = vuelo.total
    update.message.reply_text(message7)



#commandhanler para ejecutar órdenes
start_handler = CommandHandler('start', start)
handler = CommandHandler('origen', origen)
destino_handler = CommandHandler('destiny', destiny)
help_handler = CommandHandler("list", list)
handler_exit = CommandHandler('exit', exit)
reserve_handler = CommandHandler('reserve',reserve)
nombre_handler = CommandHandler('registro_nombre',registro_nombre)
pasajeros_handler = CommandHandler('registro_pasajeros',registro_pasajeros)
fecha_handler = CommandHandler('registro_fecha',registro_fecha)
total_handler = CommandHandler('total_a_pagar',total_a_pagar)


    #añadiendo los handlers
dispatcher.add_handler(start_handler)
dispatcher.add_handler(handler)
dispatcher.add_handler(destino_handler)
dispatcher.add_handler(help_handler)
dispatcher.add_handler(handler_exit)
dispatcher.add_handler(reserve_handler)
dispatcher.add_handler(fecha_handler)
dispatcher.add_handler(nombre_handler)
dispatcher.add_handler(pasajeros_handler)
dispatcher.add_handler(total_handler)


    #dispatcher.add_handler(handler_cancelar)

updater.start_polling() #empezar el bot
updater.idle() #para que espere una respuesta