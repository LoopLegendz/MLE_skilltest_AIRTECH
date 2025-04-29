import sqlite3
from typing import Tuple, List
from tabulate import tabulate

# Create an in-memory SQLite database.
def create_connection(db_path: str = ":memory:") -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
    """
    Create a database connection and return both connection and cursor.
    
    Args:
        db_path (str): Path to the database file, defaults to in-memory database
        
    Returns:
        tuple: (Connection, Cursor) objects
    """
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    return conn, cur


def create_tables(cur: sqlite3.Cursor) -> None:
    """
    Create the necessary database tables if they don't exist.
    
    Args:
        cur (sqlite3.Cursor): Database cursor
    """
    # Create the country table
    cur.execute("""
        CREATE TABLE if not exists countries (
            country_id VARCHAR (2) PRIMARY KEY,
            country_name VARCHAR (40) DEFAULT NULL,
            region VARCHAR(10) NOT NULL 
        )
    """)

    # Create the users table
    # NB: I changed the employee_id to be an INTEGER PRIMARY KEY AUTOINCREMENT 
    # because its the translation of SERIAL PRIMARY KEY in SQLite
    # NB: I changed department_id into department so the INSERT statement can work.
    cur.execute("""
        CREATE TABLE if not exists employees (
            employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name VARCHAR (20) DEFAULT NULL,
            last_name VARCHAR (25) NOT NULL,
            email VARCHAR (100) NOT NULL,
            phone_number VARCHAR (20) DEFAULT NULL,
            manager_id INT DEFAULT null REFERENCES employees (employee_id),
            department VARCHAR(30) DEFAULT NULL,
            country_id VARCHAR (2) REFERENCES countries (country_id) 
        )
    """)

def insert_data(cur: sqlite3.Cursor) -> None:
    """
    Insert a new user into the database.
    
    Args:
        cur (sqlite3.Cursor): Database cursor
        name (str): User's name
        email (str): User's email
    """
    cur.executescript("""
        INSERT INTO countries (country_id, country_name, region) VALUES
        ('AR','ARGENTINA','lamr'),
        ('BR','BRAZIL','lamr'),
        ('ES','SPAIN','euro'),
        ('FR','FRANCE','euro'),
        ('GB','UNITED KINGDOM','euro'),
        ('HK','HONG KONG','asia'),
        ('IT','ITALY','euro'),
        ('US','UNITED STATES','namr');
    
        INSERT INTO employees (first_name, last_name, email, phone_number, manager_id, department, country_id)
        VALUES ('Jean','AAA', 'jean.aaa@mycompany.fr', '32359949', NULL, 'Sales', 'FR');
        INSERT INTO employees (first_name, last_name, email, phone_number, manager_id, department, country_id)
        VALUES ('Michel','BBB', 'michel.bbb@mycompany.es', '81945947', '1', 'HR', 'ES');
        INSERT INTO employees (first_name, last_name, email, phone_number, manager_id, department, country_id)
        VALUES ('Juliane','CCC', 'juliane.ccc@mycompany.br', '87622749', '1', 'Sales', 'BR');
        INSERT INTO employees (first_name, last_name, email, phone_number, manager_id, department, country_id)
        VALUES ('Patrice','DDD', 'patrice.ddd@mycompany.hk', '13931578', '1', 'HR', 'HK');
        INSERT INTO employees (first_name, last_name, email, phone_number, manager_id, department, country_id)
        VALUES ('Louis','EEE', 'louis.eee@mycompany.fr', '68154273', '1', 'Sales', 'FR');
        INSERT INTO employees (first_name, last_name, email, phone_number, manager_id, department, country_id)
        VALUES ('Albert','FFF', 'albert.fff@mycompany.hk', '63142944', NULL, 'IT', 'HK');
        INSERT INTO employees (first_name, last_name, email, phone_number, manager_id, department, country_id)
        VALUES ('Ludivine','GGG', 'ludivine.ggg@mycompany.fr', '63280299', '6', 'IT', 'FR');
        INSERT INTO employees (first_name, last_name, email, phone_number, manager_id, department, country_id)
        VALUES ('Sophie','HHH', 'sophie.hhh@mycompany.br', '66811818', '6', 'IT', 'BR');
        INSERT INTO employees (first_name, last_name, email, phone_number, manager_id, department, country_id)
        VALUES ('Camille','III', 'camille.iii@mycompany.gb', '24205021', '6', 'Sales', 'GB');
        INSERT INTO employees (first_name, last_name, email, phone_number, manager_id, department, country_id)
        VALUES ('Frank','JJJ', 'frank.jjj@mycompany.it', '83318015', NULL, 'Sales', 'IT');
        INSERT INTO employees (first_name, last_name, email, phone_number, manager_id, department, country_id)
        VALUES ('Thomas','KKK', 'thomas.kkk@mycompany.ar', '20430282', '9', 'Sales', 'AR');
        INSERT INTO employees (first_name, last_name, email, phone_number, manager_id, department, country_id)
        VALUES ('Eric','LLL', 'eric.lll@mycompany.us', '86227391', '9', 'HR', 'US');
        INSERT INTO employees (first_name, last_name, email, phone_number, manager_id, department, country_id)
        VALUES ('Thierry','MMM', 'thierry.mmm@mycompany.gb', '93130273', '9', 'Sales', 'GB');
        INSERT INTO employees (first_name, last_name, email, phone_number, manager_id, department, country_id)
        VALUES ('Nathalie','NNN', 'nathalie.nnn@mycompany.es', '41576574', '9', 'IT', 'ES'); 
    """)

def run_query(cur: sqlite3.Cursor, sql: str) -> None:
    """
    Execute a query and print results in a neat, pipe-separated table.
    """
    cur.execute(sql)
    rows = cur.fetchall()
    headers = [col[0] for col in cur.description]
    print(tabulate(rows, headers=headers, tablefmt="fancy_grid", showindex=False))

def answer_q1(cur: sqlite3.Cursor) -> None:
    """
    Answer question 1: all employees sorted by country name
    """
    sql1 = """
        SELECT e.*
        FROM employees AS e
        JOIN countries AS c 
        ON e.country_id = c.country_id
        ORDER BY c.country_name;
    """
    print("\n--- Q1: Employees sorted by country ---")
    run_query(cur, sql1)
    
def answer_q2(cur: sqlite3.Cursor) -> None:
    """
    Answer question 2: all employees having a manager
    """
    sql2 = """
        SELECT e.*
        FROM employees AS e
        WHERE e.manager_id IS NOT NULL;
    """
    print("\n--- Q2: Employees having a manager ---")
    run_query(cur, sql2)

def answer_q3(cur: sqlite3.Cursor) -> None:
    """
    Answer question 3: all managers' details (being manager of at least one person)
    """
    sql3 = """
        SELECT DISTINCT m.*
        FROM employees AS m
        JOIN employees AS e
            ON m.employee_id = e.manager_id
    """
    print("\n--- Q3: Managers' details ---")
    run_query(cur, sql3)


def answer_q4(cur: sqlite3.Cursor) -> None:
    """
    Answer question 4: employees with their manager names
    """
    sql_q4 = """
        SELECT 
            e.employee_id,
            e.first_name      AS employee_first_name,
            e.last_name       AS employee_last_name,
            e.department,
            e.country_id,
            m.first_name      AS manager_first_name,
            m.last_name       AS manager_last_name
        FROM employees AS e
        JOIN employees AS m
            ON e.manager_id = m.employee_id
    """
    print("\n--- Q4: Employees with their manager names ---")
    run_query(cur, sql_q4)

def answer_q5(cur: sqlite3.Cursor) -> None:
    """
    Answer question 5: do the same request as 4. but including people with no managers" 
    """
    sql_q5 = """
        SELECT 
            e.employee_id,
            e.first_name      AS employee_first_name,
            e.last_name       AS employee_last_name,
            e.department,
            e.country_id,
            m.first_name      AS manager_first_name,
            m.last_name       AS manager_last_name
        FROM employees AS e
        LEFT JOIN employees AS m
            ON e.manager_id = m.employee_id;
    """
    print("\n--- Q5: All Employees and their managers (even those without managers) ---")
    run_query(cur, sql_q5)

def answer_q6(cur: sqlite3.Cursor) -> None:
    """
    Answer question 6: return the number of employees per country sorted by descending order and using the "countries" table to display the country name and region.
    """
    sql_q6 = """
        SELECT 
            c.country_name,
            c.region,
            COUNT(e.employee_id) AS employee_count
        FROM countries AS c
        LEFT JOIN employees AS e
            ON c.country_id = e.country_id
        GROUP BY 
            c.country_name,
            c.region
        ORDER BY 
            employee_count DESC;
    """
    print("\n--- Q6: Number of employees per country ---")
    run_query(cur, sql_q6)

def answer_q7(cur: sqlite3.Cursor) -> None:
    """
    Answer question 7: do the same request but only display the countries for which there are more than one employee.
    """
    sql_q7 = """
        SELECT 
            c.country_name,
            c.region,
            COUNT(e.employee_id) AS employee_count
        FROM countries AS c
        LEFT JOIN employees AS e
            ON c.country_id = e.country_id
        GROUP BY 
            c.country_name,
            c.region
        HAVING 
             COUNT(e.employee_id) > 1
        ORDER BY 
            employee_count DESC;
    """
    print("\n--- Q7: Countries with more than one employee ---")
    run_query(cur, sql_q7)


if __name__ == "__main__":
    conn, cur = create_connection()
    create_tables(cur)
    insert_data(cur)
    
    answer_q1(cur)
    answer_q2(cur)
    answer_q3(cur)
    answer_q4(cur)
    answer_q5(cur)
    answer_q6(cur)
    answer_q7(cur)

    conn.close()
