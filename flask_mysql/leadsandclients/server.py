from flask import Flask,render_template,redirect,request,session,flash
from mysqlconnection import connectToMySQL
import datetime
app = Flask(__name__)
app.secret_key = "asddjjiyfudvjbmxcmsc,"

SCHEMA = "lead_gen_business"
@app.route('/')
def index():
    db = connectToMySQL(SCHEMA)
        
    query = "select concat(clients.first_name,clients.last_name) as customer_name, count(domain_name) as number_leads from clients join sites on clients.client_id=sites.client_id group by customer_name;"    
     

    clients_leads = db.query_db(query)
    data=[]
    for client in clients_leads:
        client_data={'y': client['number_leads'],
        'label': client['customer_name']
        }
        data.append(client_data)

    print(clients_leads)
    return render_template("index.html",clients = clients_leads,Customer_data=data)

@app.route('/update',methods=["POST"])
def update():
    db = connectToMySQL(SCHEMA)
        
    query = "select concat(clients.first_name,clients.last_name) as customer_name, count(domain_name) as number_leads from clients, join sites on clients.client_id=sites.client_id group by customer_name where leads.registered_datetime >= '%(start_time)s' AND leads.registered_datetime  < '%(end_time)s';"    
     
    date_one=datetime.datetime.strptime(request.form['start_time'], "%Y-%m-%d")
    date_two=datetime.datetime.strptime(request.form['end_time'], "%Y-%m-%d")

    data = {
        'start_time': date_one,
        'end_time': date_two
    }

    date=db.query_db(query, data)  
    return redirect('/')

            
    
if __name__ == "__main__":
    app.run(debug=True)