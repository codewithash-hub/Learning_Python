import sqlite3 as sql

conn = sql.connect('cities.db')

cur = conn.cursor()

# cur.execute("CREATE TABLE Cities (CityName TEXT, CityID INT PRIMARY KEY, Population REAL)")

# Sample data for 10 records
data = [
    ('Austin', 28, 25875246),
    ('Boston', 24, 30568456),
    ('Chicago', 32, 11548625),
    ('Denver', 29, 12546215),
    ('Los Angeles', 35, 32548321),
    ('Miami', 22, 16254842),
    ('New York', 31, 21548328),
    ('Phoenix', 27, 11549842),
    ('San Francisco', 30, 15264476),
    ('Seattle', 26, 21548624)
]

# Insert the records into the table
# for record in data:
#     cur.execute("INSERT INTO Cities (CityName, CityID, Population) VALUES (?, ?, ?)", record)


# Display a list of cities sorted by population, in ascending order. 
# asc = cur.execute("SELECT CityName FROM Cities ORDER BY Population ASC")
# asc_results = asc.fetchall()

# for asc_result in asc_results:
#     print(asc_result)

#	Display a list of cities sorted by population, in descending order. 
# desc = cur.execute("SELECT CityName FROM Cities ORDER BY Population DESC")
# desc_results = desc.fetchall()

# for desc_result in desc_results:
#     print(desc_result)

# Display a list of cities sorted by name, in descending order. 
# sort_name = cur.execute("SELECT CityName FROM Cities ORDER BY CityName")
# sort_name_results = sort_name.fetchall()

# for each_sort_by_name in sort_name_results:
#     print(each_sort_by_name)
  
# Display the total population of all the cities.  
# total_population = cur.execute("SELECT SUM(Population) as Total_Population FROM Cities")
# total_pop_results = total_population.fetchone()[0]
# print(f"The Total NUmber of Population is: {total_pop_results}") 

# Display the average population of all the cities. 
# average_population = cur.execute("SELECT AVG(Population) as Average_Population FROM Cities")
# average_pop_results = average_population.fetchone()[0]
# print(f"The Average Number of Population is: {average_pop_results}") 

# Display the city with the highest population. 
# highest_population = cur.execute("SELECT CityName, MAX(Population) FROM Cities")
# highest_pop_results = highest_population.fetchone()[0]
# print(f"The city with the Highest Population is: {highest_pop_results}") 

# Display the city with the lowest population. 
lowest_population = cur.execute("SELECT CityName, MIN(Population) FROM Cities")
lowest_pop_results = lowest_population.fetchone()[0]
print(f"The city with the Lowest Population is: {lowest_pop_results}") 


conn.commit()
conn.close()