import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from numpy import random

def randGen():                                  #Q1 function randGen defined
    write_ptr=open("dataset.txt", "w")
    for k in range(10000):
        age=random.randint(1, 100)
        # print(age)
        gender=random.choice(["Male", "Female"])
        # print(gender)
        states_d={
        "AP":"Andhra Pradesh",
        "AR":"Arunachal Pradesh",
        "AS":"Assam",
        "BR":"Bihar",
        "CH":"Chhattisgarh",
        "GA":"Goa",
        "GJ":"Gujarat",
        "HR":"Haryana",
        "HP":"Himachal Pradesh",
        "JH":"Jharkhand",
        "KA":"Karnataka",
        "KL":"Kerala",
        "MP":"Madhya Pradesh",
        "MH":"Maharashtra",
        "MN":"Manipur",
        "ML":"Meghalaya",
        "MZ":"Mizoram",
        "NL":"Nagaland",
        "OR":"Odisha",
        "PB":"Punjab",
        "RJ":"Rajasthan",
        "SK":"Sikkim",
        "TN":"Tamil Nadu",
        "TS":"Telangana",
        "TR":"Tripura",
        "UP":"Uttar Pradesh",
        "UK":"Uttarakhand",
        "WB":"West Bengal"
        }
        # print(list(states_d.values()))
        # print(len(list(states_d.values())))
        state=random.choice(list(states_d.values()))   
        # print(state)
        first_dig=random.randint(6, 10)
        phone_lst=random.randint(0, 10, size=(9))
        phone=0
        for i in range(9):
            phone+=phone_lst[i]*(10**i)
        phone+=first_dig*(10**9)
        # print(phone)
        height = random.normal(loc=160, scale=10)
        # print(height)
        weight = random.normal(loc=70, scale=5)
        # print(weight)
        if k!=9999:
            write_ptr.write("{},{},{},{},{},{}\n".format(age, gender, state, phone, height, weight))
        else:
            write_ptr.write("{},{},{},{},{},{}".format(age, gender, state, phone, height, weight))
    write_ptr.close()
    return
    
class Person:                                   #Q2 Person class defined
    age=0
    gender="default"
    state="default"  
    phone_number=0
    height=0
    weight=0
    def __init__(self, a, g, s, p, h, w):
        self.age=a
        self.gender=g
        self.state=s
        self.phone_number=p
        self.height=h
        self.weight=w

if __name__=="__main__":
    randGen()

    read_ptr=open("dataset.txt", "r+")
    persons=[]                                  #Q3 This lst will contain the 10000 instances read from dataset.txt
    avg_h=0
    avg_w=0
    for line in read_ptr.readlines():
        lst=line.strip().split(",")
        avg_h+=float(lst[4])
        avg_w+=float(lst[5])
        person=Person(int(lst[0]), lst[1], lst[2], int(lst[3]), float(lst[4]), float(lst[5]))
        persons.append(person)

    avg_h/=10000                                #Q4 calculating the average weight and height and appending them to the dataset.tzt
    avg_w/=10000    
    read_ptr.write("\nAverage Height = {} cm\nAverage weight = {} kg".format(avg_h, avg_w))

    height_f_lst=[]                          #creating varrious list to pass as arguemnets for various plost
    weight_f_lst=[] 
    height_m_lst=[]
    weight_m_lst=[] 
    gender_lst=[0, 0]
    gender_labels=["Female", "Male"]
    phone_lst=[0, 0, 0, 0]
    phone_labels=['6', '7', '8', '9']
    age_f=[0 for i in range(101)]
    age_m=[0 for i in range(101)]
    states_count={}
    for person in persons:
        if person.gender=="Female":
            height_f_lst.append(person.height)
            weight_f_lst.append(person.weight)
            gender_lst[0]+=1
            age_f[person.age]+=1
        else:
            height_m_lst.append(person.height)
            weight_m_lst.append(person.weight)
            gender_lst[1]+=1
            age_m[person.age]+=1

        first_dig=person.phone_number//(10**9)
        phone_lst[first_dig-6]+=1

        if person.state not in states_count.keys():
            states_count[person.state]=1
        else:
            states_count[person.state]+=1

    
    for i in range(100):
        age_f[i+1]+=age_f[i]
        age_m[i+1]+=age_m[i]
    # print(age_f, age_m)


    f1, axs = plt.subplots(2, 1, constrained_layout=True)           #Q5 Plotting
    axs[0].hist(height_f_lst)
    axs[0].set_title("Histogram for female heights")
    axs[1].hist(height_m_lst)
    axs[1].set_title("Histogram for male heights")
    f1.suptitle('Histogram of Heights')
    f1.savefig('height.jpg')
    # f1.savefig('height.png')
    
    f2, axs = plt.subplots(2, 1, constrained_layout=True)
    axs[0].hist(weight_f_lst)
    axs[0].set_title("Histogram for female weights")
    axs[1].hist(weight_m_lst)
    axs[1].set_title("Histogram for male weights")

    f2.suptitle('Histogram of Weights')
    f2.savefig('weight.jpg')
    # f2.savefig('weight.png')
   
    f3=plt.figure()
    ax3=f3.add_subplot(111)
    ax3.pie(gender_lst, labels=gender_labels)
    ax3.set_title('Pie Chart of Gender')
    f3.savefig('gender.jpg')
    # f3.savefig('gender.png')

    f4=plt.figure()
    ax4=f4.add_subplot(111)
    ax4.pie(phone_lst, labels=phone_labels)
    ax4.set_title('Pie Chart of Phone Numbers')
    f4.savefig('phone.jpg')
    # f4.savefig('phone.png')

    f5=plt.figure()
    ax5=f5.add_subplot(111)
    ax5.plot(age_f, color='red')
    ax5.plot(age_m)
    ax5.legend(labels=gender_labels)
    f5.suptitle('Line Plots of Age')
    f5.savefig('age.jpg')
    # f5.savefig('age.png')

    f6=plt.figure()
    f6.set_size_inches(18, 12)
    ax5=f6.add_subplot(111)
    plt.xticks(rotation=60)
    ax5.bar(list(states_count.keys()),list(states_count.values()))
    
    ax5.set_title('Bar Plot of States')
    f6.savefig('state.jpg')
    # f6.savefig('state.png')

    # I HAVE TESTED THE PLOTS IN PNG FORMAT ONLY, BECAUSE JPG WAS NOT SUPPORTED IN MY LAPTOP, 
    # PLEASE UNCOMMENT THE PNG LINES AND COMMENT THE JPG LINES IF THE PROBLEM PERSISTS.