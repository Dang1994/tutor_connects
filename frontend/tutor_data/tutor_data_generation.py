import random
import csv

# Sample Indian names
first_names = ["Rajesh", "Suman", "Deepak", "Nidhi", "Amit", "Anjali", "Rahul", "Neha", "Pooja", "Kiran",
               "Aarav", "Aditi", "Abhinav", "Aisha", "Akash", "Alok", "Aman", "Ananya", "Aniket", "Arjun",
               "Arnav", "Ashok", "Avani", "Ayush", "Barun", "Bhavna", "Bhushan", "Chaitanya", "Charu", "Chirag",
               "Daksha", "Darshan", "Deepak", "Dhruv", "Dinesh", "Ekta", "Gaurav", "Gita", "Gopal", "Hari",
               "Harish", "Himanshu", "Hrithik", "Ishaan", "Jaya", "Jayesh", "Jyoti", "Karthik", "Kavita", "Kunal",
               "Lakshmi", "Lavanya", "Laxman", "Manish", "Meena", "Mohit", "Namrata", "Neeraj", "Nitin", "Omkar",
               "Pallavi", "Parul", "Prakash", "Pranjal", "Pratik", "Preeti", "Priya", "Rachit", "Rahul", "Rajesh",
               "Rajni", "Ramesh", "Rani", "Ravi", "Reena", "Riya", "Rohit", "Roma", "Sagar", "Sandeep",
               "Sanjay", "Sanjiv", "Santhosh", "Sarita", "Saurabh", "Shalini", "Shivam", "Shreya", "Sneha", "Sonam",
               "Suresh", "Surya", "Swati", "Tanvi", "Tejashwi", "Trisha", "Tushar", "Uday", "Varun", "Vikas",
               "Vikram", "Vinay", "Vishal", "Yash", "Zoya", "Aishwarya", "Anushka", "Ayesha", "Deepali", "Gauri",
               "Harpreet", "Isha", "Kanika", "Kritika", "Lavish", "Nandini", "Neeta", "Parth", "Raghav", "Rakesh",
               "Ritesh", "Sakshi", "Sameer", "Samar", "Sandeep", "Suman", "Sudhir", "Sunita", "Tanisha", "Urvashi",
               "Vishakha", "Abhay", "Abhijeet", "Akanksha", "Ameer", "Anirudh", "Asha", "Atharv", "Avinash", "Bhargav",
               "Bipin", "Chhavi", "Chintan", "Damini", "Devendra", "Devika", "Divya", "Esha", "Farhan", "Ganesh",
               "Gaurika", "Geeta", "Gopal", "Hitesh", "Indira", "Jatin", "Jivika", "Juhi", "Kavya", "Keshav",
               "Kiran", "Komal", "Kriti", "Lata", "Madhav", "Mansi", "Meenal", "Mithun", "Mohini", "Muskan",
               "Neeraj", "Nikita", "Pallav", "Parthasarathi", "Prasoon", "Prithvi", "Priyanka", "Punit", "Raghavendra",
               "Rajat", "Rakesh", "Ramya", "Rashi", "Riya", "Saanvi", "Shubham", "Shiv", "Shivani", "Siddharth",
               "Simran", "Snehal", "Soni", "Sonu", "Soumya", "Srishti", "Subhash", "Sudha", "Suhas", "Suraj",
               "Surbhi", "Swati", "Tania", "Tejas", "Tejal", "Tushar", "Uday", "Uma", "Upendra", "Urvashi",
               "Vamshi", "Varun", "Vedant", "Vinita", "Vinod", "Vishnu", "Yash", "Yogesh", "Zara", "Aarushi",
               "Abhishek", "Aditya", "Aditi", "Ajay", "Akhila", "Alok", "Amrita", "Ananya", "Anish", "Anurag",
               "Ayaan", "Bhavya", "Chandra", "Dhara", "Dimple", "Divya", "Gaurav", "Gunjan", "Harsha", "Hemal",
               "Hriday", "Indu", "Jagruti", "Jayesh", "Joshi", "Kalyani", "Kaveri", "Lavi", "Madhu", "Malhar",
               "Mitali", "Neha", "Nikita", "Omkar", "Parth", "Pritam", "Rahul", "Rakesh", "Rakhi", "Ram",
               "Rani", "Ravi", "Rishabh", "Ritesh", "Rohini", "Ruchi", "Saket", "Sameer", "Sandeep", "Sanjeev",
               "Sapna", "Saroj", "Saurav", "Shailesh", "Shalini", "Shikha", "Shilpa", "Shreya", "Shyam", "Siddharth",
               "Simi", "Soni", "Sonali", "Soumya", "Suman", "Sunil", "Surendra", "Tarun", "Tanu", "Tanvi",
               "Trisha", "Ujjwal", "Usha", "Aabha", "Aadarsh", "Aakanksha", "Aashish", "Aayushi", "Aditi", "Alisha",
               "Aman", "Anika", "Anvi", "Arpita", "Aryan", "Ashwini", "Bhuvan", "Chaitali", "Charvi", "Chhavi",
               "Chiranjeevi", "Daksh", "Dhananjay", "Divyansh", "Ekansh", "Ganesh", "Gaurav", "Gitali", "Gyanesh",
               "Harini", "Hemant", "Iksha", "Isha", "Jagdish", "Jaya", "Jeet", "Kairav", "Kamala", "Kanak",
               "Karan", "Karishma", "Keshav", "Krishna", "Kushal", "Lavanya", "Lohit", "Mahesh", "Mala",
               "Mandakini", "Manish", "Manju", "Meera", "Meghna", "Mohan", "Naina", "Namita", "Neerja", "Nidhi",
               "Nikhil", "Ojas", "Om", "Padma", "Pallavi", "Palak", "Pankaj", "Pramod", "Pranav", "Pranay",
               "Prashant", "Priyank", "Punit", "Ravi", "Renu", "Riddhi", "Rishabh", "Ritesh", "Rohit", "Ruchi",
               "Saanvi", "Sagar", "Sahil", "Sameer", "Sandhya", "Sanjoy", "Sanjay", "Santosh", "Sarita", "Saurabh",
               "Savita", "Seema", "Shantanu", "Sheela", "Shilpa", "Shubham", "Shraddha", "Shyam", "Siddharth",
               "Simi", "Soni", "Sonali", "Soumya", "Suman", "Sunil", "Surendra", "Tarun", "Tanu", "Tanvi",
               "Trisha", "Ujjwal", "Usha"]

last_names = ["Sahu", "Nayak", "Panda", "Dhal", "Bhoi", "Kumar", "Jena", "Mallick", "Sahu", "Dharam", 
              "Mahapatra", "Samantray", "Mohapatra", "Mohanty", "Bhunia", "Khatua", "Basu", "Kandula", 
              "Barik", "Swain", "Samal", "Chand", "Maharana", "Bhanja", "Patnaik", "Bansal", "Bhatia", 
              "Das", "Mandal", "Routray", "Sardar", "Sethi", "Biswal", "Kar", "Maheshwari", "Mishra", 
              "Sarangi", "Khuntia", "Kumar", "Rout", "Ghosh", "Jadhav", "Sarma", "Pattanaik", "Jani", 
              "Das", "Barik", "Bhoi", "Khuntia", "Patel", "Samantray", "Sahu", "Choudhury", "Ranjan", 
              "Pradhan", "Tripathy", "Nayak", "Maji", "Nanda", "Mohanty", "Bana", "Baran", "Keshari", 
              "Mali", "Rath", "Das", "Bansal", "Khatua", "Senapati", "Sen", "Bhowmick", "Patra", "Kumar", 
              "Sahu", "Rai", "Mallick", "Nanda", "Das", "Dandapat", "Tiwari", "Ray", "Biswas", "Das", 
              "Pradhan", "Maharana", "Das", "Bikash", "Mishra", "Das", "Swain", "Kumar", "Sahu", "Rath", 
              "Nayak", "Maji", "Barik", "Choudhury", "Patel", "Senapati", "Mishra", "Panda", "Dharma", 
              "Thakur", "Ghosh", "Reddy", "Suman", "Pradhan", "Pratap", "Mahapatra", "Nayak", "Kumar", 
              "Patel", "Patnaik", "Dandapat", "Sahoo", "Kar", "Das", "Mishra", "Kumar", "Bharati", 
              "Swain", "Pradhan", "Sahu", "Nanda", "Barik", "Bansal", "Mahanti", "Mohanty", "Patel", 
              "Sahu", "Bhanja", "Dahal", "Mahapatra", "Mishra", "Thakur", "Rani", "Mallick", "Nayak", 
              "Swarup", "Mahajan", "Ranjan", "Rath", "Kumar", "Thakur", "Bhol", "Khan", "Kumar", "Barik", 
              "Rout", "Srinivas", "Patnaik", "Prasanna", "Mishra", "Nayak", "Panda", "Sahani", "Das", 
              "Bardhan", "Pattanaik", "Das", "Jana", "Nath", "Padhy", "Mohan", "Das", "Tripathy", "Sahu", 
              "Nayak", "Mohanty", "Sahu", "Dash", "Patel", "Pradhan", "Ray", "Rath", "Bhatia", "Kar", 
              "Jena", "Samal", "Pati", "Kumar", "Mohapatra", "Thakur", "Rani", "Sahu", "Barik", "Nayak", 
              "Bansal", "Dash", "Mohapatra", "Choudhury", "Kumar", "Rout", "Sahu", "Pradhan", "Rai", 
              "Das", "Bhanja", "Mali", "Thakur", "Bhoi", "Jana", "Nayak", "Kumar", "Mahanta", "Swain", 
              "Ranjan", "Barik", "Rath", "Dhar", "Mohapatra", "Pattanaik", "Das", "Bansal", "Reddy", 
              "Sarma", "Mishra", "Nayak", "Nanda", "Patel", "Swain", "Dash", "Kumar", "Brahma", "Patra", 
              "Bhatia", "Sahu", "Dhal", "Choudhury", "Reddy", "Mahapatra", "Mallick", "Bhai", "Sahani", 
              "Jena", "Rai", "Das", "Dhal", "Nayak", "Patra", "Rathi", "Kumar", "Das", "Mahapatra", 
              "Maheshwari", "Patel", "Dash", "Rout", "Nath", "Basu", "Panda", "Mohapatra", "Kumar", 
              "Jadhav", "Nanda", "Mishra", "Nayak", "Rath", "Bhanja", "Das", "Mohanty", "Ghosh", "Dharma", 
              "Patra", "Sahu", "Mishra", "Khatua", "Bansal", "Mali", "Dash", "Rai", "Mohapatra", "Ranjan", 
              "Bhatt", "Sahu", "Sain", "Kumar", "Choudhury", "Dharma", "Bhol", "Das", "Kumar", "Mishra", 
              "Rathi", "Swain", "Dhal", "Pradhan", "Patel", "Bhowmick", "Ghosh", "Kumar", "Dash", "Rai"]

# Locations (Western Odisha districts)
locations = ["Kalahandi", "Bhubaneswar", "Nuapada", "Balangir", "Sambalpur", "Deogarh", "Bargarh", "Jharsuguda", "Sundargarh", "Angul", "Mayurbhanj", 
             "Khurda", "Cuttack", "Jagatsinghpur", "Puri", "Dhenkanal", "Nayagarh", "Ganjam", "Gajapati", "Rayagada", "Kandhamal", 
             "Koraput", "Malkangiri", "Nabarangpur", "Bolangir", "Dhenkanal", "Jajpur", "Kendrapara", "Balasore", "Bhadrak", 
             "Jagatsinghpur", "Keonjhar", "Mayurbhanj", "Cuttack", "Khurda", "Nayagarh", "Puri", "Sambalpur", "Jharsuguda", 
             "Deogarh", "Bargarh", "Kalahandi", "Nuapada", "Angul", "Sundargarh", "Rayagada", "Ganjam", "Gajapati", "Kandhamal", 
             "Koraput", "Malkangiri", "Nabarangpur", "Bolangir", "Dhenkanal", "Jajpur", "Kendrapara", "Balasore", "Bhadrak", 
             "Jagatsinghpur", "Keonjhar"]


# Subjects and Grade Levels
subjects = ["English", "Hindi", "Mathematics", "Environmental Studies", "Art and Craft", "Physical Education", "Music", "Dance",
            "Moral Science", "General Science", "Social Studies", "Computer Science", "History", "Geography", 
            "Political Science", "Economics", "Physics", "Chemistry", "Biology", "Business Studies", "Accountancy", 
            "Sociology", "Psychology", "Statistics", "Informatics Practices"]

grade_levels = ["Class 1-5 CHSE",  "Class 1-5 CBSE", "Class 1-5 ICSE", "Class 1-5 all", "Class 1-5 CHSE & CBSE", "Class 6-10 CHSE",
                "Class 6-10 CBSE", "Class 6-10 ICSE", "Class 6-10 all", "Class 6-10 CHSE & CBSE", "Only 9th-10th CHSE",
                "Only 9th-10th CBSE", "Only 9th-10th ICSE", "Only 9th-10th all", "Only 9th-10th CHSE & CBSE", "Class 11-12 CHSE",  
                "Class 11-12 CBSE", "Class 11-12 ICSE", "Class 11-12 all", "Class 11-12 CHSE & CBSE"]

# Education levels
education_levels = ["B.Sc", "M.Sc", "B.Ed", "M.A", "PhD"]

# Function to generate a random Indian phone number
def generate_phone():
    return random.choice([9, 8, 7]) * 10**9 + random.randint(100000000, 999999999)

# Generate email based on name
def generate_email(first_name, last_name):
    return f"{first_name.lower()}.{last_name.lower()}@gmail.com"

# Generate random tutoring rates
def generate_rates():
    return random.randint(300, 1000)  # Rates between 300 and 1000 INR

# Generate random years of experience
def generate_experience():
    return random.randint(1, 20)  # 1 to 20 years of experience

# Generate the dataset
with open('tutor_dataset.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Phone", "Email", "Location", "Subjects", "Grade_Level", "Tutoring_Approach", "Rates_Per_Hour", 
                     "Mode_of_Tutoring", "Experience_Years", "Education"])
    
    for _ in range(10000):  # Generating 10,000 rows
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        name = f"{first_name} {last_name}"
        phone = generate_phone()
        email = generate_email(first_name, last_name)
        location = random.choice(locations)
        subject = random.choice(subjects)
        grade_level = random.choice(grade_levels)
        tutoring_approach = "Interactive and student-centered"
        rates_per_hour = generate_rates()
        mode_of_tutoring = random.choice(["Online", "In-person", "Both"])
        experience_years = generate_experience()
        education = random.choice(education_levels)
        
        writer.writerow([name, phone, email, location, subject, grade_level, tutoring_approach, rates_per_hour, 
                         mode_of_tutoring, experience_years, education])

print("Dataset generated successfully!")
