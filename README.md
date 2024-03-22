# HPD
hpd-personal-project

# Background
Utilizng public open dataset from NYC Housing Perservation & Development, this analysis focuses on this analysis focuses on buildings selected for 
participation in the Underlying Conditions Program. Mandated by Local Law 6 of 2013, this program targets buildings based on the quantity and severity 
of class "B" and "C" violations, primarily related to mold or water leaks, issued by the Department of Housing Preservation and Development (HPD) within 
the previous year. Before designation, an inspection is conducted to verify the presence of these conditions.

# Approach
Created a backend system with routes fetching data from a JSON dataset and implemented a frontend system that fetches data from 
backend API endpoints. Dealing with large dataset, I filtered by borough, totaling the number of units for each borough, and then repeated for postcode 
in order to draw conclusions fo develop insights based on borough and postcode. With final aggregated total units for each borough and postcode, 
I charting the findings for a clear visual representation of the data, leading with impact.

# Visuals
<img width="647" alt="Screen Shot 2024-03-21 at 10 23 20 PM" src="https://github.com/DorahelyS/HPD/assets/142290529/6fab10ff-cfd6-4c85-8a09-5302b8cb1465">


# Data Takeaways
1. Bronx has the highest count of units with underlying conditions with violations classified as 'B' or 'C', totaling 5,041 units, representing 42% of the total.
2. Diving even deeper, postal code 11226 located in Brooklyn has the highest count of units with underlying conditions with violations classified as 'B' or 'C', totaling 694 units, which accounts for 6% of the total.
3. Staten Island makes up only 1% of the total units affected by underlying conditions.

# Future data analysis to drive results
1. Demographics: Can I draw any correlations between housing count and other demographics such as income, age, or ethnicity?
2. Mapping Patterns: Can I identify geographical patterns and their correlation with health conditions? Targeting those regions first to strategize unit improvements.
3. Trends Over Time: Can I analyze trends over time? Are these numbers increasing or decreasing?



