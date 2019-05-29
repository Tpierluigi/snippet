#importo le librerie: per installare  la libreria influx usare:
#pip install influxdb

from influxdb import DataFrameClient
import matplotlib.pyplot as plt
#imposto un dataframe e ci eseguo la query
client = DataFrameClient('mioserver.com', 8086, 'utente', 'password', 'nomedb')
result = client.query("""SELECT mean(value) FROM "cpu_load_short" 
                          WHERE time >= now() -1d
                          AND time < now() 
                          GROUP BY time(15s) fill(null)""")
#controllo di avere dati (deve esistere la misura selezionata)
if 'cpu_load_short' in result:
    #estraggo i dati in un array e li grafico
    y = result['cpu_load_short'].values
    plt.title("cpu_load_short")
    plt.plot(y)
    plt.show()
else: print ("mancano dati")
