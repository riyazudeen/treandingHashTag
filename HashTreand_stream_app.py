import streamlit as st
import requests
import json

teptext = ""
if 'text' not in st.session_state:
   st.session_state.text =""

#when user click the post buttom this funtion will upload the post in database
def postUpload():
    try: 
         if st.session_state.text != "":
            templist= st.session_state.text.split()
            postwords = ""
            hashwords = ""
            for i in templist:
               if i.isalnum() != True:
                  hashwords += f"{i} "
            for i in templist:
               if i.isalpha() == True:
                  postwords += f"{i} "
            #pass your post URL in api_url 
            api_url = ""
            data = {"post":postwords,"hash":hashwords}
            response = requests.post(api_url,json=data)
            if response.status_code == 200:
               st.toast('posted successfully!', icon='🎉')
               st.session_state.text = ""        
         else:
               st.toast('post is empty')
    except Exception as e:
        print(e)
        st.write(response.json())


#when user click the treanding buttom this funtion will get the all data in database
def get_treandingHash():
     #pass your post URL in api_url 
     api_url = ""
     response = requests.get(api_url)
     if response.status_code == 200:
        data = response.json()   
        if data != {}:
           st.title("Treading Hash")
           for i in data['params'].values():
             st.write(i)
             
       # st.toast('Treanding hash successfully!', icon='🎉')
     else:
        st.toast('No Data Found')
        


    
st.title("What's on your mind")
st.text_area ('Enter you Thought\'s',key= 'text')
st.button('post',on_click= postUpload)
st.subheader('Treanding hash')
st.button('Show Trending Hashtags',on_click=get_treandingHash)
st.write(teptext)
   

    
