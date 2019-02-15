# Data Files:

All of the data that you'll need is available here in the following formats:

- CSV
- Excel
- JSON
- SQL

The files are located in their respective folders, and you may choose to consume them with any library you want. This will allow you to display mock data for delivery. Below you will find the information on the data.

Employee Data:

|      | employee_id | first_name | last_name | street_address | phone_number |
| ---- | :---------: | :--------: | :-------: | :------------: | :----------: |
| Type |     int     |   string   |  string   |     string     |    string    |
| Ex   |      8      |  Abigale   |   Well    |  6 Orin Drive  | 411-740-9062 |

Patient Data:

|      | patient_id | first_name | last_name | street_address | phone_number | therapy_category | drug_name |
| ---- | :--------: | :--------: | :-------: | :------------: | :----------: | ---------------- | --------- |
| Type |    int     |   string   |  string   |     string     |    string    | string           | string    |
| Ex   |     29     |    Erin    |   Croft   |  6 Orin Drive  | 411-740-9062 | Therapy 3        | Cefprozil |

Task Data:

|      | task_id |  task_type  | patient_id | employee_id | due_date | prioirty_level |
| ---- | :-----: | :---------: | :--------: | :---------: | :------: | -------------- |
| Type |   int   |   string    |    int     |     int     |  string  | string         |
| Ex   |   21    | Task Type 3 |     9      |     23      | 3/13/18  | High           |
