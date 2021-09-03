import pyodbc


server = ''   #Enter the SQL Server Name here. Example: 'DESKTOP-JLO7LAQ;'
database = ''   #Enter the Database Name here. Example: 'bot_blaze;'


def sqlconnect():
    """ This function establishes the connection with the database. """
    try:
        return pyodbc.connect('DRIVER={SQL Server};'
                              'SERVER='+server+';'
                              'DATABASE='+database+';'
                              'Trusted_Connection=yes')
    except:
        print ("Conexão falhou. Reveja os parametros passados.")


def last_id():
    """ This SELECT gets the last id of the table. """
    mydb = sqlconnect()
    query = mydb.cursor()
    num = query.execute("""SELECT TOP 1 number
         FROM rolldice_tbo
         ORDER BY id DESC
         """)
    return num.fetchone()


def last_color():
    """ Here we get the last two numbers sorted by id,
        with this information the bot chooses the color to place the bet.
    """
    mydb = sqlconnect()
    query = mydb.cursor()
    ret = query.execute("""SELECT TOP 2 id, number, '', next_id, next_number, next_color 
     FROM (
         SELECT id, 
                number,
                color,
                lead(id) over (order by id) as next_id,
                lead(number) over (order by id) as next_number,
                lead(color) over (order by id) as next_color
         FROM rolldice_tbo
     ) AS t
     WHERE number = ? 
     ORDER BY id DESC """, last_id())
    return ret.fetchall
