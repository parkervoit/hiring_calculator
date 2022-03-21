import streamlit as st

st.title("Applicant Calculator")
with st.form("app_calculator"):
    
    model = st.radio("Market Type", options = ['New Market','Existing Market'])
    
    total_orders = st.number_input(label = 'Total Orders', 
                                    min_value = float(0),
                                    step = float(1))

    drivers = st.number_input(label = 'Drivers', 
                                    min_value = float(0),
                                    step = float(1))    
    
    attrition_rate = st.number_input(label = 'Attrition Rate', 
                                    min_value = float(0), 
                                    max_value = float(1),
                                    step = float(.02))

    order_rate = st.number_input(label = 'Order Rate', 
                                    min_value = float(0),
                                    step = float(.25))
    conversion_rate = st.number_input(label = 'Conversion Rate', 
                                    min_value = float(0),
                                    max_value = float(1),
                                    step = float(.02))

 
    submitted = st.form_submit_button("Calculate")




def calculate_applicants(model = model,
                         attrition_rate = attrition_rate,
                         total_orders = total_orders,
                         drivers = drivers,
                         order_rate = order_rate,
                         conversion_rate = conversion_rate):
    if model == 'New Market':
        return int(round((attrition_rate*(total_orders / order_rate)) + (total_orders / order_rate) / conversion_rate),0)), model
    else:
        return int(round(((attrition_rate * drivers) + (total_orders / order_rate) / conversion_rate),0)), model

if submitted:
    numapplicants,model = calculate_applicants()
    if model == 'New Market':
        st.write(f'Drivers needed to complete {total_orders} orders : {total_orders / order_rate}')
        st.write(f'Drivers lost to attrition : {(attrition_rate*(total_orders / order_rate))}')
        st.write(f'Applicants needed to complete {total_orders} orders : {(total_orders / order_rate) / conversion_rate}')
        st.write(f'Applicants needed : {numapplicants}')
    else: 
        st.write(f'Drivers needed to complete {total_orders} orders : {total_orders / order_rate}')
        st.write(f'Drivers lost to attrition : {(attrition_rate * drivers)}')
        st.write(f'Applicants needed to complete {total_orders} additional orders : {(total_orders / order_rate) / conversion_rate}')
        st.write(f'Applicants needed : {numapplicants}')
