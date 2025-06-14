import  requests
from datetime import datetime

#-----------------------------------YOUR DETAIL----------------------------------------------
USER="YOUR_NAME"
MY_TOKEN="SECRET_TOKEN"
# https://pixe.la/v1/users/{user}/graphs/{graph-id}.html


#-----------------------------------USER CREATION----------------------------------------------
pixela_endpoint="https://pixe.la/v1/users"

user_param={
    "token":MY_TOKEN,
    "username":USER,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}
# response=requests.post(url=pixela_endpoint,json=user_param)


#-----------------------------------GRAPH CREATION----------------------------------------------
headers={
    "X-USER-TOKEN":MY_TOKEN,
}
graph_endpoint=f"{pixela_endpoint}/{USER}/graphs"

GRAPH_ID="graph1"
graph_params={
    "id":GRAPH_ID,
    "name":"code-graph",
    "unit":"Hour",
    "type":"float",
    "color":"shibafu",
    "timezone":"Asia/Kolkata",
}
# response=requests.post(url=graph_endpoint,json=graph_params,headers=headers)



#-----------------------------------POSTING PIXEL----------------------------------------------
# today=datetime(year=2025,month=6,day=9)
today=datetime.now()

pixel_post_endpoint=f"{graph_endpoint}/{GRAPH_ID}"

postPixel_params={
    "date":today.strftime("%Y%m%d"),
    "quantity":input("How many hours did u code? : "),
}
# response=requests.post(url=pixel_post_endpoint,json=postPixel_params,headers=headers)



#-----------------------------------UPDATING PIXEL----------------------------------------------
pixel_endpoint=f"{pixel_post_endpoint}/{today.strftime("%Y%m%d")}"

postUpdate_params={
    "quantity":"2.8",
}
# response=requests.put(url=pixel_endpoint,json=postUpdate_params,headers=headers)



#-----------------------------------DELETING PIXEL----------------------------------------------
# response=requests.delete(url=pixel_endpoint,headers=headers)


