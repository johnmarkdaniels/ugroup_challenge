# U.Group Challenge Answers
## J. Mark Daniels

### Instructions to Run Solution

### Components of the Solution


### Challenges and Blockers
MacOS Catalina update was causing issues in setting up virtual environments **SOLVED source activate ugroup_challenge**
Balancing database normalization (star or snowflake modular construction) and ease of querying (one big database)
Allow for scaling and evolution of database utilizing modular construction
Many engine sizes are null **Possible Solution: cross reference with similar vehicles to populate LOWER PRIORITY**
Minimize overhead by eliminating redundancy among tables
Cannot import csv directly into sqlite due to table size mismatch **SOLVED**
  Copied original database and imported into Numbers. Found and corrected error in row 22782. 
Importing only one column at a time when using sqlite3 .import **SOLVED**
Fact Table imports of foreign keys resulted in gross errors in data as well as Null/NaN values in ID columns.
  Tried recreating Fact Table in SQLite Studio as well as manually through terminal with same results.
  Attempted to create Index on each, but could not import that into Fact Table either.
  Used Studio to create autoincrement ID Columns in Dimension Tables **SOLVED**
  Still won't import into Fact Table correctly

### Attempted Features and Solutions
Began utilizing SQLite Studio to make rapid modifications to database structure.
Attempted to create decentralized star/snowflake structure. Decided to focus on getting something running first.
Tried to use csv space stripper code from Stack Overflow to fix import problems.
Deleted everything and restarted following tutorial in sqlite documentation.
Create Fact table for individual transactions. Include: VIN ID, Store ID, PurchVal
Create Dimension tables for Store_Num and VIN to create separate ID's that cascade any changes to Fact Table.
Created Jupyter Notebook to quickly test changes and implement solutions.
Creating Master Notebook for feature engineering in pandas with python. Will export resultant dataframes to sqlite. Just want to get something working quickly even if it is not pretty (ie perfectly balanced between ease of queries and normalization).

