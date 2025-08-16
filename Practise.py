from flask import Flask ,render_template,request,redirect
import os
import csv
from datetime import date



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit',methods=['POST'])
def submit():
    # Date Module
    dt = date.today()
    dt = dt.strftime("%d/%m/%Y")
    Customer_ID = request.form.get('Customer_ID','')
    name = request.form.get('name','')
    Product = request.form.get('Product','')
    Rating  = request.form.get('Rating','')
    Feedback = request.form.get('Feedback','')
    Resolved = request.form.get('Resolved','')
    Follow_up = request.form.get('Follow_up','')


    filename = "Feedback_details.csv" 
    file_exists = os.path.isfile(filename)

    with open(filename ,'a', newline='' ,encoding='utf-8') as file:
        csvwriter = csv.writer(file)
        if not file_exists:
            csvwriter.writerow(["Date","Customer ID","Name","Product","Rating","Feedback","Resolved","Follo_up_Required"])
        csvwriter.writerow([dt,Customer_ID,name,Product,Rating,Feedback,Resolved,Follow_up])

    return render_template('thankyou.html')

if __name__=='__main__':
    app.run(debug = True)













# # Customer ID
# # Name
# # Product  Purchased
# # Rating(1-5)
# # Feedback Comment
# # Resolved(yes/No)
# # Follow-up-Required(Yes/No)

# x = -1

# while x!=0 :
#     customer_ID = int(input("Enter the Customer ID: "))
#     Name =   input("Enter Your Name : ")
#     Product = input("Enter the Product that you have purchased : ")
#     Rating = int(input("Rate the product from 1 to 5 :"))
#     Feedback = input("Leave the Feedback Comment : ")
#     Resolved = input("if any problem resolved or not (Yes/No) : ")
#     Follow_up = input("Follow-up-required(yes/no) : ")
#     x = int(input("press any key to continue / To Exit  press 0 :"))
#     if(x == 0):
#         break



# filename = "Feedback_details.csv"
# with open(filename ,'a', newline="") as file:
#     csvwriter = csv.writer(file)
#     csvwriter.writerow([dt,customer_ID,Name,Product,Rating,Feedback,Resolved,Follow_up])

# file.close()
