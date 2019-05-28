from influxdb import DataFrameClient
import matplotlib.pyplot as plt
client = DataFrameClient('mioserver.com', 8086, 'utente', 'password', 'nomedb')

result = client.query("""SELECT mean(value) FROM "cpu_load_short" 
                          WHERE time >= now() 
                          AND time < now() -1d
                          GROUP BY time(15s) fill(null)""")
if 'cpu_load_short' in result:
    y = result['cpu_load_short'].values
    plt.title("cpu_load_short")
    plt.plot(y)
    plt.show()
else: print ("mancano dati")
