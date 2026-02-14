from concurrent.futures import ProcessPoolExecutor

def compute_total_deduction(employee):
    name, salary = employee
    
    # Calculate individual deductions
    sss = salary * 0.045
    philhealth = salary * 0.025
    pagibig = salary * 0.02
    tax = salary * 0.10
    
    total = sss + philhealth + pagibig + tax
    net = salary - total
    
    return name, salary, total, net, sss, philhealth, pagibig, tax

def main():
    print("Data Parallelism - Salary Computation with Deductions")
    print("=" * 60)

    # Get user input for number of employees
    num_employees = int(input("How many employees do you want to enter? "))

    employees = []
    for i in range(num_employees):
        name = input(f"Enter name for employee {i+1}: ")
        salary = float(input(f"Enter salary for {name}: "))
        employees.append((name, salary))

    print("\nProcessing deductions...\n")

    with ProcessPoolExecutor() as executor:
        results = executor.map(compute_total_deduction, employees)
        
        for name, salary, total, net, sss, philhealth, pagibig, tax in results:
            print("-" * 80)
            print(f"Employee: {name}")
            print(f"Initial Salary: ₱{salary:,.2f}")
            print(f"Deductions:")
            print(f"  SSS (4.5%): ₱{sss:,.2f} ({(sss/salary)*100:.1f}%)")
            print(f"  PhilHealth (2.5%): ₱{philhealth:,.2f} ({(philhealth/salary)*100:.1f}%)")
            print(f"  Pag-IBIG (2%): ₱{pagibig:,.2f} ({(pagibig/salary)*100:.1f}%)")
            print(f"  Tax (10%): ₱{tax:,.2f} ({(tax/salary)*100:.1f}%)")
            print(f"Total Deduction: ₱{total:,.2f}")
            print(f"Net Salary: ₱{net:,.2f}")
            print("-" * 80)

if __name__ == "__main__":
    main()