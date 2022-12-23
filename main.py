import streamlit as st

st.set_page_config(page_title="Joe's Gschänkli", page_icon=":notes:")

if 'rimes' not in st.session_state:
    st.session_state['rimes'] = False

st.markdown("""
    # Hi Joe!
    Ig ha es chlises Gedichtli für di vorbereitet.  
    :notes: :notes: :notes: :notes: :notes: :notes: :notes: :notes:
""")
if st.session_state['rimes'] == False:
    st.markdown("""
        Meet Joe, the police officer with panache  
        He trains in jiu jitsu, in top physical form  
        But his true passion is a little more low-key  
        Snapshotting the world, in the early morn  

        He sees beauty in the mundane  
        And art in the everyday  
        Through his lens, the world is reframed  
        In a brilliant, colorful display  

        Joe's a man of many talents, it's true  
        But above all, he fights for what is right and just  
        A guardian angel in uniform, he'll do  
        Whatever it takes to protect and trust  

        He patrols the streets with confidence and grace  
        Ensuring the safety of the human race  
        He's quick on his feet and always alert  
        Never backing down when danger lurks  

        But when he's off duty, Joe is just like you  
        Relaxing with a camera, capturing the view  
        He travels to far-off lands and distant shores  
        Capturing memories that will last forevermore  

        Joe's a man of courage, strength, and heart  
        A true hero, right from the very start  
        But don't let that fool you, he's got a silly side  
        A cop with a sense of humor, he'll never hide  
    """)
else:
    st.markdown("""
        Meet Joe, the police officer with panache  
        He trains in jiu jitsu, in top physical **:red[form]**  
        But his true passion is a little more low-key  
        Snapshotting the world, in the early **:red[morn]**  

        He sees beauty in the **:red[mundane]**  
        And art in the **:blue[everyday]**  
        Through his lens, the world is **:red[reframed]**  
        In a brilliant, colorful **:blue[display]**  

        Joe's a man of many talents, it's **:red[true]**  
        But above all, he fights for what is right and **:blue[just]**  
        A guardian angel in uniform, he'll **:red[do]**  
        Whatever it takes to protect and **:blue[trust]**  

        He patrols the streets with confidence and **:red[grace]**  
        Ensuring the safety of the human **:red[race]**  
        He's quick on his feet and always **:blue[alert]**  
        Never backing down when danger **:blue[lurks]**  

        But when he's off duty, Joe is just like **:red[you]**  
        Relaxing with a camera, capturing the **:red[view]**  
        He travels to far-off lands and distant **:blue[shores]**  
        Capturing memories that will last forever **:blue[more]**  

        Joe's a man of courage, strength, and **:red[heart]**  
        A true hero, right from the very **:red[start]**  
        But don't let that fool you, he's got a silly **:blue[side]**  
        A cop with a sense of humor, he'll never **:blue[hide]**  
           
    """)

if st.button(label="Zeig mr was sech riemt"):

    st.session_state['rimes'] = not st.session_state['rimes']
    st.experimental_rerun()