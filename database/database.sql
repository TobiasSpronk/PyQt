SELECT  employee.id as "ID", employee.first_name as "First Name", employee.last_name as "Last Name", 
		employee.birthday as "Birthday", employee.department_name as "Department Name", 
		log_position.position as "Position", log_salary.salary as "Salary" FROM employee, log_position, log_salary 
		WHERE employee.id = log_position.employee_id  AND employee.id = log_salary.employee_id 
		AND log_salary.date= (SELECT max(date) FROM log_salary WHERE employee_id = employee.id) 
		AND log_position.date= (SELECT max(date) FROM log_position WHERE employee_id = employee.id)