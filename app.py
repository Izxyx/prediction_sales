#Import libraries
from pathlib import Path
import streamlit as st
import pickle
from PIL import Image

# Paths
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir/'styles'/'main.css'

# Configuration
st.set_page_config(page_title='Sales Prediction',page_icon='random')

# Header
with open(css_file) as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)


# Main
def main():
    st.title('Prediction Store Sales')


    with st.expander("Project's Description"):
        st.write(''' 
            The plot shows a tipycal retail store dessign.
            You *must* enter the size and fortniture parameters 
            to predict the sales of the store
        ''')
    options = st.selectbox(
        'Examples:',
        ['Small','Medium','Big'])

    medium = Image.open('./assets/example_areas.png')
    small = Image.open('./assets/example_areas2.png')
    big = Image.open('./assets/example_areas3.png')
    if options == 'Small':
        st.write(options + ' store example')
        st.image(small)
    if options == 'Medium':
        st.write(options + ' store example')
        st.image(medium)
    if options == 'Big':
        st.write(options + ' store example')
        st.image(big)

def main2():
    if st.button('------------->   PREDICT   <-------------',key=5):
        result = predict_model.predict([[square_meters,stockroom_meters,
        salesfloor_meters,useless_meters,
        shelfs,double_shelfs,registers,
        entrances]])

        if square_meters != 0 and salesfloor_meters != 0 and shelfs != 0 and double_shelfs != 0 and registers != 0 and entrances != 0:
            st.success('Super, You did it')
            st.title('\n')
            st.header('Anual Sales:')
            st.title(str(result[0]) + ' Millions')
            st.title('\n')
            st.header('Month Sales')
            st.title(str(result[0]/12) + ' Millions')
            st.balloons()
        else:
            st.error('You should input all the parameters')

if __name__ == '__main__':
    
    with st.sidebar:

        image2 = Image.open('./assets/logo.png')
        with open('./assets/model.pkl','rb') as f:
            predict_model = pickle.load(f)
            st.image(image2)

        st.header('Input store parameters:')
        st.write(''' ***Obligatory Imput*''') 

        square_meters = st.number_input('How size is the store? **')
        st.write(square_meters,' m2')

        stockroom_meters = st.number_input('How size is the stockroom?')
        st.write(stockroom_meters,' m2')

        salesfloor_meters = st.number_input('How size is the sales floor? **')
        st.write(salesfloor_meters,' m2')

        useless_meters = st.number_input('How size is the useless area?')
        st.write(useless_meters,' m2')

        shelfs = st.number_input('How many shelfs? **')
        st.write(shelfs,' shelfs')

        double_shelfs = st.number_input('How many double shelfs? **')
        st.write(double_shelfs,' double shelfs')

        registers = st.number_input('How many registers? **')
        st.write(registers)

        entrances = st.number_input('How long is the entrance? **')
        st.write(entrances,' ml')

    main()
    main2()

    

