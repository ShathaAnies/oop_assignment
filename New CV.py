
class Experience:
    def __init__(self, company, job_title, start_date, end_date):
        self.company = company
        self.job_title = job_title
        self.start_date = start_date
        self.end_date = end_date

    def display_experience(self):       
        print(f"Company Name: {self.company}")
        print(f"Job Title: {self.job_title}")
        print(f"Start Date: {self.start_date}")
        print(f"End Date: {self.end_date}")

class Education:
    def __init__(self, degree, institution, completion_date):
        self.degree = degree
        self.institution = institution
        self.completion_date = completion_date

    def display_education(self):
        print(f"The degree is: {self.degree}")
        print(f"The institution is: {self.institution}")
        print(f"Complation date: {self.completion_date}")
        


class Skill:
    def __init__(self, skill, percentage):
        self.skill = skill
        self.percentage = percentage

    def display_skill(self):
        print(f"Skill: {self.skill}")
        print(f"percentage : {self.percentage}")

class CV:

    def __init__(self):
                self.experiences = []
                self.education = []
                self.skills = []


    def add_experience(self):
                    print("...... Experiences ......")
                    company = input("please enter company name: ")
                    job_title = input("please enter job title: ")
                    start_date = input("please enter start date: ")
                    end_date = input("please enter end date: ")

                    experiences = Experience(company, job_title, start_date, end_date)
                    self.experiences.append(experiences)
                    
                    another_experience = input("Do you want to add new experience? Y/N ")
                    if another_experience == 'Y' or another_experience == 'y':
                        self.add_experience()
                    else:
                        print(" OK. Thank you.")
                        


    def add_education(self):
                    print("...... Education ......")
                    degree = input("please enter your degree: ")
                    institution = input("please enter your institution: ")
                    completion_date = input("please enter completion date: ")
                   
                    education = Education(degree, institution, completion_date)
                    self.education.append(education)
                    
                    another_education = input("Do you want to add new education? Y/N ")
                    if another_education == 'Y' or another_education == 'y':
                        self.add_education()
                    else:
                        print(" OK. Thank you.")   




    def add_skill(self):
                    print("...... Skill ......")
                    skill = input("please enter your skill: ")
                    percentage = input("please enter the percentage of skill: ")
                   
                    skills = Skill(skill, percentage)
                    self.skills.append(skills)
                    
                    another_skill = input("Do you want to add new skill? Y/N ")
                    if another_skill == 'Y' or another_skill == 'y':
                        self.add_skill()
                    else:
                        print(" OK. Thank you.") 

    def display_cv(self):
        print("................ CV ....................")
        print(f"Name: {name}")
        print(f"Birth date: {birth_date}")
        if self.experiences == [] :
            print("You Do Not Add Any experience 😊")
        else:
            print("....Experiences....")
            for experience in self.experiences:
                experience.display_experience()
            print("............................")

        if self.education == [] :
            print("You Do Not Add Any education 😊")
        else:
            print("....Education....")
            for education in self.education:
                education.display_education()
            print("............................")

        if self.skills == [] :
            print("You Do Not Add Any skill 😊")
        else:
            print("....Skills....")
            for skill in self.skills:
                skill.display_skill()
            print("............................")



   
        
name = input("Enter your name: ")
birth_date = input("Enter your Birth date: ")  
cv1 = CV()

add_experience = input("Do you want to add experience? Y/N : ")
if add_experience == 'Y' or add_experience == 'y':
    cv1.add_experience()
else:
    print("OK. 😊")

add_education = input("Do you want to add education? Y/N : ")
if add_education == 'Y' or add_education == 'y':
    cv1.add_education()
else:
    print("OK. 😊")

add_skill = input("Do you want to add skill? Y/N : ")
if add_skill == 'Y' or add_skill == 'y':
    cv1.add_skill()
else:
    print("OK. 😊")

cv1.display_cv()