# cal_house_price

### 1- create ur notebook --> create a git repo --> create a folder on ur pc and clone the repo --> lunch the vscode from anaconda 
____________________________
### 2- create a conda env 
conda create -n cal_env python=3.10 -y
or in same project folder 
conda create -p ./cal_env python=3.10 -y 
__________________________________
### 3- activate conda activate ./cal_env
### 4- create a requirements.txt file 
### 5- install it using 
pip install -r requirements.txt 

( u can iew the lib and their versions using the command :  pip list )

### 6-  download the : ( model _ notebook _ scaler if u need it _ features name just to keep the features in the same order _data just to upload it also on git but not needed here since that it's already a built in ds )

__________________________________
# Deployment 

# 1- create a streamlit UI  and upload on streamlit cloud 
### 1- create streamlit_app.py 
### 2- run the streamlit _ app  using this command : 
streamlit run streamlit_app.py  

test it then press on terminal and 
ctr +c to stop the app 
### 3- upload everything on ur repo as streamlit version 
## but befor u add anything make sure the env is in gitignore   u can add cal_env/ just in case in the #env section 

 #### 1- git add .
 #### git status here just to make sure  the files are ready 
 #### 2- git commit -m "Streamlit ML app ready"
 #### 3- git push 
# 2- now deploy on streamlit cloud 
  #### 1- create an account using ur git hub acc 
  #### 2-  New app  --> take the url of ur repo 
  ### 3-  branch --> main _ main path file should be detected automatically 
  #### 4- write the name for ur url don't use - not _ 
  ### 5- after deployment u will find ur app runing and share button then copy the link and put it in ur git hub 

 We deployed the Streamlit version for quick demonstration using Streamlit Cloud, and later we will extend the project with Flask and FastAPI for full backend deployment on Render.
 


 _________________________________________________________________
 # Deploy with Flask 
## 1 - create a file called Flask_app.py
## 2- run the flask app using this command 
 python Flask_app.py
##  3- test on postman 
#### open postman --> method = post ____ url = put the url ___ body --> raw= json  __ in the box put the data and make sure to validate it 

###  test on postman using this key values pair
{
  "MedInc": 8.3252,
  "HouseAge": 41,
  "AveRooms": 6.9841,
  "AveBedrms": 1.0238,
  "Population": 322,
  "AveOccup": 2.55,
  "Latitude": 37.88,
  "Longitude": -122.23
}

## now we can deploy on render 
1. Push Flask project → GitHub
### very important change the flask app  befor deployment 
make the code like this ::: 
'''
#run the server
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
''''''

2. Connect GitHub → Render

3. Render deploys automatically
4. take the  live URL and then use it with anyfront end u like 

ctrl+C
git add .
git commit -m "deploying flask api"
git push

_____________
## 4- open render  crete an acc connect it with ur github 
### 5- Create New Web Service 
### 6- puplic repo __ put ur repo url 

#### build commands : 
pip install -r requirements.txt 
start command -->  python Flask_app.py


# then deploy 
