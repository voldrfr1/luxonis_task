from flask import Flask,render_template
import psycopg2

app = Flask(__name__)
def get_db_connection():
    '''
    Opens connection

    Returns
    -------
    conn : connect instance

    '''
    conn =  psycopg2.connect(database = "postgres", user = "postgres", 
                                password = "postgres", host = "database", port = "5432")
    return conn


@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT * FROM flats ORDER BY id DESC LIMIT 500;')
    res = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('index.html', data=res)


#def create_tables():
#    return 'Hello World'

if __name__ == '__main__':
         app.run(host='0.0.0.0', port=8080, debug=True)