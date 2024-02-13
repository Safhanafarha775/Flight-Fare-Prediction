import sys
from tkinter import *
from tkcalendar import *
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt

def ml_gui():
    
    import pandas as pd
    #read cleaned dataset
    dataset=pd.read_excel('fareset.xlsx')
    
    #feature selection
    X = dataset.loc[:,['Total_Stops', 'journey_day', 'journey_month', 'dep_hour',
       'dep_min', 'Air Asia', 'Air India', 'GoAir', 'IndiGo', 'Jet Airways',
       'Jet Airways Business', 'Multiple carriers',
       'Multiple carriers Premium economy', 'SpiceJet', 'Trujet', 'Vistara',
       'Vistara Premium economy', 'Chennai', 'Delhi', 'Kolkata', 'Mumbai',
       'Destination_Cochin', 'Destination_Delhi', 'Destination_Hyderabad',
       'Destination_Kolkata', 'Destination_New Delhi']]
    y = dataset.iloc[:, 1]
    
    #split data into train and test
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)
    
    #Train the model
    from sklearn.ensemble import RandomForestRegressor
    rf_reg = RandomForestRegressor()
    rf_reg.fit(X_train, y_train)
    
    #collecting departure date and converting into day and month
    date_dep=cal1.get_date()
    journey_day = int(pd.to_datetime(date_dep).day)
    journey_month = int(pd.to_datetime(date_dep).month)
    
    # Departure
    dep_hour=int(dephour.get())
    dep_min=int(depmin.get())
    
    #total stops
    Total_stops=stop_data.get()
    
    #source
    Source=source_data.get()
    if (Source == 'Delhi'):
        Delhi = 1
        Kolkata = 0
        Mumbai = 0
        Chennai = 0

    elif (Source == 'Kolkata'):
        Delhi = 0
        Kolkata = 1
        Mumbai = 0
        Chennai = 0

    elif (Source == 'Mumbai'):
        Delhi = 0
        Kolkata = 0
        Mumbai = 1
        Chennai = 0

    elif (Source == 'Chennai'):
        Delhi = 0
        Kolkata = 0
        Mumbai = 0
        Chennai = 1

    else:
        Delhi = 0
        Kolkata = 0
        Mumbai = 0
        Chennai = 0
        
    #destination
    destination=dest_data.get()
    if (destination== 'Cochin'):
        Destination_Cochin = 1
        Destination_Delhi = 0
        Destination_Hyderabad = 0
        Destination_Kolkata = 0
        Destination_New_Delhi=0
    
    elif (destination == 'Delhi'):
        Destination_Cochin = 0
        Destination_Delhi = 1
        Destination_Hyderabad = 0
        Destination_Kolkata = 0
        Destination_New_Delhi=0

    elif (destination == 'Hyderabad'):
        Destination_Cochin = 0
        Destination_Delhi = 0
        Destination_Hyderabad = 1
        Destination_Kolkata = 0
        Destination_New_Delhi=0

    elif (destination == 'Kolkata'):
        Destination_Cochin = 0
        Destination_Delhi = 0
        Destination_Hyderabad = 0
        Destination_Kolkata = 1
        Destination_New_Delhi=0
        
    elif (destination == 'New Delhi'):
        Destination_Cochin = 0
        Destination_Delhi = 0
        Destination_Hyderabad = 0
        Destination_Kolkata = 1
        Destination_New_Delhi=0

    else:
        Destination_Cochin = 0
        Destination_Delhi = 0
        Destination_Hyderabad = 0
        Destination_Kolkata = 0
        Destination_New_Delhi=0
    
    #airline
    airline=airline_data.get()
    if (airline=='Air Asia'):
        Air_Asia=1
        Air_India=0
        GoAir=0
        Indigo=0
        Jet_Airways=0
        Jet_Airways_Business=0
        Multiple_carriers=0
        Multiple_carriers_Premium_economy=0
        SpiceJet=0
        Trujet=0
        Vistara=0
        Vistara_Premium_economy=0
        
    elif (airline=='Air India'):
        Air_Asia=0
        Air_India=1
        GoAir=0
        Indigo=0
        Jet_Airways=0
        Jet_Airways_Business=0
        Multiple_carriers=0
        Multiple_carriers_Premium_economy=0
        SpiceJet=0
        Trujet=0
        Vistara=0
        Vistara_Premium_economy=0
        
    elif (airline=='GoAir'):
        Air_Asia=0
        Air_India=0
        GoAir=1
        Indigo=0
        Jet_Airways=0
        Jet_Airways_Business=0
        Multiple_carriers=0
        Multiple_carriers_Premium_economy=0
        SpiceJet=0
        Trujet=0
        Vistara=0
        Vistara_Premium_economy=0
        
    elif (airline=='Indigo'):
       Air_Asia=0
       Air_India=0
       GoAir=0
       Indigo=1
       Jet_Airways=0
       Jet_Airways_Business=0
       Multiple_carriers=0
       Multiple_carriers_Premium_economy=0
       SpiceJet=0
       Trujet=0
       Vistara=0
       Vistara_Premium_economy=0
    
    elif (airline=='Jet Airways'):
        Air_Asia=0
        Air_India=0
        GoAir=0
        Indigo=0
        Jet_Airways=1
        Jet_Airways_Business=0
        Multiple_carriers=0
        Multiple_carriers_Premium_economy=0
        SpiceJet=0
        Trujet=0
        Vistara=0
        Vistara_Premium_economy=0
        
    elif (airline=='Jet Airways Business'):
        Air_Asia=0
        Air_India=0
        GoAir=0
        Indigo=0
        Jet_Airways=0
        Jet_Airways_Business=1
        Multiple_carriers=0
        Multiple_carriers_Premium_economy=0
        SpiceJet=0
        Trujet=0
        Vistara=0
        Vistara_Premium_economy=0
        
    elif (airline=='Multiple carriers'):
        Air_Asia=0
        Air_India=0
        GoAir=0
        Indigo=0
        Jet_Airways=0
        Jet_Airways_Business=0
        Multiple_carriers=1
        Multiple_carriers_Premium_economy=0
        SpiceJet=0
        Trujet=0
        Vistara=0
        Vistara_Premium_economy=0
        
    elif (airline=='Multiple carriers Premium economy'):
        Air_Asia=0
        Air_India=0
        GoAir=0
        Indigo=0
        Jet_Airways=0
        Jet_Airways_Business=0
        Multiple_carriers=0
        Multiple_carriers_Premium_economy=1
        SpiceJet=0
        Trujet=0
        Vistara=0
        Vistara_Premium_economy=0
        
    elif (airline=='SpiceJet'):
       Air_Asia=0
       Air_India=0
       GoAir=0
       Indigo=0
       Jet_Airways=0
       Jet_Airways_Business=0
       Multiple_carriers=0
       Multiple_carriers_Premium_economy=0
       SpiceJet=1
       Trujet=0
       Vistara=0
       Vistara_Premium_economy=0
        
    elif (airline=='Trujet'):
        Air_Asia=0
        Air_India=0
        GoAir=0
        Indigo=0
        Jet_Airways=0
        Jet_Airways_Business=0
        Multiple_carriers=0
        Multiple_carriers_Premium_economy=0
        SpiceJet=0
        Trujet=1
        Vistara=0
        Vistara_Premium_economy=0

    elif (airline=='Vistara'):
        Air_Asia=0
        Air_India=0
        GoAir=0
        Indigo=0
        Jet_Airways=0
        Jet_Airways_Business=0
        Multiple_carriers=0
        Multiple_carriers_Premium_economy=0
        SpiceJet=0
        Trujet=0
        Vistara=1
        Vistara_Premium_economy=0

    else:
        Air_Asia=0
        Air_India=0
        GoAir=0
        Indigo=0
        Jet_Airways=0
        Jet_Airways_Business=0
        Multiple_carriers=0
        Multiple_carriers_Premium_economy=0
        SpiceJet=0
        Trujet=0
        Vistara=0
        Vistara_Premium_economy=1
        
  
    df=pd.DataFrame(columns=['Total_Stops', 'journey_day', 'journey_month', 'dep_hour',
       'dep_min', 'Air Asia', 'Air India', 'GoAir', 'IndiGo', 'Jet Airways',
       'Jet Airways Business', 'Multiple carriers',
       'Multiple carriers Premium economy', 'SpiceJet', 'Trujet', 'Vistara',
       'Vistara Premium economy', 'Chennai', 'Delhi', 'Kolkata', 'Mumbai',
       'Destination_Cochin', 'Destination_Delhi', 'Destination_Hyderabad',
       'Destination_Kolkata', 'Destination_New Delhi'])
    df.loc[0,'Total_Stops']=Total_stops
    df.loc[0,'journey_day']=journey_day
    df.loc[0,'journey_month']=journey_month
    df.loc[0,'dep_hour']=dep_hour
    df.loc[0,'dep_min']=dep_min
    df.loc[0,'Air Asia']=Air_Asia
    df.loc[0,'Air India']=Air_India
    df.loc[0,'GoAir']=GoAir
    df.loc[0,'IndiGo']=Indigo
    df.loc[0,'Jet Airways']=Jet_Airways
    df.loc[0,'Jet Airways Business']=Jet_Airways_Business
    df.loc[0,'Multiple carriers']=Multiple_carriers
    df.loc[0,'Multiple carriers Premium economy']=Multiple_carriers_Premium_economy
    df.loc[0,'SpiceJet']=SpiceJet
    df.loc[0,'Trujet']=Trujet
    df.loc[0,'Vistara']=Vistara
    df.loc[0,'Vistara Premium economy']=Vistara_Premium_economy
    df.loc[0,'Chennai']=Chennai
    df.loc[0,'Delhi']=Delhi
    df.loc[0,'Kolkata']=Kolkata
    df.loc[0,'Mumbai']=Mumbai
    df.loc[0,'Destination_Cochin']=Destination_Cochin
    df.loc[0,'Destination_Delhi']=Destination_Delhi
    df.loc[0,'Destination_Hyderabad']=Destination_Hyderabad
    df.loc[0,'Destination_Kolkata']=Destination_Kolkata
    df.loc[0,'Destination_New Delhi']=Destination_New_Delhi
    
    
    database=df
    
    #prediction
    output=rf_reg.predict(database)
    
    lbl_rslt=Label(window,text='Predicted price : '+str(output),font=20)
    lbl_rslt.place(x='180',y='450')
    
if __name__ == '__main__':
    
    #creating form for accepting data
    global window
    window=Tk()
    window.title('Flight Fare Prediction')
    window.geometry('500x550')
    window.resizable(width=True,height=True)
    window.configure(bg='pink')
    
    

    frame1=Frame(window,bg='pink')
    lbl_dep=Label(frame1,text='Dept Date',font=15,bg='pink')
    lbl_dep.grid(row=0,column=0,padx=10)
    dept_date=StringVar()
    cal1=DateEntry(frame1, width= 20, date_pattern="mm-dd-yyyy",textvariable=dept_date)
    cal1.grid(row=1,column=0,padx=10)
    lbl_deptime=Label(frame1,text='Dept Time',font=15,width=20,bg='pink')
    lbl_deptime.grid(row=0,column=1,padx=10)
    dephour=IntVar()
    sp1=Spinbox(frame1,from_=1,to=24,textvariable=dephour)
    sp1.grid(row=1,column=1)
    depmin=IntVar()
    sp2=Spinbox(frame1,from_=00,to=59,)
    sp2.grid(row=2,column=1)
    frame1.place(x='70',y='80')

    frame2=Frame(window,bg='pink')
    lbl_source=Label(frame2,text='Source',font=15,width=15,bg='pink')
    lbl_source.grid(row=0,column=0,padx=10)
    source_data=StringVar()
    combo1=ttk.Combobox(frame2,state='readonly',
                        values=['Delhi','Kolkata','Banglore','Mumbai','Chennai '],
                        textvariable=source_data)
    combo1.grid(row=1,column=0)
    lbl_dest=Label(frame2,text='Destination',font=15,width=20,bg='pink')
    lbl_dest.grid(row=0,column=1,padx=10)
    dest_data=StringVar()
    combo2=ttk.Combobox(frame2,state='readonly',
                        values=['Cochin','Banglore','Delhi','New Delhi','Hyderabad','Kolkata'],
                        textvariable=dest_data)
    combo2.grid(row=1,column=1)
    frame2.place(x='70',y='190')

    frame3=Frame(window,bg='pink')
    lbl_stop=Label(frame3,text='Stopage',font=15,width=15,bg='pink')
    lbl_stop.grid(row=0,column=0,padx=10)
    stop_data=IntVar()
    combo3=ttk.Combobox(frame3,state='readonly',values=[0,1,2,3,4],textvariable=stop_data)
    combo3.grid(row=1,column=0)
    lbl_airline=Label(frame3,text='Airline',font=15,width=20,bg='pink')
    lbl_airline.grid(row=0,column=1,padx=10)
    airline_data=StringVar()
    combo4=ttk.Combobox(frame3,state='readonly',
                        values=['Air Asia', 'Air India', 'GoAir', 'IndiGo', 'Jet Airways',
                                'Jet Airways Business', 'Multiple carriers',
                                'Multiple carriers Premium economy', 'SpiceJet', 'Trujet', 'Vistara',
                                'Vistara Premium economy'],
                        textvariable=airline_data)
    combo4.grid(row=1,column=1)
    frame3.place(x='70',y='290')

    button=Button(window,text='Submit',bg='blue',command=ml_gui)
    button.place(x='220',y='380')
    

    window.mainloop() 
    
    