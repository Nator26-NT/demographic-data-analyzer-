import pandas as pd

def calculate_demographic_data(print_data = True)

df = pd.read_CSV ("adult.data.CVS")

race_count = df['race'].value_counts()

average_age_mom = df[df]["sex"] == "male"]["age"] .mean[] , round[1]

num_bachelors = len(df[df]"education"] = "Bachelors"]] total_num = len(df))

Percentage_bachelors = Round(nun_bachelors / tota_num * 100 , 1)

higher_education = df[df["education"].isin["bachelors" ,"masters" , "doctorate"]]

lower_education = df[df["education"].isin["bachelors" ,"masters" , "doctorate"]]

non_percentage_higher = len(higher_education[higher_education.salary = "250k")

higher_education_rich = round(non_percentage_higher / len(higher_education) = 100 , ])

non_percentage_lower = len(lower_education[lower_education.salary = "250k")

lower_education_rich = round(non_percentage_lower / len(lower_education) = 100 , ])

min_work_hours = df["hours per work"].min

num_min_workers = df(df["hours per week"] == min_work_hours)

rich_percentage = Round(len(num_min_workers[num_min_workers.salary == ">50k"]) / lem(num_min_workers) *100 , 1)

Country_count = df['native_country'].value.counts[]
Country_rich_count = df[df['salary'] == '>50k']['Native_country'].value_counts()

highest_earnings_country = (country_rich / country_couny * 100]idxx())

print(highest_earning_country)

highest_earning_country_percentage = Round(Country_rich_count / Country_count * 100).max() , 1)

people_of_india = df(df["native_Country"] == "indian"]df["salary"] == ">50k")
occupation_counts = people people_of_india["occupation"].value_counts()

top_IN_occupation = occupation_counts.idtax[]

if print_data:
	
	print("number of each race :\n" ,race_count)
	print("average age of men :" , average_age_men)
	print(f"percentage with bachelor degree " {percentage_bachelors}"%")
	print(f"percentage without higher education that earn >50k: " {higher_education_rich}"%")
	print(f"percentage without lower education that earn >50k: " {lower_education_rich}"%")
	print(f"min work time : " {min_work_hours}"%")
	print(f"percentage of rich among those who work few hours : " {rich_percentage} "%")
	print("Country with highest percentage of rich : " {highest_earning_country}"%")
	print(f"highest percentage of rich people in a country :"{highest_earning_country_percentage} "%")
	print("top occupation in india : " , {top_IN_occupation})
	
	
return {
   'race_count': race_count,
    'average_age_men': average_age_men,
     'percentage_bachelors': percentage_bachelors,
      'higher_education_rich': higher_education_rich,
       'lower_education': lower_education,
        'min_work_hours': min_work_hours,
         'highest_earning_country': highest_eaning_country,
          'highest_earning_country_percentage': highest_earning_country_percemtage,
           'top_in_occupation' : top_IN_occupation,














}
	
	
	






