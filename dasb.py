#Importing libraries
import matplotlib.pyplot as plt
import mysql.connector

#Create Dashboard
def dash():
        #Connecting to database
        mydb = mysql.connector.connect(user='root', password="Arcana000-", host='localhost', database='trfdb')
        mycursor = mydb.cursor()
        check_query = "show tables"
        mycursor.execute(check_query)

        #Gathering the table names in database
        table_list = []
        for table in mycursor:
            tab = table[0]
            table_list.append(tab)
        print(table_list)

        table_name_axis = []
        x_axiss= []
        avg_pedestrian_line = []
        
        ped_00 = 0
        ped_01 = 0
        ped_02 = 0
        ped_03 = 0
        ped_04 = 0
        ped_05 = 0
        ped_06 = 0
        ped_07 = 0
        ped_08 = 0
        ped_09 = 0
        ped_10 = 0
        ped_11 = 0
        ped_12 = 0
        ped_13 = 0
        ped_14 = 0
        ped_15 = 0
        ped_16 = 0
        ped_17 = 0
        ped_18 = 0
        ped_19 = 0
        ped_20 = 0
        ped_21 = 0
        ped_22 = 0
        ped_23 = 0
        for tables in table_list:
            table_name_axis.append(tables)
            download_query = ("""select time, pedestrian from {}""").format(tables)
            
            mycursor.execute(download_query)

            myallData = mycursor.fetchall()

            all_pedestrian = []
            all_time = []
            
            total_coun = 0
            
            
            
            for time, pedestrian in myallData:
                
                total_coun +=1
                #print(time)
                if time[:2] == "00":
                    ped_00 = ped_00 + int(pedestrian)
                if time[:2] == "01":
                    ped_01 = ped_01 + int(pedestrian)
                if time[:2] == "02":
                    ped_02 = ped_02 + int(pedestrian)
                if time[:2] == "03":
                    ped_03 = ped_03 + int(pedestrian)
                if time[:2] == "04":
                    ped_04 = ped_04 + int(pedestrian)
                if time[:2] == "05":
                    ped_05 = ped_05 + int(pedestrian)
                if time[:2] == "06":
                    ped_06 = ped_06 + int(pedestrian)
                if time[:2] == "07":
                    ped_07 = ped_07 + int(pedestrian)
                if time[:2] == "08":
                    ped_08 = ped_08 + int(pedestrian)
                if time[:2] == "09":
                    ped_09 = ped_09 + int(pedestrian)
                if time[:2] == "10":
                    ped_10 = ped_10 + int(pedestrian)
                if time[:2] == "11":
                    ped_11 = ped_11 + int(pedestrian)
                if time[:2] == "12":
                    ped_12 = ped_12 + int(pedestrian)
                if time[:2] == "13":
                    ped_13 = ped_13 + int(pedestrian)
                if time[:2] == "14":
                    ped_14 = ped_14 + int(pedestrian)
                if time[:2] == "15":
                    ped_15 = ped_15 + int(pedestrian)
                if time[:2] == "16":
                    ped_16 = ped_16 + int(pedestrian)
                if time[:2] == "17":
                    ped_17 = ped_17 + int(pedestrian)
                if time[:2] == "18":
                    ped_18 = ped_18 + int(pedestrian)
                if time[:2] == "19":
                    ped_19 = ped_19 + int(pedestrian)
                if time[:2] == "20":
                    ped_20 = ped_20 + int(pedestrian)
                if time[:2] == "21":
                    ped_21 = ped_21 + int(pedestrian)
                if time[:2] == "22":
                    ped_22 = ped_22 + int(pedestrian)
                if time[:2] == "23":
                    ped_23 = ped_23 + int(pedestrian)
                    
                print(ped_23)
                print(ped_00)
                #all_time.append(time)
                #all_pedestrian.append(pedestrian)
            #print(all_time)


            

            # #Calculating average of classes in each table
            # for i in all_pedestrian:
            #     if i != '0':
            #         coun_pedestrian +=1
            #         total_pedestrian = total_pedestrian + float(i)


            
            
        #print(ped_00)
        avg_pedestrian_00 = (ped_00/len(table_list)) if ped_00 != 0 else 0
        avg_pedestrian_01 = (ped_01/len(table_list)) if ped_01 != 0 else 0
        avg_pedestrian_02 = (ped_02/len(table_list)) if ped_02 != 0 else 0
        avg_pedestrian_03 = (ped_03/len(table_list)) if ped_03 != 0 else 0
        avg_pedestrian_04 = (ped_04/len(table_list)) if ped_04 != 0 else 0
        avg_pedestrian_05 = (ped_05/len(table_list)) if ped_05 != 0 else 0
        avg_pedestrian_06 = (ped_06/len(table_list)) if ped_06 != 0 else 0
        avg_pedestrian_07 = (ped_07/len(table_list)) if ped_07 != 0 else 0
        avg_pedestrian_08 = (ped_08/len(table_list)) if ped_08 != 0 else 0
        avg_pedestrian_09 = (ped_09/len(table_list)) if ped_09 != 0 else 0
        avg_pedestrian_10 = (ped_10/len(table_list)) if ped_10 != 0 else 0
        avg_pedestrian_11 = (ped_11/len(table_list)) if ped_11 != 0 else 0
        avg_pedestrian_12 = (ped_12/len(table_list)) if ped_12 != 0 else 0
        avg_pedestrian_13 = (ped_13/len(table_list)) if ped_13 != 0 else 0
        avg_pedestrian_14 = (ped_14/len(table_list)) if ped_14 != 0 else 0
        avg_pedestrian_15 = (ped_15/len(table_list)) if ped_15 != 0 else 0
        avg_pedestrian_16 = (ped_16/len(table_list)) if ped_16 != 0 else 0
        avg_pedestrian_17 = (ped_17/len(table_list)) if ped_17 != 0 else 0
        avg_pedestrian_18 = (ped_18/len(table_list)) if ped_18 != 0 else 0
        avg_pedestrian_19 = (ped_19/len(table_list)) if ped_19 != 0 else 0
        avg_pedestrian_20 = (ped_20/len(table_list)) if ped_20 != 0 else 0
        avg_pedestrian_21 = (ped_21/len(table_list)) if ped_21 != 0 else 0
        avg_pedestrian_22 = (ped_22/len(table_list)) if ped_22 != 0 else 0
        avg_pedestrian_23 = (ped_23/len(table_list)) if ped_23 != 0 else 0
        
        avg_pedestrian_line.append(avg_pedestrian_00)
        avg_pedestrian_line.append(avg_pedestrian_01)
        avg_pedestrian_line.append(avg_pedestrian_02)
        avg_pedestrian_line.append(avg_pedestrian_03)
        avg_pedestrian_line.append(avg_pedestrian_04)
        avg_pedestrian_line.append(avg_pedestrian_05)
        avg_pedestrian_line.append(avg_pedestrian_06)
        avg_pedestrian_line.append(avg_pedestrian_07)
        avg_pedestrian_line.append(avg_pedestrian_08)
        avg_pedestrian_line.append(avg_pedestrian_09)
        avg_pedestrian_line.append(avg_pedestrian_10)
        avg_pedestrian_line.append(avg_pedestrian_11)
        avg_pedestrian_line.append(avg_pedestrian_12)
        avg_pedestrian_line.append(avg_pedestrian_13)
        avg_pedestrian_line.append(avg_pedestrian_14)
        avg_pedestrian_line.append(avg_pedestrian_15)
        avg_pedestrian_line.append(avg_pedestrian_16)
        avg_pedestrian_line.append(avg_pedestrian_17)
        avg_pedestrian_line.append(avg_pedestrian_18)
        avg_pedestrian_line.append(avg_pedestrian_19)
        avg_pedestrian_line.append(avg_pedestrian_20)
        avg_pedestrian_line.append(avg_pedestrian_21)
        avg_pedestrian_line.append(avg_pedestrian_22)
        avg_pedestrian_line.append(avg_pedestrian_23)
        
        for i in range(24):
            x_axiss.append(i)
            
        #Plotting the graph
        plt.plot(x_axiss, avg_pedestrian_line, label = "Pedestrian")
    
        #Showing graph
        plt.legend()
        plt.title("Pedestrian Detection Graph")
        plt.xlabel("Time")
        plt.ylabel("Average of Pedestrian")
        plt.show()

#Calling function
dash()