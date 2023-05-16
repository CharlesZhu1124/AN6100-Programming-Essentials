from flask import Flask, Response,request, render_template, session, redirect
from typing import Any, Dict, Optional
import pandas as pd

app = Flask(__name__, static_url_path='/resource')
app.config["JSON_AS_ASCII"] = False

#initialize the database df
global df
df = pd.DataFrame(columns=['id', 'name'])
# df=df.append({'ID':'A1','Product_Name':'Iphone'},ignore_index=True)
# df=df.append({'ID':'A2','Product_Name':'HUAWEI'},ignore_index=True)

#my student info
@app.route('/')
def index():
    return 'Group A, Index G2200626G, Zhu Wentao'

#Display all the products present in the database
#If the database is empty, the program will show an error message to ask the user to add data
@app.route('/a/products/all')
def display_products():
    if df.shape[0]==0:
        return 'The database is empty, please add more data.'
    else:
        return render_template('display.html', tables=[df.to_html(classes='data',index=0)], titles=['Product Database Display'])

#Additional Function: with this url, user can enter a interface to search the name of the product ID he/she wants
@app.route('/a/product/search',methods=['GET','POST'])
def search_product_ui():
    if request.method == 'POST':
        product_id = str(request.form.get('pid'))
        temp_df = df[df['id'] == product_id]
        product_name=''
        if  temp_df.shape[0]==0:
            product_name='No Product with this id'
        else:
            product_name=temp_df.iloc[0, 1]
        return (render_template("search.html", result1=product_id, result2=product_name))
    else:
        return (render_template("search.html", result1="waiting", result2="waiting"))

#Search for products on the basis of ‘id’ and return the product name
@app.route('/a/product',methods=['GET'])
def search_product():
    product_id=str(request.args.get('id'))
    temp_df=df[df['id'] == product_id]
    if temp_df.shape[0]==0:
        return 'ERROR! No product with id %s!'%product_id
    else:
        product_name = temp_df.iloc[0, 1]
        return 'The product name of [id : %s] is %s.'%(product_id,product_name)

#Add a new product to the database with id as value1 and name of product as value2
#If the id already exists, it will show a error message with the current product id and name
@app.route('/a/product/add',methods=['GET'])
def add_product():
    product_id=str(request.args.get('id'))
    product_name=str(request.args.get('name'))
    temp_df = df[df['id'] == product_id]
    if temp_df.shape[0]==0:
        df.loc[len(df)]=[product_id,product_name]
        return '[id : %s  name : %s] has been successfully added to the database.' % (product_id, product_name)
    else:
        product_id2=temp_df.iloc[0,0]
        product_name2 = temp_df.iloc[0, 1]
        return 'ERROR! [id : %s] exists with Product %s.'%(product_id2, product_name2)

#Additional Function: with url /a/downloadcsv , the user can download the csv file of the database into his/her computer
def generate_download_headers(extension: str, filename: Optional[str] = None) -> Dict[str, Any]:
    filename = 'Product_Database'
    content_disp = f"attachment; filename={filename}.{extension}"
    headers = {"Content-Disposition": content_disp}
    return headers

@app.route("/a/downloadcsv")
def csv():
    csv_bin_data = df.to_csv(index=True, encoding="utf-8")  # 生成csv二进制流

    return Response(
        csv_bin_data,
        status=200,
        headers=generate_download_headers("csv"),
        mimetype="application/csv",
    )

if __name__ == '__main__':
    app.run()