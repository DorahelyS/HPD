# HPD
hpd-personal-project

# Background
Utilizing public open dataset from NYC Housing Preservation & Development (HPD), this analysis focuses on buildings selected for 
participation in the Underlying Conditions Program. Mandated by Local Law 6 of 2013, this program targets buildings based on the quantity and severity 
of class "B" and "C" violations, primarily related to mold or water leaks, issued HPD within the previous year and most recently updated 3/1/2024. 
Important to note, before designation, an inspection is conducted to verify the presence of these conditions.

# Approach
Created a backend system with routes fetching data from a JSON dataset pulled from HPD and implemented a frontend system that fetches data from 
backend API endpoints. Dealing with large dataset, I built an algorithm that filters by borough, totaling the number of units for each borough. Curious about postcode findings, 
I repeated the process in order to draw conclusions to develop insights based solely on borough and postcode. With final aggregated total units for each borough and postcode, 
I charted the findings for a clear visual representation of the data, leading with impact.

# Visuals
<img width="630" alt="visual1" src="https://github.com/DorahelyS/HPD/assets/142290529/2226083a-1a26-469a-917f-bba0c1b2d46c">
<img width="617" alt="visual2" src="https://github.com/DorahelyS/HPD/assets/142290529/1d4a4db9-29c6-4f02-8706-b21434b0756d">
<img width="617" alt="visual3" src="https://github.com/DorahelyS/HPD/assets/142290529/aa252bf0-abc5-4d86-baec-b57e5b40a851">



# Data Takeaways
1. Bronx has the highest count of units with underlying conditions with violations classified as 'B' or 'C', totaling 5,041 units, representing 42% of the total.
2. Diving even deeper, postal code 11226 located in Brooklyn has the highest count of units with underlying conditions with violations classified as 'B' or 'C', totaling 694 units, which accounts for 6% of the total.
3. Staten Island makes up only 1% of the total units affected by underlying conditions.

# Future data analysis to drive results
1. Demographics: Can I draw any correlations between housing count and other demographics such as income, age, or ethnicity?
2. Mapping Patterns: Can I identify geographical patterns and their correlation with health conditions? Targeting those regions first to strategize unit improvements.
3. Trends Over Time: Can I analyze trends over time? Are these numbers increasing or decreasing?



