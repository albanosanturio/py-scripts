import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint
print ("SPREADSHEET HANDLER")

#edit git
#le paso scope (api que va a usar) y credenciales (json con mis keys)
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('google-sheets-e0674f296b50.json', scope)
client = gspread.authorize(creds)

#creo archivos y los comparto
#for x in range (2):
#	sh = client.create('A new spreadsheet %s' %x)
#	sh.share('albanosanturio@gmail.com', perm_type='user', role='writer')

#abro el sheet correspondiente en la hoja 1
sheet = client.open('sheet-test').sheet1
prueba = sheet.get_all_records()
print(prueba)

#uso pretty printer para visualizarlo como json en pantalla
pp = pprint.PrettyPrinter()
pp.pprint(prueba)
pp.pprint(sheet.col_values(1))

#escribo sobre celdas, hago una diagonal en este caso
#rompe si tomo celda (0,0) o si me voy de margenes
for x in range(9):
  print(x)
  y=x+1
  sheet.update_cell(y, y, "xxxxx" )


#extraigo valores de determinadas celdas, bajo por columna 1
for x in range(20):
  print(x+1)
  y=x+1
  val = sheet.cell(y, 1).value
  print(val)

