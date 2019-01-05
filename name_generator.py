import random

boy_names = ['Aadesh', 'Aadi', 'Aakash', 'Aarav', 'Aarnav', 'Aarush', 'Aayush', 'Abeer', 'Abhay', 'Abhijeet',
             'Abhimanyu', 'Abhiram', 'Abhishek', 'Adit', 'Aditya', 'Adnan', 'Advaith', 'Advay', 'Advik', 'Agastya',
             'Ajay', 'Akarsh', 'Akshay', 'Amandeep', 'Amol', 'Anay', 'Anik', 'Aniruddh', 'Anirudh', 'Anmol', 'Ansh',
             'Arin', 'Arjun', 'Arnav', 'Arush', 'Aryan', 'Atharv', 'Avi', 'Ayaan', 'Ayush', 'Ayushman', 'Azad',
             'Bharat', 'Bhavin', 'Bodhi', 'Chandan', 'Chetan', 'Chirag', 'Daksh', 'Dalip', 'Darsh', 'Darshit', 'Deepak',
             'Dev', 'Devansh', 'Dhruv', 'Dinesh', 'Divit', 'Divyansh', 'Eklavya', 'Eshan', 'Faiyaz', 'Farhan', 'Gaurav',
             'Gautam', 'Govinda', 'Gurdeep', 'Gurkiran', 'Hansh', 'Hari', 'Harikiran', 'Harish', 'Harsh', 'Harshil',
             'Hemant', 'Himmat', 'Hredhaan', 'Hrithik', 'Indra', 'Indrajit', 'Indranil', 'Ishaan', 'Jagan', 'Jai',
             'Jayesh', 'Kabir', 'Kalpit', 'Kamal', 'Karan', 'Karthik', 'Kiaan', 'Krish', 'Krishna', 'Kushal', 'Laksh',
             'Lakshay', 'Lakshit', 'Lalit', 'Madhavaditya', 'Madhup', 'Manan', 'Manish', 'Mehul', 'Mitul', 'Mohan',
             'Nachiket', 'Naksh', 'Nakul', 'Navin', 'Neel', 'Neerav', 'Neil', 'Nishith', 'Ojas', 'Om', 'Parth',
             'Pranav', 'Pranay', 'Praneel', 'Pranit', 'Pratyush', 'Prem', 'Priyansh', 'Raahithya', 'Rachit', 'Raghav',
             'Rahul', 'Rajesh', 'Rajiv', 'Ramesh', 'Ranbir', 'Ranveer', 'Rayaan', 'Rehaan', 'Reyansh', 'Rishabh',
             'Rishi', 'Rohan', 'Rohit', 'Ronith', 'Rudra', 'Rushil', 'Ryan', 'Sabhya', 'Sahil', 'Sai', 'Saksham',
             'Samaksh', 'Samar', 'Samarth', 'Samesh', 'Sanjay', 'Sarthak', 'Sathvik', 'Shaan', 'Shakti', 'Shaurya',
             'Shivansh', 'Shlok', 'Shray', 'Shreyas', 'Siddharth', 'Tarun', 'Tejas', 'Tushar', 'Uthkarsh', 'Vaibhav',
             'Vedant', 'Veer', 'Viaan', 'Vihaan', 'Vijay', 'Vinod', 'Viraj', 'Vivaan', 'Yakshit', 'Yash', 'Yug', 'Zayn',
             'Zyan']

girl_names = ['Aadhira', 'Aadhya', 'Aadriti', 'Aadya', 'Aahana', 'Aalia', 'Aanya', 'Aaradhya', 'Aarna', 'Aarohi',
              'Aarushi', 'Aarya', 'Aaryahi', 'Aavya', 'Aayra', 'Adah', 'Additri', 'Aditi', 'Advika', 'Adweta', 'Adya',
              'Ahana', 'Akshara', 'Alisha', 'Amaira', 'Amaya', 'Amrita', 'Amruta', 'Amyra', 'Anaisha', 'Ananya',
              'Anaya', 'Andrea', 'Angel', 'Anika', 'Anshika', 'Anvi', 'Anya', 'Aradhana', 'Aradhya', 'Aria', 'Arunima',
              'Arya', 'Avani', 'Avni', 'Ayat', 'Ayesha', 'Bhavna', 'Bhavya', 'Charvi', 'Daksha', 'Dhriti', 'Dhvani',
              'Disha', 'Divija', 'Divya', 'Diya', 'Drishya', 'Eleanor', 'Emma', 'Eva', 'Fatima', 'Gabriella', 'Gauri',
              'Hayaa', 'Hiral', 'Hrishita', 'Inaaya', 'Ira', 'Isha', 'Ishani', 'Ishanvi', 'Ishika', 'Ishita', 'Jasmine',
              'Jhanvi', 'Jia', 'Jivika', 'Jiya', 'Kashvi', 'Kavya', 'Keya', 'Khushi', 'Kiara', 'Krisha', 'Kyra',
              'Lakshmi', 'Maahi', 'Mahika', 'Mahira', 'Maithreyi', 'Manasvi', 'Manly', 'Manya', 'Maria', 'Mary',
              'Maryam', 'Meera', 'Megha', 'Meghana', 'Meher', 'Mia', 'Michelle', 'Misha', 'Mishka', 'Mishti', 'Mitali',
              'Myra', 'Naira', 'Navya', 'Nayantara', 'Neysa', 'Niharika', 'Nisha', 'Nitara', 'Nitya', 'Olivia', 'Pari',
              'Parinaaz', 'Pihu', 'Pranavi', 'Pratyusha', 'Princess', 'Prisha', 'Rachita', 'Raveena', 'Reeva', 'Riddhi',
              'Ridhi', 'Riya', 'Saanvi', 'Sahana', 'Sai', 'Saira', 'Samaira', 'Sana', 'Sanaya', 'Sara', 'Sarah',
              'Saumya', 'Shanaya', 'Shivanya', 'Shravya', 'Shreya', 'Siya', 'Sneha', 'Sophia', 'Sri', 'Suhana',
              'Suhani', 'Swara', 'Tania', 'Tanvi', 'Tanya', 'Tara', 'Tia', 'Tiya', 'Trisha', 'Vaishnavi', 'Vansha',
              'Vanya', 'Vardaniya', 'Veda', 'Vedanshi', 'Vedhika', 'Vedika', 'Vinaya', 'Vrinda', 'Vritika', 'Yashvi',
              'Yazhini', 'Zara', 'Zoe', 'Zoya']


def generator(n_list):
    while len(names_list) < 10:
        name = random.choice(n_list)
        if name not in names_list:
            names_list.append(name)
    for name in sorted(names_list):
        print(name)


print("\t\tBaby name generator\n")
print("1. Boys Names")
print("2. Girls names")
choice = input("\n\nEnter your choice: ")
print("\n\nNames:\n")
names_list = []
if choice == '1':
    generator(boy_names)
elif choice == '2':
    generator(girl_names)
else:
    print("Invalid choice")

