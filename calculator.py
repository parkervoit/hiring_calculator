import streamlit as st

st.title("Applicant Calculator")
st.sidebar.title('Field descriptions')
st.sidebar.table({'Fields':['Market Type','Total Orders','Drivers','Attrition Rate','Order Rate','Conversion Rate'],
                  'Description':['Select type of market you are calculating applicant quantity for',
                                'Total order demand in market',
                                'Number of drivers currently in market',
                                'Rate of driver attrition',
                                'Number of orders deliverable per driver',
                                'Rate in which applicants become drivers']})
with st.form("app_calculator"):
    col1, col2 = st.columns(2)
    model = st.radio("Market Type", options = ['New Market','Existing Market'])
    
    with col1: 
        st.header('Totals')
        total_orders = st.number_input(label = 'Total Orders', 
                                        min_value = float(0),
                                        step = float(1))

        drivers = st.number_input(label = 'Drivers', 
                                        min_value = float(0),
                                        step = float(1))    
    with col2: 
        st.header('Rates')
        order_rate = st.number_input(label = 'Order Rate', 
                                        min_value = float(0),
                                        step = float(.25))
        
        attrition_rate = st.number_input(label = 'Attrition Rate', 
                                        min_value = float(0), 
                                        max_value = float(1),
                                        step = float(.02))

        conversion_rate = st.number_input(label = 'Conversion Rate', 
                                        min_value = float(0),
                                        max_value = float(1),
                                        step = float(.02))

    submitted = st.form_submit_button("Calculate!")

def calculate_applicants(model = model,
                         attrition_rate = attrition_rate,
                         total_orders = total_orders,
                         drivers = drivers,
                         order_rate = order_rate,
                         conversion_rate = conversion_rate):
    if model == 'New Market':
        return int(round(((attrition_rate*(total_orders / order_rate)) + (total_orders / order_rate) / conversion_rate),0)), model
    else:
        return int(round(((attrition_rate * drivers) + (total_orders / order_rate) / conversion_rate),0)), model

if submitted:
    with st.container():
        col1, col2 = st.columns(2)
        numapplicants,model = calculate_applicants()
        if model == 'New Market':
            with col1:
                st.metric(label = 'Drivers Lost to Attrition', value = int(round((attrition_rate*(total_orders / order_rate)),0)), delta = None)
                st.metric(label = 'Order Demand', value = total_orders, delta = None)
            with col2:
                st.metric(label = 'Applicants Needed', value = int(numapplicants), delta = None)
                st.metric(label = 'Deliveries per Driver', value = int(total_orders))
            st.write(f'Drivers needed to complete {int(total_orders)} orders : {int(round((total_orders / order_rate),0))}')
            st.write(f'Drivers lost to attrition : {int(round((attrition_rate*(total_orders / order_rate)),0))}')
            st.write(f'Applicants needed to complete {int(total_orders)} orders : {int(round(((total_orders / order_rate) / conversion_rate),0))}')
            st.write(f'Applicants needed : {int(numapplicants)}')
        else: 
            with col1:
                st.metric(label = 'Drivers Lost to Attrition', value = int(round((attrition_rate*(total_orders / order_rate)),0)), delta = None)
                st.metric(label = 'Order Demand', value = total_orders, delta = None)
            with col2:
                st.metric(label = 'Applicants Needed', value = int(numapplicants), delta = None)
                st.metric(label = 'Deliveries per Driver', value = int(total_orders))
            st.write(f'Drivers needed to complete {int(total_orders)} orders : {int(round((total_orders / order_rate),0))}')
            st.write(f'Drivers lost to attrition : {int(round((attrition_rate * drivers),0))}')
            st.write(f'Applicants needed to complete {int(total_orders)} additional orders : {int(round(((total_orders / order_rate) / conversion_rate),0))}')
            st.write(f'Applicants needed : {int(numapplicants)}')